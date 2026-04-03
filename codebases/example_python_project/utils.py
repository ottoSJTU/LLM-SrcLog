"""Utility functions for the example Python project"""

def get_error_prefix():
    """Return error prefix string"""
    return "[ERROR] "

def get_user_status(user_id):
    """Return user status based on user_id"""
    if user_id < 0:
        return "Invalid user"
    elif user_id == 0:
        return "Guest user"
    else:
        return "Registered user"

def validate_input(input_str):
    """Validate input string"""
    if input_str is None or len(input_str) == 0:
        return False
    return True
