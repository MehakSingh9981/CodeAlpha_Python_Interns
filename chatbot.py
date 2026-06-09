def basic_chatbot():
    print("🤖 Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        # Taking input and making it lowercase for easy comparison
        user_input = input("You: ").strip().lower()
        
        # Rule 1: Exit condition
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day ahead!")
            break
            
        # Rule 2: Greetings
        elif user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi! How can I help you today?")
            
        # Rule 3: Well-being check
        elif user_input in ["how are you", "how's it going"]:
            print("🤖 Chatbot: I'm doing fine, thanks for asking! How about you?")
            
        # Rule 4: Handling standard response to well-being
        elif user_input in ["i am fine", "i'm fine", "good", "doing well"]:
            print("🤖 Chatbot: That's wonderful to hear!")
            
        # Rule 5: Basic identity question
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I am a basic Python chatbot created for my CodeAlpha assignment.")
        elif user_input in [""]:
            print("🤖 Chatbot: Your Name is Mehak Singh Maheshwari")
        elif user_input in ["you can help me","help me","suggest some thing for these reason"]:
            print("🤖 Chatbot: Yes Please tell me ,What can i help you ?")     
        # Fallback for unknown inputs
        else:
            print("🤖 Chatbot: I'm sorry, I am a rule-based bot and don't quite understand that yet. Try saying 'hello' or 'how are you'.")

if __name__ == "__main__":
    basic_chatbot()