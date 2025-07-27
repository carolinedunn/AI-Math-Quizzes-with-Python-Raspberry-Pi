import tkinter as tk
from tkinter import messagebox
import random

# Full 20-question bank
full_questions = [
    {"question": "Who was the first President of the United States?",
     "options": ["George Washington", "John Adams", "Thomas Jefferson", "James Madison"],
     "answer": "George Washington"},
    {"question": "Who was the principal author of the Declaration of Independence?",
     "options": ["Thomas Jefferson", "John Adams", "James Madison", "Alexander Hamilton"],
     "answer": "Thomas Jefferson"},
    {"question": "Which president purchased the Louisiana Territory?",
     "options": ["James Monroe", "Thomas Jefferson", "Andrew Jackson", "John Quincy Adams"],
     "answer": "Thomas Jefferson"},
    {"question": "Which president led the Union during the Civil War?",
     "options": ["Andrew Johnson", "Abraham Lincoln", "Ulysses S. Grant", "James Buchanan"],
     "answer": "Abraham Lincoln"},
    {"question": "Which president signed the Emancipation Proclamation?",
     "options": ["Abraham Lincoln", "Andrew Jackson", "James K. Polk", "Zachary Taylor"],
     "answer": "Abraham Lincoln"},
    {"question": "Who was the only president to serve more than two terms?",
     "options": ["Teddy Roosevelt", "Franklin D. Roosevelt", "Woodrow Wilson", "Dwight D. Eisenhower"],
     "answer": "Franklin D. Roosevelt"},
    {"question": "Who was president during World War I?",
     "options": ["Herbert Hoover", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge"],
     "answer": "Woodrow Wilson"},
    {"question": "Who was president at the start of the Great Depression?",
     "options": ["Herbert Hoover", "Franklin D. Roosevelt", "Harry Truman", "Warren G. Harding"],
     "answer": "Herbert Hoover"},
    {"question": "Who dropped the atomic bomb to end WWII?",
     "options": ["Franklin D. Roosevelt", "Harry S. Truman", "Dwight Eisenhower", "John F. Kennedy"],
     "answer": "Harry S. Truman"},
    {"question": "Which president desegregated the U.S. military?",
     "options": ["Harry Truman", "Dwight D. Eisenhower", "Lyndon B. Johnson", "John F. Kennedy"],
     "answer": "Harry Truman"},
    {"question": "Who led the U.S. in the 1950s during the Cold War and the Interstate Highway expansion?",
     "options": ["Dwight D. Eisenhower", "Harry Truman", "John F. Kennedy", "Lyndon B. Johnson"],
     "answer": "Dwight D. Eisenhower"},
    {"question": "Who was assassinated in 1963 in Dallas, Texas?",
     "options": ["John F. Kennedy", "Lyndon B. Johnson", "Robert Kennedy", "Richard Nixon"],
     "answer": "John F. Kennedy"},
    {"question": "Which president signed the Civil Rights Act of 1964?",
     "options": ["John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon", "Jimmy Carter"],
     "answer": "Lyndon B. Johnson"},
    {"question": "Who resigned due to the Watergate scandal?",
     "options": ["Gerald Ford", "Richard Nixon", "Lyndon B. Johnson", "Jimmy Carter"],
     "answer": "Richard Nixon"},
    {"question": "Who became president after Nixon resigned?",
     "options": ["Ronald Reagan", "Jimmy Carter", "Gerald Ford", "Walter Mondale"],
     "answer": "Gerald Ford"},
    {"question": "Who was president during the Iran hostage crisis?",
     "options": ["Jimmy Carter", "Ronald Reagan", "Gerald Ford", "Richard Nixon"],
     "answer": "Jimmy Carter"},
    {"question": "Who won the election of 1980?",
     "options": ["Jimmy Carter", "Ronald Reagan", "George H.W. Bush", "Walter Mondale"],
     "answer": "Ronald Reagan"},
    {"question": "Who was president during the Mexican-American War?",
     "options": ["James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce"],
     "answer": "James K. Polk"},
    {"question": "Which president delivered the Gettysburg Address?",
     "options": ["Abraham Lincoln", "Ulysses S. Grant", "Andrew Johnson", "James Buchanan"],
     "answer": "Abraham Lincoln"},
    {"question": "Which president was a famous general in WWII before taking office?",
     "options": ["Harry Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon Johnson"],
     "answer": "Dwight D. Eisenhower"},
]

class PresidentQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("U.S. Presidents Quiz (1776–1980)")
        self.root.geometry("600x400")
        self.score = 0
        self.current_question = 0
        self.timer_seconds = 10
        self.timer_running = False

        # Pick 5 random questions from the pool
        self.questions = random.sample(full_questions, 5)

        self.question_label = tk.Label(root, text="", wraplength=560, font=("Helvetica", 16), justify="left")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options_var, value="", font=("Helvetica", 14))
            rb.pack(anchor="w", padx=30)
            self.options.append(rb)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
        self.timer_label.pack(pady=10)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_btn.pack(pady=20)

        self.show_question()

    def show_question(self):
        q = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
        self.options_var.set(None)
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)
        self.start_timer()

    def start_timer(self):
        self.timer_seconds = 10
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_seconds > 0 and self.timer_running:
            self.timer_label.config(text=f"Time left: {self.timer_seconds} seconds")
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        elif self.timer_running:
            self.timer_running = False
            self.timer_label.config(text="⏰ Time's up!")
            self.next_question()

    def check_answer(self):
        if not self.timer_running:
            return
        selected = self.options_var.get()
        self.timer_running = False
        if selected == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        result = f"You scored {self.score} out of {len(self.questions)}.\n"
        if self.score == 5:
            result += "🏆 Perfect score!"
        elif self.score >= 3:
            result += "🎉 Great job!"
        else:
            result += "📚 Keep studying history."
        messagebox.showinfo("Quiz Complete", result)
        self.root.quit()

# Run the quiz
if __name__ == "__main__":
    root = tk.Tk()
    app = PresidentQuizApp(root)
    root.mainloop()
