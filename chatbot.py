import random

# Sample dataset
data = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "order_status": ["where is my order", "track my order", "order status", "has my order shipped"],
    "return_policy": ["how to return a product", "return policy", "can I return my item"],
    "refund_policy": ["when will I get refund", "refund policy", "how do I get my money back"],
    "human": ["talk to human", "speak to agent", "not helpful", "need real support"]
}

# Responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "order_status": "To check your order status, please visit the 'My Orders' section.",
    "return_policy": "You can return any product within 7 days of delivery. Need help initiating a return?",
    "refund_policy": "Refunds are processed within 5–7 business days after product return.",
    "human": "Transferring you to a human agent. Please wait..."
}

# Function to recognize intent
def recognize_intent(user_input):
    user_input = user_input.lower()
    for intent, phrases in data.items():
        for phrase in phrases:
            if phrase in user_input:
                return intent
    return "unknown"

# Chat loop
def chat():
    print("🤖 Chatbot: Hello! Welcome to Customer Support. Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Chatbot: Thank you for contacting us. Have a great day!")
            break
        intent = recognize_intent(user_input)
        if intent != "unknown":
            print(f"🤖 Chatbot: {responses[intent]}")
        else:
            print("🤖 Chatbot: I'm sorry, I didn't understand that. Transferring to human support...")

# Run chatbot
if __name__ == "__main__":
    chat()
