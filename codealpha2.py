import nltk
from nltk.chat.util import Chat , reflections

#Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!','Hi there!','Hey!']),
    (r'how are you', ['I am good,thankyou.','I am doing well. How about you?']),
    (r'(.*) your name?', ['I am a chatbot.', 'You can call me program.']),
    (r'bye|goodbye',['Goodbye!','See you later!', 'Take care.']),
]
    
# Create a chatbot
chatbot = Chat(pairs,reflections)

#Function to start the chat
def start_chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Bot:",response)

#Start the chat
start_chat()