import tkinter as tk
from tkinter import messagebox
import random

class AlgebraQuizApp:
    """
    A GUI-based algebra quiz game focusing on addition and subtraction.
    """
    def __init__(self, master):
        self.master = master
        master.title("Basic Algebra Quiz")
        master.geometry("400x300") # Set initial window size
        master.resizable(False, False) # Make window non-resizable for simplicity

        self.questions = []
        self.score = 0
        self.current_question_index = 0

        # Configure styles for better appearance (optional but good practice)
        master.configure(bg="#e0f2f7") # Light blue background
        master.option_add('*Font', 'Inter 12') # Set default font
        master.option_add('*Button.activeBackground', '#b3e0ff') # Light blue on hover

        # --- GUI Elements ---

        # Welcome/Instructions Label
        self.instruction_label = tk.Label(master, text="Welcome to the Basic Algebra Quiz!\nFocus: Addition and Subtraction",
                                         bg="#e0f2f7", fg="#004d40", wraplength=350)
        self.instruction_label.pack(pady=10)

        # Question Label
        self.question_label = tk.Label(master, text="Click 'Start Quiz' to begin!",
                                       bg="#e0f2f7", fg="#333333", font="Inter 14 bold")
        self.question_label.pack(pady=10)

        # Entry for user answer
        self.answer_entry = tk.Entry(master, width=20, justify='center', bd=2, relief="groove")
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer_event) # Allow Enter key to submit

        # Submit Button
        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer,
                                       bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised", bd=2,
                                       activebackground="#45a049", cursor="hand2")
        self.submit_button.pack(pady=5)

        # Feedback Label (Correct/Incorrect)
        self.feedback_label = tk.Label(master, text="", bg="#e0f2f7", fg="#d32f2f")
        self.feedback_label.pack(pady=5)

        # Score Label
        self.score_label = tk.Label(master, text="Score: 0/0", bg="#e0f2f7", fg="#333333")
        self.score_label.pack(pady=5)

        # Start/Restart Quiz Button
        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz,
                                       bg="#2196F3", fg="white", padx=10, pady=5, relief="raised", bd=2,
                                       activebackground="#1976D2", cursor="hand2")
        self.start_button.pack(pady=10)

        # Initially disable answer input and submit button
        self.answer_entry.config(state='disabled')
        self.submit_button.config(state='disabled')

    def generate_questions(self, num_questions=5):
        """
        Generates a list of basic algebra questions (addition and subtraction).
        """
        self.questions = []
        for _ in range(num_questions):
            operation = random.choice(['+', '-'])
            num1 = random.randint(1, 15) # Increased range for numbers
            num2 = random.randint(1, 15)

            if operation == '+':
                if random.random() < 0.33: # x + num2 = result
                    result = num1 + num2
                    question_text = f"x + {num2} = {result}. What is x?"
                    correct_answer = num1
                elif random.random() < 0.66: # num1 + x = result
                    result = num1 + num2
                    question_text = f"{num1} + x = {result}. What is x?"
                    correct_answer = num2
                else: # x = num1 + num2
                    question_text = f"What is {num1} + {num2}?"
                    correct_answer = num1 + num2

            elif operation == '-':
                if random.random() < 0.33: # x - num2 = result
                    result = num1 - num2
                    question_text = f"x - {num2} = {result}. What is x?"
                    correct_answer = num1
                elif random.random() < 0.66: # num1 - x = result
                    # Ensure num1 is larger than num2 for positive result if x is subtracted
                    if num1 < num2:
                        num1, num2 = num2, num1
                    result = num1 - num2
                    question_text = f"{num1} - x = {result}. What is x?"
                    correct_answer = num2
                else: # x = num1 - num2
                    question_text = f"What is {num1} - {num2}?"
                    correct_answer = num1 - num2

            self.questions.append({"question": question_text, "answer": correct_answer})

    def start_quiz(self):
        """
        Resets the quiz state and starts a new quiz.
        """
        self.score = 0
        self.current_question_index = 0
        self.generate_questions() # Regenerate questions for a new game
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END) # Clear previous answer
        self.answer_entry.config(state='normal') # Enable input
        self.submit_button.config(state='normal') # Enable submit button
        self.start_button.config(text="Restart Quiz") # Change button text
        self.display_question()

    def display_question(self):
        """
        Displays the current question.
        """
        if self.current_question_index < len(self.questions):
            q_data = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question {self.current_question_index + 1}: {q_data['question']}")
            self.answer_entry.delete(0, tk.END) # Clear entry for new question
            self.answer_entry.focus_set() # Set focus to the entry field
        else:
            self.end_quiz()

    def check_answer_event(self, event=None):
        """
        Event handler for pressing Enter key in the answer entry.
        """
        self.check_answer()

    def check_answer(self):
        """
        Checks the user's answer and updates the score.
        """
        try:
            user_answer_str = self.answer_entry.get().strip()
            if not user_answer_str:
                messagebox.showwarning("Input Error", "Please enter an answer.")
                return

            user_answer = float(user_answer_str)
            correct_answer = self.questions[self.current_question_index]['answer']

            # Compare integer values for basic algebra problems
            if user_answer == int(user_answer) and correct_answer == int(correct_answer):
                if int(user_answer) == int(correct_answer):
                    self.feedback_label.config(text="Correct!", fg="#2e7d32") # Dark green
                    self.score += 1
                else:
                    self.feedback_label.config(text=f"Incorrect. Correct: {int(correct_answer)}", fg="#d32f2f") # Dark red
            else: # Fallback for float comparison if needed (e.g., if division was added later)
                if user_answer == correct_answer:
                    self.feedback_label.config(text="Correct!", fg="#2e7d32")
                    self.score += 1
                else:
                    self.feedback_label.config(text=f"Incorrect. Correct: {correct_answer}", fg="#d32f2f")

            self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
            self.current_question_index += 1
            self.master.after(1000, self.display_question) # Display next question after 1 second
            self.answer_entry.delete(0, tk.END) # Clear entry immediately after checking

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
        except IndexError:
            # This can happen if check_answer is called when quiz is already ended
            pass

    def end_quiz(self):
        """
        Ends the quiz and displays the final score.
        """
        self.question_label.config(text="Quiz Complete!")
        self.feedback_label.config(text="") # Clear feedback
        self.answer_entry.config(state='disabled') # Disable input
        self.submit_button.config(state='disabled') # Disable submit button

        final_message = f"You scored {self.score} out of {len(self.questions)}.\n"
        if self.score == len(self.questions):
            final_message += "Excellent work! You got all of them right!"
        elif self.score >= len(self.questions) / 2:
            final_message += "Good job! Keep practicing!"
        else:
            final_message += "Keep practicing, you'll get there!"

        messagebox.showinfo("Quiz Results", final_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = AlgebraQuizApp(root)
    root.mainloop()
