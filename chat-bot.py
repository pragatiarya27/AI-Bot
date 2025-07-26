def rule_based_chatbot():
    print("🤖 Hello! I’m RuleBot. Ask me anything or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ['bye', 'exit', 'quit']:
            print("RuleBot: Goodbye! Have a nice day! 👋")
            break

        # Greetings
        elif any(word in user_input for word in ['hello', 'hi', 'hey']):
            print("RuleBot: Hello there! How can I help you?")

        # Asking about chatbot
        elif "your name" in user_input:
            print("RuleBot: I'm RuleBot, your simple rule-based assistant!")

        # Asking for help
        elif "help" in user_input:
            print("RuleBot: I can answer basic questions. Try asking me about the weather, time, or how I'm doing.")

        # Asking about weather
        elif "weather" in user_input:
            print("RuleBot: I’m not connected to live weather data, but it’s always sunny inside this terminal ☀️")

        # Asking about time
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"RuleBot: The current time is {now}.")

        # Asking how are you
        elif "how are you" in user_input:
            print("RuleBot: I'm just code, but I'm functioning as expected!")

        # Unknown input
        else:
            print("RuleBot: Sorry, I didn’t understand that. Try asking something else.")

# Run the chatbot
rule_based_chatbot()
