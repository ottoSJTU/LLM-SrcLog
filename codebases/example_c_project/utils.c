#include "utils.h"
#include <string.h>

const char* get_error_prefix() {
    return "[ERROR] ";
}

const char* get_user_status(int user_id) {
    if (user_id < 0) {
        return "Invalid user";
    } else if (user_id == 0) {
        return "Guest user";
    } else {
        return "Registered user";
    }
}

int validate_input(const char* input) {
    if (input == NULL || strlen(input) == 0) {
        return 0;
    }
    return 1;
}
