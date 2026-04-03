#include <iostream>
#include <cstdio>
#include "utils.hpp"

#define LOG_ERROR(fmt, ...) fprintf(stderr, "[ERROR] " fmt "\n", ##__VA_ARGS__)
#define LOG_INFO(fmt, ...) printf("[INFO] " fmt "\n", ##__VA_ARGS__)
#define LOG_DEBUG(msg) std::cout << "[DEBUG] " << msg << std::endl

int main() {
    int user_id = 456;
    std::string input = "test_input";

    // Test 1: Simple printf
    printf("C++ Application started\n");

    // Test 2: printf with variable
    printf("User ID: %d\n", user_id);

    // Test 3: LOG_ERROR macro with function call
    LOG_ERROR("Failed to process user: %s", get_user_status(user_id).c_str());

    // Test 4: LOG_INFO with string literal
    LOG_INFO("System status: %s", "Running");

    // Test 5: fprintf with function call
    fprintf(stderr, "Error prefix: %s\n", get_error_prefix().c_str());

    // Test 6: Conditional logging
    if (!validate_input(input)) {
        LOG_ERROR("Invalid input provided");
    }

    // Test 7: std::cout logging
    LOG_DEBUG("Processing user " + std::to_string(user_id));

    // Test 8: printf with multiple variables
    printf("Processing user %d with input %s\n", user_id, input.c_str());

    return 0;
}
