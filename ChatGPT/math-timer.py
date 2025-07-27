import tkinter as tk
from tkinter import messagebox
import random

class PEMDASQuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PEMDAS Quiz")
        self.score = 0
        self.question_number = 0
        self.total_questions = 5
        self.timer_seconds = 10
        self.timer_id = None

        self.question_label = tk.Label(root, text="Welcome to the PEMDAS Quiz!", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 14), fg="red")
        self.timer_label.pack(pady=5)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=10)

        self.generate_next_question()

    def generate_expression(self):
        operations = ['+', '-', '*', '/']
        expr = ""
        for _ in range(3):
            num = random.randint(1, 10)
            op = random.choice(operations)
            expr += f"{num} {op} "
        expr += str(random.randint(1, 10))
        return expr

    def generate_next_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        if self.question_number >= self.total_questions:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {self.total_questions}.")
            self.root.quit()
            return

        self.current_expr = self.generate_expression()
        try:
            self.correct_answer = eval(self.current_expr)
        except ZeroDivisionError:
            self.generate_next_question()
            return

        self.question_number += 1
        self.timer_seconds = 20
        self.update_timer()

        self.question_label.config(text=f"Question {self.question_number}: What is {self.current_expr}?")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds} seconds")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text=f"Time's up! The correct answer was {self.correct_answer:.2f}")
            self.root.after(1500, self.generate_next_question)

    def check_answer(self):
        if self.timer_seconds <= 0:
            return

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        try:
            user_answer = float(self.answer_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")
            return

        if abs(user_answer - self.correct_answer) < 0.01:
            self.feedback_label.config(text="Correct!")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer was {self.correct_answer:.2f}")

        self.root.after(1500, self.generate_next_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = PEMDASQuizGUI(root)
    root.mainloop()
