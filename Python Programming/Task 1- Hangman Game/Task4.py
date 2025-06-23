# Function to get a reply based on user input
def get_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

# Chat loop
print("Welcome to Basic Chatbot! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = get_reply(user_message)
    print("Bot:", response)

    if user_message.lower().strip() == "bye":
        break
