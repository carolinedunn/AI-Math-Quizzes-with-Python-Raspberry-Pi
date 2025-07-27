import tkinter as tk
from tkinter import messagebox

# Question data (Presidents 1776–1980)
questions = [
    {
        "question": "Who was the first President of the United States?",
        "options": ["George Washington", "John Adams", "Thomas Jefferson", "James Madison"],
        "answer": "George Washington"
    },
    {
        "question": "Who was the principal author of the Declaration of Independence and later became president?",
        "options": ["John Adams", "Thomas Jefferson", "James Monroe", "Benjamin Franklin"],
        "answer": "Thomas Jefferson"
    },
    {
        "question": "Which U.S. President led the Union during the Civil War?",
        "options": ["Ulysses S. Grant", "Andrew Johnson", "Abraham Lincoln", "James Buchanan"],
        "answer": "Abraham Lincoln"
    },
    {
        "question": "Who was the only U.S. President to serve more than two terms?",
        "options": ["Teddy Roosevelt", "Woodrow Wilson", "Franklin D. Roosevelt", "Dwight D. Eisenhower"],
        "answer": "Franklin D. Roosevelt"
    },
    {
        "question": "Who was elected President in 1980?",
        "options": ["Jimmy Carter", "Ronald Reagan", "Gerald Ford", "Richard Nixon"],
        "answer": "Ronald Reagan"
    }
]

class PresidentQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("U.S. Presidents Quiz (1776–1980)")
        self.root.geometry("500x300")
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=480, font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options_var, value="", font=("Helvetica", 12))
            rb.pack(anchor="w")
            self.options.append(rb)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 12))
        self.submit_btn.pack(pady=20)

        self.show_question()

    def show_question(self):
        q = questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
        self.options_var.set(None)
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def check_answer(self):
        selected = self.options_var.get()
        if not selected:
            messagebox.showwarning("No answer", "Please select an answer.")
            return
        if selected == questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        result = f"You scored {self.score} out of {len(questions)}.\n"
        if self.score == 5:
            result += "🏆 Excellent! You're a presidential expert!"
        elif self.score >= 3:
            result += "✅ Good job! You know your history."
        else:
            result += "📚 Keep studying—history is important!"
        messagebox.showinfo("Quiz Complete", result)
        self.root.quit()

# Run the quiz
if __name__ == "__main__":
    root = tk.Tk()
    app = PresidentQuizApp(root)
    root.mainloop()
