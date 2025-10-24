import tkinter as tk

# Quiz data
quiz_questions = [
    {
        "question": "What does a ZeroDivisionError indicate?",
        "options": ["Invalid syntax", "Division by zero", "Missing argument", "Wrong data type"],
        "answer": 1
    },
    {
        "question": "Which block always executes?",
        "options": ["try", "except", "finally", "raise"],
        "answer": 2
    },
    {
        "question": "What does sys.argv[0] represent?",
        "options": ["First argument", "Script name", "Last argument", "Argument count"],
        "answer": 1
    },
    {
        "question": "Which module provides structured parsing?",
        "options": ["sys", "os", "argparse", "math"],
        "answer": 2
    },
    {
        "question": "What does the raise keyword do?",
        "options": ["Catch an error", "Ignore an error", "Trigger an exception", "Log an error"],
        "answer": 2
    }
]

# GUI setup
window = tk.Tk()
window.title("Python Quiz")
window.geometry("800x700")
window.configure(bg="#1e1e1e")

tk.Label(window, text="Python Quiz: Exception Handling & Command Line Arguments",
         font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e").pack(pady=20)

responses = []
score_label = tk.Label(window, font=("Arial", 16), fg="lightblue", bg="#1e1e1e")
score_label.pack(pady=10)

# Display questions
for q_index, q in enumerate(quiz_questions):
    tk.Label(window, text=f"{q_index + 1}. {q['question']}", font=("Arial", 14),
             fg="white", bg="#1e1e1e").pack(anchor="w", padx=20, pady=(10, 0))
    var = tk.IntVar(value=-1)
    responses.append(var)
    for i, opt in enumerate(q["options"]):
        tk.Radiobutton(window, text=opt, variable=var, value=i, font=("Arial", 12),
                       fg="white", bg="#1e1e1e", selectcolor="#2e2e2e").pack(anchor="w", padx=40)

# Submit button
def submit_quiz():
    score = 0
    for i, var in enumerate(responses):
        if var.get() == quiz_questions[i]["answer"]:
            score += 1
    score_label.config(text=f"Your Score: {score} / {len(quiz_questions)}")

tk.Button(window, text="Submit Quiz", font=("Arial", 14), command=submit_quiz).pack(pady=30)

window.mainloop()
