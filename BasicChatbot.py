def chatbot():

    print("🤖 Chatbot: Hello! I am a simple chatbot.")
    print("🤖 Chatbot: Type 'bye' to exit.")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is SimpleBot.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


# Start the chatbot
chatbot()