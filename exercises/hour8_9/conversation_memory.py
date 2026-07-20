conversation_history = []

while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    conversation_history.append(message)

    print("\nConversation Memory:")
    for item in conversation_history:
        print("-", item)