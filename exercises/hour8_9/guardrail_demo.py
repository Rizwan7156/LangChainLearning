def guardrail(text):

    if "hack" in text.lower():
        raise ValueError("Blocked by guardrail")

    return text


text = input("Enter request: ")

try:
    print("Accepted:", guardrail(text))
except Exception as ex:
    print(ex)