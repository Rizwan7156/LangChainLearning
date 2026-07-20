memory = {}

name = input("What is your name? ")
memory["name"] = name

language = input("What is your favorite language? ")
memory["language"] = language

conversation = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print("\nSession Summary:")

        for item in conversation:
            print("-", item)

        print(
            f"\nI remember that your name is "
            f"{memory['name']}"
        )

        print(
            f"I remember that your favorite "
            f"language is {memory['language']}"
        )

        break

    conversation.append(user_input)

    print("Bot:", user_input)