"""Main module for the example Python project"""

import logging
from utils import get_error_prefix, get_user_status, validate_input

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    user_id = 789
    input_str = "test_input"

    # Test 1: Simple print
    print("Python Application started")

    # Test 2: logging.info with variable
    logging.info("User ID: %d", user_id)

    # Test 3: logger.error with function call
    logger.error("Failed to process user: %s", get_user_status(user_id))

    # Test 4: logging.warning with string literal
    logging.warning("System status: %s", "Running")

    # Test 5: logger.debug with function call
    logger.debug("Error prefix: %s", get_error_prefix())

    # Test 6: Conditional logging
    if not validate_input(input_str):
        logger.error("Invalid input provided")

    # Test 7: logging.critical with f-string
    logging.critical(f"Processing user {user_id}")

    # Test 8: print with multiple variables
    print(f"Processing user {user_id} with input {input_str}")

if __name__ == "__main__":
    main()
