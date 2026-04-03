# %%
import json
import javalang
import re
import os



LOG_METHODS = ["error", "fatal", "info", "warn", "debug"]

# %%
def print_ast(java_code):
    # Parse Java code
    tree = javalang.parse.parse(java_code)
    
    # Recursively print AST
    def print_node(node, depth=0):
        indent = "  " * depth
        node_type = type(node).__name__
        
        # Handle basic value nodes
        if isinstance(node, (str, int, float, bool)) or node is None:
            print(f"{indent}{node_type}: {node}")
            return
        
        # Handle AST nodes
        print(f"{indent}{node_type}")
        
        # Traverse node attributes
        for attr_name in node.attrs:
            attr_value = getattr(node, attr_name)
            
            # Skip null values
            if attr_value is None:
                continue
                
            # Handle list attributes
            if isinstance(attr_value, list):
                if len(attr_value) > 0:
                    print(f"{indent}  {attr_name}:")
                    for item in attr_value:
                        if isinstance(item, javalang.ast.Node):
                            print_node(item, depth + 2)
                        else:
                            print(f"{indent}    {type(item).__name__}: {item}")
            # Handle node attributes
            elif isinstance(attr_value, javalang.ast.Node):
                print(f"{indent}  {attr_name}:")
                print_node(attr_value, depth + 2)
            # Handle basic type attributes
            else:
                print(f"{indent}  {attr_name}: {attr_value}")

    # Start printing from root node
    print_node(tree)


def preprocess_java_code(code):
    """
    Preprocess Java source code to fix syntax that javalang cannot parse:
    - Replace T[].class with Object.class (T can be any valid type name, including packages or inner classes)
    """
    # Match pattern: type name (allows letters, digits, underscores, dots, $) + [] + .class
    # Example matches: String[].class, java.lang.String[].class, MyClass.Inner[].class
    pattern = r'([a-zA-Z_][\w.$]*\[\s*\])\s*\.\s*class\b'
    
    def replace_match():
        # Replace with "Object.class" (length difference doesn't matter as it's not used for log extraction)
        return "Object.class"
    
    # Execute replacement
    processed_code = re.sub(pattern, replace_match, code)
    return processed_code

# %%
def is_log_method(s):
    return s.lower() in [method.lower() for method in LOG_METHODS]


def extract_log_calls(java_code):
    try:
        tree = javalang.parse.parse(java_code)
    except Exception:
        return []

    log_calls = []
    
    for path, node in tree.filter(javalang.tree.MethodInvocation):
        if is_log_method(node.member):
            position = node.position.line if node.position else "unknown"
            
            # Log template = first argument (must exist)
            if not node.arguments:
                continue  # No arguments, skip
            
            first_arg = node.arguments[0]
            template = ""
            
            if isinstance(first_arg, javalang.tree.Literal):
                val = first_arg.value
                if isinstance(val, str) and len(val) >= 2 and val.startswith('"') and val.endswith('"'):
                    template = val[1:-1]  # Remove double quotes
                else:
                    template = str(val)
            elif isinstance(first_arg, javalang.tree.BinaryOperation):
                # Support concatenation like "a" + b + "c", but only keep string literal parts
                template = extract_string_from_binary(first_arg)
            else:
                # First argument is not a string (rare), use placeholder
                template = "undefined template"
            
            log_calls.append({
                "line": position,
                "method": node.member,
                "template": template,
                "full_expression": str(node)
            })
    
    return log_calls

def extract_string_from_binary(node):
    """
    Extract string template from BinaryOperation:
    - Keep content for literals
    - Replace non-literals with {}
    - Only handle + operation
    """
    if isinstance(node, javalang.tree.BinaryOperation) and node.operator == '+':
        left = extract_string_from_binary(node.operandl)
        right = extract_string_from_binary(node.operandr)
        return left + right
    elif isinstance(node, javalang.tree.Literal):
        val = node.value
        if isinstance(val, str) and len(val) >= 2 and val.startswith('"') and val.endswith('"'):
            return val[1:-1]
        else:
            return str(val)
    else:
        # Non-literal expression (e.g., variable, method call) → represent with {}
        return "{}"

def extract_binary_operation(node):
    if isinstance(node, javalang.tree.BinaryOperation) and node.operator == "+":
        left = extract_binary_operation(node.operandl)
        right = extract_binary_operation(node.operandr)
        return left + right
    elif isinstance(node, javalang.tree.Literal):
        # Literal's value might be a quoted string like '"hello"'
        val = node.value
        if isinstance(val, str) and len(val) >= 2 and val.startswith('"') and val.endswith('"'):
            try:
                return val[1:-1]  # Remove quotes
            except:
                pass
        return str(val)
    else:
        return "{}"


def extract_logs_from_directory(src_dir, output_json_path):
    result = {}
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code = f.read()
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")
                    continue

                try:
                    logs = extract_log_calls(code)
                    if logs:
                        result[file_path] = logs
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue

    with open(output_json_path, 'w', encoding='utf-8') as out_file:
        json.dump(result, out_file, indent=2, ensure_ascii=False)

    print(f"✅ Log calls extracted and saved to {output_json_path}")

def find_method_declaration(tree, method_name):
    for path, node in tree.filter(javalang.tree.MethodDeclaration):
        if node.name == method_name:
            return node
    return None

STRING_METHODS = {
    'toUpperCase', 'toLowerCase', 'substring', 'replace', 'indexOf',
    'lastIndexOf', 'contains', 'startsWith', 'endsWith', 'trim',
    'split', 'format', 'valueOf', 'charAt', 'length', 'equals',
    'compareTo', 'concat'
}

def contains_method_invocation(node):
    if isinstance(node, javalang.tree.MethodInvocation):
        return True
    if hasattr(node, 'children'):
        for child in node.children:
            if isinstance(child, list):
                for item in child:
                    if isinstance(item, javalang.ast.Node) and contains_method_invocation(item):
                        return True
            elif isinstance(child, javalang.ast.Node):
                if contains_method_invocation(child):
                    return True
    return False

def extract_all_return_statements(method_node):
    """Recursively traverse method body and extract all ReturnStatement nodes"""
    returns = []

    def _collect_returns(node):
        if isinstance(node, javalang.tree.ReturnStatement):
            returns.append(node)
        elif hasattr(node, 'children'):
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, javalang.ast.Node):
                            _collect_returns(item)
                elif isinstance(child, javalang.ast.Node):
                    _collect_returns(child)

    if hasattr(method_node, 'body') and isinstance(method_node.body, list):
        for stmt in method_node.body:
            _collect_returns(stmt)

    return returns

def extract_method_source_code(method_node, source_code):
    """
    Extract complete source code of MethodDeclaration from original source_code (including method signature and body)
    """
    if not method_node.position or not hasattr(method_node, 'body') or method_node.body is None:
        return str(method_node)

    start_line = method_node.position.line  # Method start line (javalang line numbers start from 1)
    end_line = start_line
    def find_last_position(node):
        nonlocal end_line
        if hasattr(node, 'position') and node.position and node.position.line > end_line:
            end_line = node.position.line
        if hasattr(node, 'children'):
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, javalang.ast.Node):
                            find_last_position(item)
                elif isinstance(child, javalang.ast.Node):
                    find_last_position(child)

    find_last_position(method_node)

    lines = source_code.splitlines()
    if 1 <= start_line <= len(lines) and 1 <= end_line <= len(lines):
        method_lines = lines[start_line - 1: end_line]
        # Try to preserve indentation, return complete method definition
        return "\n".join(method_lines).rstrip()
    else:
        return f"// Method source unavailable (lines {start_line}-{end_line})"


def parse_imports_and_package_v2(java_code, filename="none"):
    """Parse Java file and return (package_name, import_map)"""
    try:
        tree = javalang.parse.parse(java_code)
    except Exception as e:
        return None, {}

    package_name = None
    import_map = {}

    for path, node in tree:
        if isinstance(node, javalang.tree.PackageDeclaration):
            package_name = node.name
        elif isinstance(node, javalang.tree.Import):
            if not node.static and not node.wildcard:
                full_path = node.path
                simple_name = full_path.split('.')[-1]
                import_map[simple_name] = full_path

    return package_name, import_map

def build_class_to_file_map(root_dir):
    """Build class name -> file path mapping, skip all directories containing 'test/'"""
    class_to_file = {}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        normalized_dirpath = dirpath.replace('\\', '/').lower()
        if '/test/' in normalized_dirpath:
            continue

        for filename in filenames:
            if filename.endswith('.java'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        code = f.read()

                    # Try to parse with javalang
                    package, _ = parse_imports_and_package_v2(code, filepath)
                    class_name = filename[:-5]

                    # If parsing fails, try to infer package name from path (assuming standard Maven structure)
                    if package is None:
                        # Assume path contains /src/main/java/ or similar structure
                        parts = dirpath.replace('\\', '/').split('/')
                        if 'java' in parts:
                            java_index = parts.index('java')
                            if java_index + 1 < len(parts):
                                inferred_package = ".".join(parts[java_index + 1:])
                                package = inferred_package

                    class_to_file[class_name] = filepath
                    if package:
                        full_class_name = f"{package}.{class_name}"
                        class_to_file[full_class_name] = filepath

                except Exception as e:
                    continue
    
    return class_to_file

def load_and_parse_file_by_class(class_name, class_to_file_map):
    """Load file by class name"""
    if class_name not in class_to_file_map:
        print(f"❌ Class not found in mapping: {class_name}")
        return None, None

    filepath = class_to_file_map[class_name]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
            tree = javalang.parse.parse(code)
            return tree, code
    except Exception as e:
        print(f"⚠️ Failed to load or parse file {filepath}: {e}")
        return None, None

# ========== Built-in class handling ==========
BUILT_IN_CLASSES = {
    'String', 'Integer', 'Boolean', 'Long', 'Double', 'Float', 'Character'
}

UNRESOLVED = "__UNRESOLVED__"

def resolve_method_invocation_target_v2(invocation_node, current_package, import_map):
    """Resolve MethodInvocation target"""
    qualifier = invocation_node.qualifier
    method_name = invocation_node.member

    # Handle variable or simple identifier as caller
    if isinstance(qualifier, javalang.tree.MemberReference) or isinstance(qualifier, str):
        qual_name = qualifier.member if isinstance(qualifier, javalang.tree.MemberReference) else qualifier

        # Variable style (lowercase start, not imported, no dots), infer common String methods as built-in; otherwise mark as unresolved
        is_variable_like = (
            isinstance(qualifier, javalang.tree.MemberReference) or
            (isinstance(qualifier, str) and qual_name and qual_name[0].islower() and qual_name not in import_map and '.' not in qual_name)
        )
        if is_variable_like:
            if method_name in STRING_METHODS:
                return 'java.lang.String', method_name
            # Unknown variable type function call, mark as unresolved
            return UNRESOLVED, method_name

        # Resolve rest by class name
        if qual_name in import_map:
            return import_map[qual_name], method_name
        elif '.' in qual_name:
            return qual_name, method_name
        else:
            if qual_name in BUILT_IN_CLASSES:
                return 'java.lang.' + qual_name, method_name
            if current_package:
                return f"{current_package}.{qual_name}", method_name
            else:
                return qual_name, method_name
    else:
        # Other complex cases, handled as unresolved by upper layer
        return UNRESOLVED, method_name

def get_source_line(source_code, line_number):
    """Return source code line by line number"""
    lines = source_code.splitlines()
    if 1 <= line_number <= len(lines):
        return lines[line_number - 1].rstrip()
    return ""

def get_invocation_source(invocation_node):
    """Generate human-readable invocation string"""
    def get_literal_or_var_string(expr):
        if isinstance(expr, javalang.tree.Literal):
            return expr.value
        elif isinstance(expr, javalang.tree.MemberReference):
            return expr.member
        elif isinstance(expr, javalang.tree.MethodInvocation):
            return get_invocation_source(expr)
        elif isinstance(expr, str):
            return expr
        else:
            return str(expr)
    
    args_str = ", ".join([get_literal_or_var_string(arg) for arg in invocation_node.arguments]) if hasattr(invocation_node, 'arguments') else ""
    if isinstance(invocation_node.qualifier, javalang.tree.MemberReference):
        qualifier_str = invocation_node.qualifier.member + "."
    else:
        qualifier_str = (invocation_node.qualifier + ".") if invocation_node.qualifier else ""
    return f"{qualifier_str}{invocation_node.member}({args_str})"

def get_enclosing_type_name_from_path(path):
    """Find the nearest type declaration name from method node's path"""
    for p in reversed(path):
        if isinstance(p, (javalang.tree.ClassDeclaration,
                          javalang.tree.EnumDeclaration,
                          javalang.tree.InterfaceDeclaration,
                          javalang.tree.AnnotationDeclaration)):
            return p.name
    return "UnknownClass"

# ========== Path tracing core ==========
def trace_all_log_call_paths_across_files(initial_code, log_call, class_to_file_map):
    """Trace log call paths across files"""
    tree = javalang.parse.parse(initial_code)
    package, import_map = parse_imports_and_package_v2(initial_code)

    # Find MethodDeclaration containing this log call line and its path
    containing_method = None
    containing_method_path = None
    for path, node in tree.filter(javalang.tree.MethodDeclaration):
        if node.position and node.position.line <= log_call['line']:
            if containing_method is None or node.position.line > containing_method.position.line:
                containing_method = node
                containing_method_path = path

    if not containing_method:
        return [[(None, None, "Log method call")]]

    target_log_node = None
    for sub_path, sub_node in containing_method.filter(javalang.tree.MethodInvocation):
        if (sub_node.member in LOG_METHODS and 
            sub_node.position and sub_node.position.line == log_call['line']):
            target_log_node = sub_node
            break

    if not target_log_node:
        return [[(None, None, "Log method call")]]

    # Parse class name that calls the log method
    simple_class_name = get_enclosing_type_name_from_path(containing_method_path)
    current_class_name = f"{package}.{simple_class_name}" if package else simple_class_name

    all_paths = []
    
    # Starting point“Called function info”fixed as“Log method call”
    start_tuple = (current_class_name, get_invocation_source(target_log_node), "Log method call")

    if target_log_node.arguments:
        _trace_method_calls_only(
            path_so_far=[start_tuple],
            expr=target_log_node.arguments[0],
            current_tree=tree,
            current_class=current_class_name,
            current_package=package or "",
            import_map=import_map or {},
            class_to_file_map=class_to_file_map,
            all_paths=all_paths,
            visited=set(),
            terminal_on_no_call=True
        )
    else:
        all_paths.append([start_tuple])

    return all_paths

def _trace_method_calls_only(path_so_far, expr, current_tree, current_class, current_package, import_map, class_to_file_map, all_paths, visited, terminal_on_no_call=True):
    """Only trace method calls; if expression has no method calls, converge current path as needed; mark and end if function is unresolvable"""
    if expr is None:
        all_paths.append(path_so_far[:])
        return

    # Top level: if expression has no method calls at all, converge path
    if terminal_on_no_call and not contains_method_invocation(expr):
        all_paths.append(path_so_far[:])
        return

    if isinstance(expr, javalang.tree.MethodInvocation):
        target_class_full, method_name = resolve_method_invocation_target_v2(expr, current_package, import_map)

        # Unresolvable function, mark and end path
        if target_class_full == UNRESOLVED:
            new_path = path_so_far[:]
            new_path.append((current_class, get_invocation_source(expr), "❓ Unresolvable function"))
            all_paths.append(new_path)
            return
        
        if target_class_full is None:
            target_class_full = current_class

        # If it's Java built-in class, skip tracing but record
        if isinstance(target_class_full, str) and target_class_full.startswith('java.lang'):
            new_path = path_so_far[:]
            new_path.append((target_class_full, get_invocation_source(expr), "✅ Built-in method"))
            all_paths.append(new_path)
            return

        node_sig = f"{target_class_full}.{method_name}"
        if node_sig in visited:
            new_path = path_so_far[:]
            new_path.append((target_class_full, get_invocation_source(expr), "🔄 Already visited"))
            all_paths.append(new_path)
            return

        simple_class_name = target_class_full.split('.')[-1]
        target_tree, target_code = load_and_parse_file_by_class(simple_class_name, class_to_file_map)
        if not target_tree:
            new_path = path_so_far[:]
            new_path.append((target_class_full, get_invocation_source(expr), "❓ Unresolvable function"))
            all_paths.append(new_path)
            return

        target_method_node = find_method_declaration(target_tree, method_name)
        if not target_method_node:
            new_path = path_so_far[:]
            new_path.append((target_class_full, get_invocation_source(expr), "❓ Unresolvable function"))
            all_paths.append(new_path)
            return

        # Extract complete method source code
        full_method_source = extract_method_source_code(target_method_node, target_code)

        new_path = path_so_far[:]
        invocation_source = get_invocation_source(expr)
        new_path.append((target_class_full, invocation_source, full_method_source))

        visited_copy = visited.copy()
        visited_copy.add(node_sig)

        # Continue tracing: based on expressions in return statements (because log value flows from return values)
        return_stmts = extract_all_return_statements(target_method_node)
        if not return_stmts:
            # Method has no return statement (e.g., void method), path terminates here
            all_paths.append(new_path)
        else:
            # Create independent path branch for each return statement
            for ret_stmt in return_stmts:
                if ret_stmt.expression:
                    _trace_method_calls_only(
                        new_path, ret_stmt.expression, target_tree, target_class_full,
                        current_package, import_map, class_to_file_map, all_paths,
                        visited_copy, terminal_on_no_call=True
                    )
                else:
                    # return; no expression
                    all_paths.append(new_path)

    elif isinstance(expr, javalang.tree.BinaryOperation):
        # For binary operations, only trace method calls within; converge path if needed when both sides have no method calls
        left_has_call = contains_method_invocation(expr.operandl)
        right_has_call = contains_method_invocation(expr.operandr)

        if left_has_call:
            _trace_method_calls_only(path_so_far, expr.operandl, current_tree, current_class, current_package, import_map, class_to_file_map, all_paths, visited, terminal_on_no_call=False)
        if right_has_call:
            _trace_method_calls_only(path_so_far, expr.operandr, current_tree, current_class, current_package, import_map, class_to_file_map, all_paths, visited, terminal_on_no_call=False)

        if terminal_on_no_call and not left_has_call and not right_has_call:
            all_paths.append(path_so_far[:])

    else:
        # Other expression types：only allow at top level“converge even without method calls”
        if terminal_on_no_call:
            all_paths.append(path_so_far[:])


# ========== Test functions ==========
def test_full_cross_file_analysis(root_dir):
    class_to_file_map = build_class_to_file_map(root_dir)

    a_class = "Foo"
    if a_class not in class_to_file_map:
        print(f"❌ Entry class not found {a_class}")
        return

    with open(class_to_file_map[a_class], 'r', encoding='utf-8') as f:
        code_a = f.read()

    log_calls = extract_log_calls(code_a)
    if not log_calls:
        print("❌ No log calls extracted")
        return

    print(f"🔍 Extracted {len(log_calls)} log call(s)")

    total_paths = 0

    for idx, log_call in enumerate(log_calls):
        print(f"\n=== Analyzing log call # {idx + 1} log call(s) ===")
        print(f"Location: line {log_call['line']}, method: {log_call['method']}")
        print(f"Template: {log_call['template']}")

        all_paths = trace_all_log_call_paths_across_files(code_a, log_call, class_to_file_map)

        print(f"\n=== 🌐 Call path analysis result ( {len(all_paths)} path(s) in total)===")
        for i, path in enumerate(all_paths, 1):
            print(f"\n--- Path {i} ---")
            for j, (cls, invoc, stmt) in enumerate(path):
                print(f"  {j+1}. Class: {cls}")
                print(f"     Invocation code: {invoc}")
                print(f"     Called function info: {stmt}")

        total_paths += len(all_paths)

    print(f"\n✅ Total {len(log_calls)} log call(s)，found {total_paths} complete path")

def test_full_cross_file_analysis_c_cpp(root_dir):
    """Test function for C/C++ projects"""
    file_to_path_map = build_file_map_c_cpp(root_dir)

    # Look for main.c or main.cpp
    entry_file = None
    for filename in ["main.c", "main.cpp"]:
        if filename in file_to_path_map:
            entry_file = filename
            break

    if not entry_file:
        print(f"❌ Entry file not found (looking for main.c or main.cpp)")
        return

    print(f"✅ Found entry file: {entry_file}")

    with open(file_to_path_map[entry_file], 'r', encoding='utf-8') as f:
        code = f.read()

    log_calls = extract_log_calls_c_cpp(code)
    if not log_calls:
        print("❌ No log calls extracted")
        return

    print(f"🔍 Extracted {len(log_calls)} log call(s)")

    total_paths = 0

    for idx, log_call in enumerate(log_calls):
        print(f"\n=== Analyzing log call #{idx + 1} ===")
        print(f"Location: line {log_call['line']}, method: {log_call['method']}")
        print(f"Template: {log_call['template']}")

        all_paths = trace_all_log_call_paths_across_files_c_cpp(code, log_call, file_to_path_map)

        print(f"\n=== 🌐 Call path analysis result ({len(all_paths)} path(s) in total) ===")
        for i, path in enumerate(all_paths, 1):
            print(f"\n--- Path {i} ---")
            for j, (file, invoc, stmt) in enumerate(path):
                print(f"  {j+1}. File: {file}")
                print(f"     Invocation code: {invoc}")
                print(f"     Called function info: {stmt}")

        total_paths += len(all_paths)

    print(f"\n✅ Total {len(log_calls)} log call(s), found {total_paths} complete path(s)")

def test_full_cross_file_analysis_python(root_dir):
    """Test function for Python projects"""
    file_to_path_map = build_file_map_python(root_dir)

    # Look for main.py
    entry_file = "main.py"
    if entry_file not in file_to_path_map:
        print(f"❌ Entry file not found (looking for main.py)")
        return

    print(f"✅ Found entry file: {entry_file}")

    with open(file_to_path_map[entry_file], 'r', encoding='utf-8') as f:
        code = f.read()

    log_calls = extract_log_calls_python(code)
    if not log_calls:
        print("❌ No log calls extracted")
        return

    print(f"🔍 Extracted {len(log_calls)} log call(s)")

    total_paths = 0

    for idx, log_call in enumerate(log_calls):
        print(f"\n=== Analyzing log call #{idx + 1} ===")
        print(f"Location: line {log_call['line']}, method: {log_call['method']}")
        print(f"Template: {log_call['template']}")

        all_paths = trace_all_log_call_paths_across_files_python(code, log_call, file_to_path_map)

        print(f"\n=== 🌐 Call path analysis result ({len(all_paths)} path(s) in total) ===")
        for i, path in enumerate(all_paths, 1):
            print(f"\n--- Path {i} ---")
            for j, (module, invoc, stmt) in enumerate(path):
                print(f"  {j+1}. Module: {module}")
                print(f"     Invocation code: {invoc}")
                print(f"     Called function info: {stmt}")

        total_paths += len(all_paths)

    print(f"\n✅ Total {len(log_calls)} log call(s), found {total_paths} complete path(s)")

# %%
#Count Java files excluding test files
def count_java_files_excluding_test(root_dir):
    """
    Count all non-test .java files in the root_dir directory.
    Exclusion rule：AnyPathpart（directory name or file name）contains 'test'（case-insensitive) will be ignored。
    
    Args:
        root_dir (str): Root directory to scanPath
    
    Returns:
        int: Number of non-test .java files
    """
    java_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Convert currentPathto lowercase for uniform judgment
        normalized_dirpath = dirpath.replace('\\', '/').lower()
        
        # IfPathcontains '/test/' or ends with '/test' ending，skip entire directory
        if '/test/' in normalized_dirpath or normalized_dirpath.endswith('/test'):
            continue

        for filename in filenames:
            if filename.lower().endswith('.java'):
                java_count += 1

    return java_count


# %%
def count_log_calls_in_directory(src_dir):
    """
    Count total number of log calls in Java files under all non-test directories in the specified directory.
    
    Args:
        src_dir (str): Source code root directoryPath
        
    Returns:
        int: Total number of log calls
    """
    total_log_count = 0

    for root, _, files in os.walk(src_dir):
        # Skip directories containing '/test/' (case-insensitive)
        normalized_root = root.replace('\\', '/').lower()
        if '/test/' in normalized_root:
            continue

        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code = f.read()
                except Exception as e:
                    continue

                try:
                    logs = extract_log_calls(code)
                    total_log_count += len(logs)
                except Exception as e:
                    continue

    return total_log_count


# ========== C/C++ Support ==========

# C/C++ log methods and functions
C_CPP_LOG_FUNCTIONS = [
    "printf", "fprintf", "sprintf", "snprintf",
    "syslog", "LOG_ERROR", "LOG_FATAL", "LOG_INFO",
    "LOG_WARN", "LOG_DEBUG", "LOG_TRACE",
    "logit", "error", "fatal", "debug", "debug2", "debug3",
    "verbose", "do_log2", "error_f", "fatal_f", "debug_f",
    "verbose_f", "logdie"
]

# Map C/C++ function names to log levels
C_CPP_FUNCTION_TO_LEVEL = {
    "printf": "INFO",
    "fprintf": "INFO",
    "sprintf": "INFO",
    "snprintf": "INFO",
    "syslog": "INFO",
    "LOG_ERROR": "ERROR",
    "LOG_FATAL": "FATAL",
    "LOG_INFO": "INFO",
    "LOG_WARN": "WARN",
    "LOG_DEBUG": "DEBUG",
    "LOG_TRACE": "DEBUG",
    "logit": "INFO",
    "error": "ERROR",
    "error_f": "ERROR",
    "fatal": "FATAL",
    "fatal_f": "FATAL",
    "logdie": "FATAL",
    "debug": "DEBUG",
    "debug2": "DEBUG",
    "debug3": "DEBUG",
    "debug_f": "DEBUG",
    "verbose": "INFO",
    "verbose_f": "INFO",
    "do_log2": "INFO"
}

def is_c_cpp_log_function(name):
    """Check if a function name is a C/C++ logging function"""
    return name in C_CPP_LOG_FUNCTIONS

# ========== Python Support ==========

# Python log methods and functions
PYTHON_LOG_FUNCTIONS = [
    "error", "fatal", "info", "warn", "warning",
    "debug", "critical", "exception", "print"
]

def is_python_log_function(name):
    """Check if a function name is a Python logging function"""
    return name in PYTHON_LOG_FUNCTIONS

def detect_language_from_extension(file_path):
    """Detect language from file extension"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.java':
        return 'java'
    elif ext == '.c' or ext == '.h':
        return 'c'
    elif ext in ['.cpp', '.cc', '.cxx', '.hpp', '.hxx']:
        return 'cpp'
    elif ext == '.py':
        return 'python'
    return None

def extract_log_calls_c_cpp(code):
    """
    Extract log calls from C/C++ code using regex-based parsing.
    Supports: printf, fprintf, sprintf, snprintf, syslog, LOG_* macros
    """
    log_calls = []
    lines = code.split('\n')

    # Pattern to match log function calls
    # Matches: function_name(args...)
    pattern = r'(\w+)\s*\('

    for line_num, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('//') or line.strip().startswith('/*'):
            continue

        # Find all function calls in the line
        matches = re.finditer(pattern, line)
        for match in matches:
            func_name = match.group(1)
            if not is_c_cpp_log_function(func_name):
                continue

            # Extract the format string (first string argument)
            # Look for string literals after the function name
            rest_of_line = line[match.end():]

            # Handle fprintf/syslog/do_log2 which have a first non-string argument
            if func_name in ['fprintf', 'syslog', 'do_log2']:
                # Skip first argument, find the format string
                string_match = re.search(r',\s*"([^"]*)"', rest_of_line)
            else:
                # First argument is the format string
                string_match = re.search(r'"([^"]*)"', rest_of_line)

            if string_match:
                template = string_match.group(1)
                # Replace %s, %d, %f, etc. with <.*>
                template = re.sub(r'%[-+0 #]*\*?[0-9]*\.?[0-9]*[hlL]?[diouxXeEfFgGaAcspn%]', '<.*>', template)
            else:
                template = "undefined template"

            # Get log level from function name
            level = C_CPP_FUNCTION_TO_LEVEL.get(func_name, "INFO")

            log_calls.append({
                "line": line_num,
                "method": func_name,
                "template": template,
                "level": level,
                "full_expression": line.strip()
            })

    return log_calls

def parse_includes_c_cpp(code):
    """
    Parse #include directives from C/C++ code.
    Returns a list of included file names.
    """
    includes = []
    lines = code.split('\n')

    for line in lines:
        line = line.strip()
        # Match #include "file.h" or #include <file.h>
        match = re.match(r'#include\s+[<"]([^>"]+)[>"]', line)
        if match:
            include_file = match.group(1)
            # Extract just the filename (remove path if present)
            include_name = os.path.basename(include_file)
            includes.append(include_name)

    return includes

def build_file_map_c_cpp(root_dir):
    """
    Build file name -> file path mapping for C/C++ files.
    Maps both header files (.h, .hpp) and source files (.c, .cpp).
    Skips test directories.
    """
    file_to_path = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        normalized_dirpath = dirpath.replace('\\', '/').lower()
        if '/test/' in normalized_dirpath:
            continue

        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx']:
                filepath = os.path.join(dirpath, filename)
                # Map by filename
                file_to_path[filename] = filepath
                # Also map by basename without extension (for function lookup)
                basename = os.path.splitext(filename)[0]
                if basename not in file_to_path:
                    file_to_path[basename] = filepath

    return file_to_path

def extract_function_definition_c_cpp(code, func_name):
    """
    Extract function definition from C/C++ code using regex.
    Returns the function source code if found, None otherwise.
    """
    # Pattern to match function definitions
    # Matches: return_type function_name(params) { body }
    pattern = r'(\w+[\s\*]+)' + re.escape(func_name) + r'\s*\([^)]*\)\s*\{[^}]*\}'

    match = re.search(pattern, code, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(0)

    return None

def extract_return_statements_c_cpp(func_code):
    """
    Extract return statements from C/C++ function code.
    Returns a list of return statement strings.
    """
    returns = []

    # Pattern to match return statements
    pattern = r'return\s+([^;]+);'

    matches = re.finditer(pattern, func_code)
    for match in matches:
        return_expr = match.group(1).strip()
        returns.append(return_expr)

    return returns

def extract_function_calls_c_cpp(code):
    """
    Extract function calls from C/C++ code.
    Returns a list of function names called in the code.
    """
    calls = []

    # Pattern to match function calls
    pattern = r'(\w+)\s*\('

    matches = re.finditer(pattern, code)
    for match in matches:
        func_name = match.group(1)
        # Skip keywords and common C/C++ constructs
        if func_name not in ['if', 'while', 'for', 'switch', 'sizeof', 'return']:
            calls.append(func_name)

    return calls

def extract_log_calls_python(code):
    """
    Extract log calls from Python code using regex-based parsing.
    Supports: logging.error(), logging.info(), print(), etc.
    """
    log_calls = []
    lines = code.split('\n')

    # Patterns to match log function calls
    # Matches: logging.error(...), logger.info(...), print(...)
    patterns = [
        r'logging\.(\w+)\s*\(',
        r'logger\.(\w+)\s*\(',
        r'(print)\s*\('
    ]

    for line_num, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('#'):
            continue

        for pattern in patterns:
            matches = re.finditer(pattern, line)
            for match in matches:
                func_name = match.group(1)
                if not is_python_log_function(func_name):
                    continue

                # Extract the format string (first string argument)
                rest_of_line = line[match.end():]

                # Look for string literals (single or double quotes)
                string_match = re.search(r'["\']([^"\']*)["\']', rest_of_line)

                if string_match:
                    template = string_match.group(1)
                    # Replace %s, %d, %f, {}, etc. with <.*>
                    template = re.sub(r'%[-+0 #]*\*?[0-9]*\.?[0-9]*[hlL]?[diouxXeEfFgGaAcspn%]', '<.*>', template)
                    template = re.sub(r'\{[^}]*\}', '<.*>', template)
                else:
                    template = "undefined template"

                log_calls.append({
                    "line": line_num,
                    "method": func_name,
                    "template": template,
                    "full_expression": line.strip()
                })

    return log_calls

def parse_imports_python(code):
    """
    Parse import statements from Python code.
    Returns a list of imported module names.
    """
    imports = []
    lines = code.split('\n')

    for line in lines:
        line = line.strip()
        # Match: import module, from module import something
        import_match = re.match(r'import\s+(\w+)', line)
        from_match = re.match(r'from\s+(\w+)\s+import', line)

        if import_match:
            imports.append(import_match.group(1))
        elif from_match:
            imports.append(from_match.group(1))

    return imports

def build_file_map_python(root_dir):
    """
    Build file name -> file path mapping for Python files.
    Maps .py files by their module name (filename without .py).
    Skips test directories.
    """
    file_to_path = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        normalized_dirpath = dirpath.replace('\\', '/').lower()
        if '/test/' in normalized_dirpath or normalized_dirpath.endswith('/test'):
            continue

        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                # Map by filename
                file_to_path[filename] = filepath
                # Also map by module name (without .py extension)
                module_name = filename[:-3]
                if module_name not in file_to_path:
                    file_to_path[module_name] = filepath

    return file_to_path

def extract_function_definition_python(code, func_name):
    """
    Extract function definition from Python code using regex.
    Returns the function source code if found, None otherwise.
    """
    # Pattern to match function definitions
    # Matches: def function_name(params):
    pattern = r'def\s+' + re.escape(func_name) + r'\s*\([^)]*\):[^\n]*\n(?:(?:    |\t).*\n)*'

    match = re.search(pattern, code, re.MULTILINE)
    if match:
        return match.group(0)

    return None

def extract_return_statements_python(func_code):
    """
    Extract return statements from Python function code.
    Returns a list of return statement strings.
    """
    returns = []

    # Pattern to match return statements
    pattern = r'return\s+(.+?)(?:\n|$)'

    matches = re.finditer(pattern, func_code)
    for match in matches:
        return_expr = match.group(1).strip()
        returns.append(return_expr)

    return returns

def trace_all_log_call_paths_across_files_python(initial_code, log_call, file_to_path_map):
    """
    Trace log call paths across Python files.
    Similar to C/C++ version but adapted for Python structure.
    """
    all_paths = []

    # Starting point
    start_tuple = ("CurrentFile", log_call['full_expression'], "Log function call")

    # Simple tracing: just return the initial log call for now
    all_paths.append([start_tuple])

    # Try to find function calls in the log statement
    func_name = log_call['method']
    expr = log_call['full_expression']

    # Extract function calls from the expression
    func_calls = re.findall(r'(\w+)\s*\(', expr)

    # For each function call, try to trace it
    for called_func in func_calls:
        if called_func == func_name or called_func in ['print', 'str', 'int', 'float']:
            continue

        # Try to find the function definition in imported modules
        imports = parse_imports_python(initial_code)

        for import_module in imports:
            if import_module in file_to_path_map:
                import_path = file_to_path_map[import_module]
                try:
                    with open(import_path, 'r', encoding='utf-8') as f:
                        import_code = f.read()

                    func_def = extract_function_definition_python(import_code, called_func)
                    if func_def:
                        path = [start_tuple]
                        path.append((import_module, called_func + "()", func_def))
                        all_paths.append(path)
                        break
                except Exception:
                    continue

    return all_paths if all_paths else [[start_tuple]]

def trace_all_log_call_paths_across_files_c_cpp(initial_code, log_call, file_to_path_map):
    """
    Trace log call paths across C/C++ files.
    Similar to Java version but adapted for C/C++ structure.
    """
    all_paths = []

    # Starting point
    start_tuple = ("CurrentFile", log_call['full_expression'], "Log function call")

    # Extract the format string argument from the log call
    # For most log functions, the format string is the first or second argument
    func_name = log_call['method']

    # Simple tracing: just return the initial log call for now
    # Full cross-file tracing would require more sophisticated parsing
    all_paths.append([start_tuple])

    # Try to find function calls in the log statement
    expr = log_call['full_expression']
    func_calls = extract_function_calls_c_cpp(expr)

    # For each function call, try to trace it
    for called_func in func_calls:
        if called_func == func_name:  # Skip the log function itself
            continue

        # Try to find the function definition in included files
        includes = parse_includes_c_cpp(initial_code)

        for include_file in includes:
            if include_file in file_to_path_map:
                include_path = file_to_path_map[include_file]
                try:
                    with open(include_path, 'r', encoding='utf-8') as f:
                        include_code = f.read()

                    func_def = extract_function_definition_c_cpp(include_code, called_func)
                    if func_def:
                        path = [start_tuple]
                        path.append((include_file, called_func + "()", func_def))
                        all_paths.append(path)
                        break
                except Exception:
                    continue

    return all_paths if all_paths else [[start_tuple]]

if __name__=="__main__":
    test_full_cross_file_analysis("./codebases/example_java_project")
    test_full_cross_file_analysis_c_cpp("./codebases/example_c_project")
    test_full_cross_file_analysis_c_cpp("./codebases/example_cpp_project")
    test_full_cross_file_analysis_python("./codebases/example_python_project")
