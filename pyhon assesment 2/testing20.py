# Create a Python library with the function to input the values with expectation handling and demonstrate with the example


# custom_input_library.py

def get_valid_input(prompt, data_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print(error_message)
