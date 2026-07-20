from middleware import validate_input

text = input("Enter message: ")

try:
    print("Validated:", validate_input(text))
except Exception as ex:
    print(ex)