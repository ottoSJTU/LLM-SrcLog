#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

#define LOG_ERROR(fmt, ...) fprintf(stderr, "[ERROR] " fmt "\n", ##__VA_ARGS__)
#define LOG_INFO(fmt, ...) printf("[INFO] " fmt "\n", ##__VA_ARGS__)

int main() {
    int user_id = 123;
    const char* input = "test_input";

    // Test 1: Simple printf
    printf("Application started\n");

    // Test 2: printf with variable
    printf("User ID: %d\n", user_id);

    // Test 3: LOG_ERROR macro with function call
    LOG_ERROR("Failed to process user: %s", get_user_status(user_id));

    // Test 4: LOG_INFO with string concatenation
    LOG_INFO("System status: %s", "Running");

    // Test 5: fprintf with function call
    fprintf(stderr, "Error prefix: %s\n", get_error_prefix());

    // Test 6: Conditional logging
    if (!validate_input(input)) {
        LOG_ERROR("Invalid input provided");
    }

    // Test 7: printf with multiple variables
    printf("Processing user %d with input %s\n", user_id, input);

    return 0;
}
