# ============================================
# P6 Quiz App - No API Key Required!
# ============================================

import tkinter as tk
from tkinter import messagebox
import random

# ---- Quiz Questions ----
questions = [
    {
        "question": "What does AI stand for?",
        "options": ["Automated Intelligence", "Artificial Intelligence", "Advanced Internet", "Automated Internet"],
        "answer": "Artificial Intelligence",
        "category": "AI Basics"
    },
    {
        "question": "Which language is most used in AI and Data Science?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": "Python",
        "category": "Programming"
    },
    {
        "question": "What is Machine Learning?",
        "options": ["A robot that learns", "Teaching machines to learn from data", "A computer game", "A programming language"],
        "answer": "Teaching machines to learn from data",
        "category": "AI Basics"
    },
    {
        "question": "What does NLP stand for?",
        "options": ["Natural Language Processing", "New Learning Program", "Neural Logic Processing", "None of these"],
        "answer": "Natural Language Processing",
        "category": "AI Basics"
    },
    {
        "question": "Which of these is a Python library for Machine Learning?",
        "options": ["React", "Django", "Scikit-learn", "Bootstrap"],
        "answer": "Scikit-learn",
        "category": "Programming"
    },
    {
        "question": "What is a Neural Network inspired by?",
        "options": ["Computer chips", "Human brain", "Solar system", "Internet"],
        "answer": "Human brain",
        "category": "AI Basics"
    },
    {
        "question": "What does CSV stand for?",
        "options": ["Comma Separated Values", "Computer Stored Values", "Central Storage Volume", "None of these"],
        "answer": "Comma Separated Values",
        "category": "Data Science"
    },
    {
        "question": "Which library is used for data visualization in Python?",
        "options": ["NumPy", "Pandas", "Matplotlib", "Tkinter"],
        "answer": "Matplotlib",
        "category": "Data Science"
    },
    {
        "question": "What is Deep Learning?",
        "options": ["Learning underwater", "A subset of Machine Learning using neural networks", "A new programming language", "Learning deeply about computers"],
        "answer": "A subset of Machine Learning using neural networks",
        "category": "AI Basics"
    },
    {
        "question": "What is GitHub used for?",
        "options": ["Gaming", "Social media", "Storing and sharing code", "Video editing"],
        "answer": "Storing and sharing code",
        "category": "Programming"
    },
]

# ---- Quiz State ----
current_question = 0
score = 0
selected_answer = None
quiz_questions = []

def start_quiz():
    global current_question, score, quiz_questions, selected_answer
    current_question = 0
    score = 0
    selected_answer = None
    quiz_questions = random.sample(questions, len(questions))
    
    start_frame.pack_forget()
    quiz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    load_question()

def load_question():
    global selected_answer
    selected_answer = None
    next_btn.config(state=tk.DISABLED, bg="#475569")

    q = quiz_questions[current_question]
    
    # Update progress
    progress_label.config(text=f"Question {current_question + 1} of {len(quiz_questions)}")
    score_label.config(text=f"⭐ Score: {score}")
    category_label.config(text=f"📚 {q['category']}")
    
    # Update progress bar
    progress = (current_question / len(quiz_questions)) * 100
    canvas.coords(progress_bar, 0, 0, progress * 4, 20)
    
    # Update question
    question_label.config(text=q["question"])
    
    # Update options
    shuffled = q["options"][:]
    random.shuffle(shuffled)
    
    for i, btn in enumerate(option_buttons):
        btn.config(text=shuffled[i], bg="#1e293b", fg="white",
                  activebackground="#3b82f6", state=tk.NORMAL,
                  command=lambda o=shuffled[i]: check_answer(o))

def check_answer(selected):
    global score, selected_answer
    selected_answer = selected
    q = quiz_questions[current_question]
    correct = q["answer"]
    
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
        if btn["text"] == correct:
            btn.config(bg="#10b981", fg="white")
        elif btn["text"] == selected and selected != correct:
            btn.config(bg="#ef4444", fg="white")
    
    if selected == correct:
        score += 1
        score_label.config(text=f"⭐ Score: {score}")
    
    next_btn.config(state=tk.NORMAL, bg="#3b82f6")

def next_question():
    global current_question
    current_question += 1
    
    if current_question >= len(quiz_questions):
        show_result()
    else:
        load_question()

def show_result():
    quiz_frame.pack_forget()
    result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    total = len(quiz_questions)
    percentage = (score / total) * 100
    
    if percentage == 100:
        emoji = "🏆"
        msg = "Perfect Score! Outstanding!"
        color = "#fbbf24"
    elif percentage >= 80:
        emoji = "🌟"
        msg = "Excellent! Great job!"
        color = "#10b981"
    elif percentage >= 60:
        emoji = "👍"
        msg = "Good! Keep learning!"
        color = "#3b82f6"
    else:
        emoji = "💪"
        msg = "Keep practicing! You can do it!"
        color = "#f59e0b"
    
    result_emoji.config(text=emoji)
    result_title.config(text=msg, fg=color)
    result_score.config(text=f"{score} / {total}")
    result_percent.config(text=f"{percentage:.0f}%", fg=color)

def restart_quiz():
    result_frame.pack_forget()
    start_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# ---- Build Window ----

window = tk.Tk()
window.title("🎯 AI Quiz App")
window.geometry("520x600")
window.configure(bg="#0f172a")
window.resizable(False, False)

# Header
header = tk.Frame(window, bg="#6366f1", pady=14)
header.pack(fill=tk.X)
tk.Label(header, text="🎯 AI Quiz App", font=("Arial", 20, "bold"),
         bg="#6366f1", fg="white").pack()
tk.Label(header, text="Test your AI & Python knowledge!", font=("Arial", 10),
         bg="#6366f1", fg="#c7d2fe").pack()

# ---- Start Frame ----
start_frame = tk.Frame(window, bg="#0f172a")
start_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

tk.Label(start_frame, text="🤖", font=("Arial", 60),
         bg="#0f172a", fg="white").pack(pady=20)
tk.Label(start_frame, text="Welcome to AI Quiz!", font=("Arial", 18, "bold"),
         bg="#0f172a", fg="white").pack()
tk.Label(start_frame, text="10 questions on AI, Python & Data Science",
         font=("Arial", 11), bg="#0f172a", fg="#94a3b8").pack(pady=5)
tk.Label(start_frame, text="✅ Test your knowledge\n⭐ Score points\n🏆 Get your result",
         font=("Arial", 11), bg="#0f172a", fg="#94a3b8", justify=tk.LEFT).pack(pady=10)

tk.Button(start_frame, text="🚀 Start Quiz!", font=("Arial", 14, "bold"),
          bg="#6366f1", fg="white", relief=tk.FLAT, cursor="hand2",
          padx=30, pady=12, command=start_quiz).pack(pady=20)

# ---- Quiz Frame ----
quiz_frame = tk.Frame(window, bg="#0f172a")

# Progress
top_frame = tk.Frame(quiz_frame, bg="#0f172a")
top_frame.pack(fill=tk.X, pady=(0, 5))

progress_label = tk.Label(top_frame, text="Question 1 of 10",
                           font=("Arial", 10, "bold"), bg="#0f172a", fg="#94a3b8")
progress_label.pack(side=tk.LEFT)

score_label = tk.Label(top_frame, text="⭐ Score: 0",
                       font=("Arial", 10, "bold"), bg="#0f172a", fg="#fbbf24")
score_label.pack(side=tk.RIGHT)

# Progress bar
canvas = tk.Canvas(quiz_frame, height=20, bg="#1e293b", highlightthickness=0)
canvas.pack(fill=tk.X, pady=4)
progress_bar = canvas.create_rectangle(0, 0, 0, 20, fill="#6366f1", outline="")

category_label = tk.Label(quiz_frame, text="📚 Category",
                           font=("Arial", 9), bg="#0f172a", fg="#6366f1")
category_label.pack(anchor="w")

# Question
question_frame = tk.Frame(quiz_frame, bg="#1e293b", padx=15, pady=15)
question_frame.pack(fill=tk.X, pady=8)

question_label = tk.Label(question_frame, text="",
                           font=("Arial", 13, "bold"), bg="#1e293b", fg="white",
                           wraplength=450, justify=tk.LEFT)
question_label.pack(anchor="w")

# Options
options_frame = tk.Frame(quiz_frame, bg="#0f172a")
options_frame.pack(fill=tk.X, pady=5)

option_buttons = []
for i in range(4):
    btn = tk.Button(options_frame, text="", font=("Arial", 11),
                    bg="#1e293b", fg="white", relief=tk.FLAT,
                    cursor="hand2", padx=10, pady=10,
                    wraplength=440, justify=tk.LEFT, anchor="w")
    btn.pack(fill=tk.X, pady=3)
    option_buttons.append(btn)

# Next button
next_btn = tk.Button(quiz_frame, text="Next ➤", font=("Arial", 12, "bold"),
                     bg="#475569", fg="white", relief=tk.FLAT, cursor="hand2",
                     padx=20, pady=10, state=tk.DISABLED, command=next_question)
next_btn.pack(pady=10)

# ---- Result Frame ----
result_frame = tk.Frame(window, bg="#0f172a")

result_emoji = tk.Label(result_frame, text="🏆", font=("Arial", 60), bg="#0f172a")
result_emoji.pack(pady=10)

result_title = tk.Label(result_frame, text="", font=("Arial", 18, "bold"),
                        bg="#0f172a", fg="#10b981")
result_title.pack()

tk.Label(result_frame, text="Your Score:", font=("Arial", 12),
         bg="#0f172a", fg="#94a3b8").pack(pady=(20, 0))

result_score = tk.Label(result_frame, text="", font=("Arial", 36, "bold"),
                        bg="#0f172a", fg="white")
result_score.pack()

result_percent = tk.Label(result_frame, text="", font=("Arial", 20, "bold"),
                          bg="#0f172a", fg="#10b981")
result_percent.pack()

tk.Button(result_frame, text="🔄 Play Again", font=("Arial", 13, "bold"),
          bg="#6366f1", fg="white", relief=tk.FLAT, cursor="hand2",
          padx=25, pady=12, command=restart_quiz).pack(pady=20)

window.mainloop()
