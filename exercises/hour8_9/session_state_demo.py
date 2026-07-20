session_state = {
    "user_name": "",
    "topic": ""
}

session_state["user_name"] = input("Enter your name: ")
session_state["topic"] = input("Enter learning topic: ")

print("\nSession State")
print(session_state)