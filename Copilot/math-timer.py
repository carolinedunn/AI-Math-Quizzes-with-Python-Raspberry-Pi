import tkinter as tk
import random

class MathQuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz with Timer")
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="Time left: 10s", font=("Helvetica", 14))
        self.timer_label.pack()

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.feedback_label.pack()

        self.score_label = tk.Label(root, text="Score: 0/5", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.questions_asked = 0
        self.score = 0
        self.time_left = 10
        self.timer_running = False

        self.ask_question()

    def ask_question(self):
        self.num1 = random.randint(1, 20)
        self.num2 = random.randint(1, 20)
        self.operation = random.choice(['+', '-'])

        if self.operation == '-' and self.num2 > self.num1:
            self.num1, self.num2 = self.num2, self.num1

        self.correct_answer = self.num1 + self.num2 if self.operation == '+' else self.num1 - self.num2
        self.question_label.config(text=f"Q{self.questions_asked + 1}: What is {self.num1} {self.operation} {self.num2}?")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.time_left = 10
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        self.timer_running = True
        self.countdown()

    def countdown(self):
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.countdown)
        elif self.timer_running:
            self.feedback_label.config(text=f"⏰ Time's up! Answer: {self.correct_answer}", fg="red")
            self.timer_running = False
            self.questions_asked += 1
            self.score_label.config(text=f"Score: {self.score}/5")
            if self.questions_asked < 5:
                self.root.after(1500, self.ask_question)
            else:
                self.end_quiz()

    def check_answer(self):
        if not self.timer_running:
            return

        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.score += 1
                self.feedback_label.config(text="✅ Correct!", fg="green")
            else:
                self.feedback_label.config(text=f"❌ Incorrect! Answer: {self.correct_answer}", fg="red")
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a number.", fg="orange")

        self.timer_running = False
        self.questions_asked += 1
        self.score_label.config(text=f"Score: {self.score}/5")
        if self.questions_asked < 5:
            self.root.after(1500, self.ask_question)
        else:
            self.end_quiz()

    def end_quiz(self):
        self.question_label.config(text="🏁 Quiz Complete!")
        self.answer_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.timer_label.config(text="")
        self.feedback_label.config(text=f"Final Score: {self.score}/5 🎉", fg="blue")

# Start the quiz
root = tk.Tk()
quiz_app = MathQuizGUI(root)
root.mainloop()
