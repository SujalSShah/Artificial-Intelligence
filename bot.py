import aiml

# Create the AIML kernel
kernel = aiml.Kernel()

# Load AIML file
kernel.learn("brain/chatbot.aiml")

print("SimpleBot is ready!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = kernel.respond(user_input)
    print("Bot:", response)
