def validate_input(user_input):

    if len(user_input.strip()) == 0:
        raise ValueError("Input cannot be empty")

    return user_input


text = input("Enter message: ")

try:
    print("Validated:", validate_input(text))
except Exception as ex:
    print(ex)