import tkinter as tk
from tkinter import messagebox
import random

class WorldCapitalsQuiz:
    def __init__(self, master):
        self.master = master
        master.title("World Capitals Quiz")
        master.geometry("500x350") # Set a fixed window size
        master.resizable(False, False) # Make window non-resizable
        master.configure(bg="#e0f7fa") # Light blue background

        self.capitals_data = self.get_capitals_data()
        self.all_countries = list(self.capitals_data.keys())
        self.num_questions_per_game = 5 # Game now stops after 5 questions

        self.current_question_index = 0
        self.score = 0
        self.current_quiz_countries = []

        # Styling
        label_font = ("Arial", 14)
        button_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)

        # Welcome message
        self.welcome_label = tk.Label(master, text="Welcome to the World Capitals Quiz!", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#004d40")
        self.welcome_label.pack(pady=10)

        # Question label
        self.question_label = tk.Label(master, text="", font=label_font, bg="#e0f7fa", fg="#263238", wraplength=450)
        self.question_label.pack(pady=10)

        # Entry for user answer
        self.answer_entry = tk.Entry(master, font=entry_font, width=30, bd=2, relief="groove")
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer()) # Allow pressing Enter

        # Submit button
        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer, font=button_font, bg="#4CAF50", fg="white", activebackground="#66BB6A", activeforeground="white", relief="raised", bd=3, padx=10, pady=5)
        self.submit_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(master, text="", font=label_font, bg="#e0f7fa", fg="#d32f2f")
        self.feedback_label.pack(pady=5)

        # Score label
        self.score_label = tk.Label(master, text="Score: 0/0", font=label_font, bg="#e0f7fa", fg="#388E3C")
        self.score_label.pack(pady=10)

        self.start_new_game()

    def get_capitals_data(self):
        """
        Returns a dictionary of countries and their capitals.
        This data is hardcoded for simplicity, representing a selection of
        countries from various continents.
        """
        return {
            "Afghanistan": "Kabul", "Albania": "Tirana", "Algeria": "Algiers",
            "Angola": "Luanda", "Argentina": "Buenos Aires", "Australia": "Canberra",
            "Austria": "Vienna", "Bangladesh": "Dhaka", "Belgium": "Brussels",
            "Brazil": "Brasilia", "Canada": "Ottawa", "Chile": "Santiago",
            "China": "Beijing", "Colombia": "Bogota", "Cuba": "Havana",
            "Denmark": "Copenhagen", "Egypt": "Cairo", "Ethiopia": "Addis Ababa",
            "Finland": "Helsinki", "France": "Paris", "Germany": "Berlin",
            "Ghana": "Accra", "Greece": "Athens", "Hungary": "Budapest",
            "India": "New Delhi", "Indonesia": "Jakarta", "Iran": "Tehran",
            "Iraq": "Baghdad", "Ireland": "Dublin", "Israel": "Jerusalem",
            "Italy": "Rome", "Japan": "Tokyo", "Kenya": "Nairobi",
            "Mexico": "Mexico City", "Morocco": "Rabat", "Netherlands": "Amsterdam",
            "New Zealand": "Wellington", "Nigeria": "Abuja", "Norway": "Oslo",
            "Pakistan": "Islamabad", "Peru": "Lima", "Philippines": "Manila",
            "Poland": "Warsaw", "Portugal": "Lisbon", "Russia": "Moscow",
            "Saudi Arabia": "Riyadh", "South Africa": "Pretoria", "South Korea": "Seoul",
            "Spain": "Madrid", "Sweden": "Stockholm", "Switzerland": "Bern",
            "Thailand": "Bangkok", "Turkey": "Ankara", "Ukraine": "Kyiv",
            "United Kingdom": "London", "United States": "Washington D.C.",
            "Uruguay": "Montevideo", "Venezuela": "Caracas", "Vietnam": "Hanoi"
        }

    def normalize_answer(self, answer):
        """
        Normalizes a user's answer for easier comparison (lowercase, stripped).
        """
        return answer.strip().lower()

    def start_new_game(self):
        """
        Initializes a new game by resetting scores and shuffling questions.
        """
        self.current_question_index = 0
        self.score = 0
        random.shuffle(self.all_countries)
        # Select the first N questions for this game
        self.current_quiz_countries = self.all_countries[:self.num_questions_per_game]
        self.update_score_display()
        self.ask_question()
        self.submit_button.config(state=tk.NORMAL) # Enable submit button
        self.answer_entry.config(state=tk.NORMAL) # Enable entry
        self.feedback_label.config(text="") # Clear previous feedback

    def ask_question(self):
        """
        Displays the current question.
        """
        if self.current_question_index < self.num_questions_per_game:
            country = self.current_quiz_countries[self.current_question_index]
            self.question_label.config(text=f"Question {self.current_question_index + 1}: What is the capital of {country}?")
            self.answer_entry.delete(0, tk.END) # Clear the entry field
            self.feedback_label.config(fg="black", text="Type your answer above.") # Reset feedback text
        else:
            self.end_game()

    def check_answer(self):
        """
        Checks the user's answer and updates the score.
        """
        if self.current_question_index >= self.num_questions_per_game:
            return # Prevent checking answers after the game ends

        user_answer = self.answer_entry.get()
        country = self.current_quiz_countries[self.current_question_index]
        correct_capital = self.capitals_data[country]

        if self.normalize_answer(user_answer) == self.normalize_answer(correct_capital):
            self.feedback_label.config(fg="#388E3C", text="Correct!")
            self.score += 1
        else:
            self.feedback_label.config(fg="#D32F2F", text=f"Incorrect. The capital is {correct_capital}.")

        self.update_score_display()
        self.current_question_index += 1
        self.master.after(1500, self.ask_question) # Wait 1.5 seconds before next question

    def update_score_display(self):
        """
        Updates the score label.
        """
        self.score_label.config(text=f"Score: {self.score}/{self.current_question_index}")

    def end_game(self):
        """
        Ends the game and displays the final score.
        """
        self.question_label.config(text="Quiz Finished!")
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.config(state=tk.DISABLED) # Disable entry field
        self.submit_button.config(state=tk.DISABLED) # Disable submit button

        final_message = f"Your final score is: {self.score}/{self.num_questions_per_game}\n\nDo you want to play again?"
        if messagebox.askyesno("Quiz Over!", final_message):
            self.start_new_game()
        else:
            self.master.destroy() # Close the window if user doesn't want to play again


if __name__ == "__main__":
    # Ensure there are at least 50 countries in the data for the warning to be relevant
    # The current data has more than 50 countries, so this warning is less critical here,
    # but good to keep if you ever shorten the data list.
    if len(WorldCapitalsQuiz(tk.Tk()).get_capitals_data()) < 50:
        print("Warning: The provided data has fewer than 50 countries, so fewer questions might be asked per full quiz cycle if `num_questions_total` was set to 50.")
        print("For this GUI version, the game is set to 5 questions, which is fine.")

    root = tk.Tk()
    app = WorldCapitalsQuiz(root)
    root.mainloop()
