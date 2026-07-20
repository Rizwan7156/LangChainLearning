conversation_history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print("\nConversation Summary:")

        for item in conversation_history:
            print("-", item)

        break

    conversation_history.append(user_input)

    print("Bot:", user_input)