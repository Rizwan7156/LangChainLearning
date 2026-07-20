from middleware import validate_input

def process_request():

    try:

        user_input = input("Enter message: ")

        validated = validate_input(user_input)

        print("Processed:", validated)

    except Exception as ex:

        print(ex)

process_request()