#include "utils.hpp"

std::string get_error_prefix() {
    return "[ERROR] ";
}

std::string get_user_status(int user_id) {
    if (user_id < 0) {
        return "Invalid user";
    } else if (user_id == 0) {
        return "Guest user";
    } else {
        return "Registered user";
    }
}

bool validate_input(const std::string& input) {
    return !input.empty();
}
