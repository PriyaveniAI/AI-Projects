# ============================================
# P3 Chatbot - Simple AI Chatbot
# No API Key Required!
# ============================================

import tkinter as tk
from tkinter import scrolledtext
import datetime

# ---- Chatbot Brain (No API Key Needed!) ----

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "namaste", "helo"]):
        return "Hello! 👋 How can I help you today?"

    elif any(word in user_input for word in ["how are you", "how r u", "wassup", "what's up"]):
        return "I'm doing great, thank you! 😊 How about you?"

    elif any(word in user_input for word in ["good", "fine", "great", "awesome", "nice"]):
        return "That's wonderful to hear! 🎉 What can I do for you?"

    # Name
    elif any(word in user_input for word in ["your name", "who are you", "what are you"]):
        return "I'm Buddy AI 🤖 - your friendly chatbot assistant! I'm here to help you."

    # Time & Date
    elif any(word in user_input for word in ["time", "clock"]):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is ⏰ {now}"

    elif any(word in user_input for word in ["date", "today", "day"]):
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today is 📅 {today}"

    # Help
    elif any(word in user_input for word in ["help", "what can you do", "features"]):
        return ("I can help you with:\n"
                "• Answering basic questions\n"
                "• Telling time and date\n"
                "• Simple math\n"
                "• Jokes 😄\n"
                "• Motivation 💪\n"
                "Just type and ask me anything!")

    # Math
    elif any(word in user_input for word in ["calculate", "math", "solve", "+"]):
        try:
            # Extract math expression safely
            expression = ''.join(c for c in user_input if c in "0123456789+-*/(). ")
            result = eval(expression)
            return f"The answer is: 🔢 {result}"
        except:
            return "Please type a math problem like: calculate 5 + 3"

    # Jokes
    elif any(word in user_input for word in ["joke", "funny", "laugh", "lol"]):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😂",
            "Why did the computer go to the doctor? Because it had a virus! 💻😄",
            "What do you call a fish without eyes? A fsh! 🐟😂",
            "Why did the math book look sad? Because it had too many problems! 📚😄"
        ]
        import random
        return random.choice(jokes)

    # Motivation
    elif any(word in user_input for word in ["motivat", "inspire", "sad", "depress", "tired", "help me"]):
        quotes = [
            "💪 Believe in yourself! You are stronger than you think!",
            "🌟 Every day is a new opportunity to grow and improve!",
            "🚀 Keep going! Great things take time.",
            "✨ You are capable of amazing things!"
        ]
        import random
        return random.choice(quotes)

    # Weather (simple response)
    elif any(word in user_input for word in ["weather", "rain", "sunny", "temperature"]):
        return "I can't check live weather yet, but you can check weather.com or Google for the latest! 🌤️"

    # Bye
    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit", "close"]):
        return "Goodbye! 👋 Have a wonderful day! Come back anytime 😊"

    # Thanks
    elif any(word in user_input for word in ["thank", "thanks", "thanku", "ty"]):
        return "You're welcome! 😊 Happy to help anytime!"

    # Name of user
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip().title()
        return f"Nice to meet you, {name}! 😊 How can I help you today?"

    # Default response
    else:
        return ("I'm not sure about that, but I'm learning! 🤖\n"
                "Try asking me:\n"
                "• Tell me a joke\n"
                "• What is the time?\n"
                "• Motivate me\n"
                "• Calculate 10 + 5")


# ---- Simple GUI ----

def send_message(event=None):
    user_text = entry.get().strip()
    if not user_text:
        return

    # Show user message
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_text}\n", "user")

    # Get bot response
    response = get_response(user_text)
    chat_area.insert(tk.END, f"Buddy AI: {response}\n\n", "bot")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)


# ---- Build Window ----

window = tk.Tk()
window.title("Buddy AI Chatbot 🤖")
window.geometry("500x600")
window.configure(bg="#1e1e2e")
window.resizable(False, False)

# Title Label
title = tk.Label(window, text="🤖 Buddy AI Chatbot", font=("Arial", 16, "bold"),
                 bg="#6366f1", fg="white", pady=12)
title.pack(fill=tk.X)

subtitle = tk.Label(window, text="No API Key Required ✅", font=("Arial", 9),
                    bg="#1e1e2e", fg="#94a3b8")
subtitle.pack(pady=2)

# Chat Area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED,
                                       font=("Arial", 11), bg="#2d2d3f", fg="white",
                                       insertbackground="white", padx=10, pady=10,
                                       relief=tk.FLAT)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="#a5b4fc", font=("Arial", 11, "bold"))
chat_area.tag_config("bot", foreground="#86efac", font=("Arial", 11))

# Welcome message
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Buddy AI: Hello! 👋 I'm Buddy AI, your chatbot!\nType a message below and press Enter or click Send!\n\n", "bot")
chat_area.config(state=tk.DISABLED)

# Input Frame
input_frame = tk.Frame(window, bg="#1e1e2e")
input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

entry = tk.Entry(input_frame, font=("Arial", 12), bg="#2d2d3f", fg="white",
                 insertbackground="white", relief=tk.FLAT, bd=8)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
entry.bind("<Return>", send_message)
entry.focus()

send_btn = tk.Button(input_frame, text="Send ➤", font=("Arial", 11, "bold"),
                     bg="#6366f1", fg="white", relief=tk.FLAT, cursor="hand2",
                     padx=12, pady=8, command=send_message)
send_btn.pack(side=tk.RIGHT, padx=(8, 0))

# Footer
footer = tk.Label(window, text="Press Enter or click Send to chat",
                  font=("Arial", 8), bg="#1e1e2e", fg="#64748b")
footer.pack(pady=(0, 6))

window.mainloop()
