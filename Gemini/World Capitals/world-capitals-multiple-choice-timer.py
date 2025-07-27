import tkinter as tk
from tkinter import messagebox
import random

class WorldCapitalsQuiz:
    def __init__(self, master):
        self.master = master
        master.title("World Capitals Quiz")
        master.geometry("600x450") # Increased window size for more content
        master.resizable(False, False)
        master.configure(bg="#e0f7fa")

        # Data for countries and capitals
        self.capitals_data = self.get_capitals_data()
        self.all_countries = list(self.capitals_data.keys())
        self.num_questions_per_game = 5 # Game still stops after 5 questions
        self.time_limit_per_question = 15 # Time in seconds for each question

        # Game state variables
        self.current_question_index = 0
        self.score = 0
        self.current_quiz_countries = []
        self.time_left = self.time_limit_per_question
        self.timer_id = None # To manage the after() calls for the timer

        # --- GUI Elements ---
        label_font = ("Arial", 14)
        button_font = ("Arial", 12, "bold")
        timer_font = ("Arial", 16, "bold")

        # Welcome message
        self.welcome_label = tk.Label(master, text="Welcome to the World Capitals Quiz!", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#004d40")
        self.welcome_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(master, text=f"Time: {self.time_limit_per_question}", font=timer_font, bg="#e0f7fa", fg="#c62828")
        self.timer_label.pack(pady=5)

        # Question label
        self.question_label = tk.Label(master, text="", font=label_font, bg="#e0f7fa", fg="#263238", wraplength=550)
        self.question_label.pack(pady=15)

        # Frame for answer buttons
        self.choices_frame = tk.Frame(master, bg="#e0f7fa")
        self.choices_frame.pack(pady=10)

        self.choice_buttons = []
        for i in range(4): # 4 multiple choice options
            btn = tk.Button(self.choices_frame, text="", font=button_font, bg="#2196F3", fg="white", activebackground="#64B5F6", activeforeground="white", relief="raised", bd=3, padx=20, pady=10, width=25)
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.choice_buttons.append(btn)

        # Feedback label
        self.feedback_label = tk.Label(master, text="", font=label_font, bg="#e0f7fa", fg="#d32f2f")
        self.feedback_label.pack(pady=5)

        # Score label
        self.score_label = tk.Label(master, text="Score: 0/0", font=label_font, bg="#e0f7fa", fg="#388E3C")
        self.score_label.pack(pady=10)

        # Start the first game
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
        Normalizes a string for easier comparison (lowercase, stripped).
        """
        if answer is None: # Handle case where timer runs out (no answer)
            return ""
        return answer.strip().lower()

    def start_new_game(self):
        """
        Initializes a new game by resetting scores, shuffling questions,
        and setting up the first question.
        """
        self.stop_timer() # Ensure any previous timer is stopped
        self.current_question_index = 0
        self.score = 0
        random.shuffle(self.all_countries)
        self.current_quiz_countries = self.all_countries[:self.num_questions_per_game]
        self.update_score_display()
        self.ask_question()
        self.enable_choice_buttons()
        self.feedback_label.config(text="") # Clear previous feedback

    def ask_question(self):
        """
        Displays the current question and its multiple-choice options.
        Starts the timer for the question.
        """
        self.stop_timer() # Stop the timer for the previous question

        if self.current_question_index < self.num_questions_per_game:
            country = self.current_quiz_countries[self.current_question_index]
            correct_capital = self.capitals_data[country]

            # Generate incorrect options
            incorrect_options = []
            while len(incorrect_options) < 3:
                random_country = random.choice(self.all_countries)
                random_capital = self.capitals_data[random_country]
                if random_capital != correct_capital and random_capital not in incorrect_options:
                    incorrect_options.append(random_capital)

            # Combine correct and incorrect, then shuffle
            options = [correct_capital] + incorrect_options
            random.shuffle(options)

            # Update question label
            self.question_label.config(text=f"Question {self.current_question_index + 1}: What is the capital of {country}?")

            # Update and enable choice buttons
            self.enable_choice_buttons()
            for i, btn in enumerate(self.choice_buttons):
                btn.config(text=options[i], command=lambda selected=options[i]: self.check_answer(selected))

            self.feedback_label.config(fg="black", text="Choose an option below.")
            self.start_timer() # Start timer for the new question
        else:
            self.end_game()

    def check_answer(self, selected_answer):
        """
        Checks the user's selected answer or handles a timeout.
        """
        self.stop_timer() # Stop the timer as an answer has been given or time ran out
        self.disable_choice_buttons() # Disable buttons immediately after answer

        country = self.current_quiz_countries[self.current_question_index]
        correct_capital = self.capitals_data[country]

        if self.normalize_answer(selected_answer) == self.normalize_answer(correct_capital):
            self.feedback_label.config(fg="#388E3C", text="Correct!")
            self.score += 1
        else:
            if selected_answer is None: # Indicates time out
                self.feedback_label.config(fg="#D32F2F", text=f"Time's up! The capital is {correct_capital}.")
            else:
                self.feedback_label.config(fg="#D32F2F", text=f"Incorrect. The capital is {correct_capital}.")

        self.update_score_display()
        self.current_question_index += 1
        # Wait 1.5 seconds before showing the next question or ending the game
        self.master.after(1500, self.ask_question)

    def start_timer(self):
        """
        Initializes and starts the countdown timer for the current question.
        """
        self.time_left = self.time_limit_per_question
        self.timer_label.config(text=f"Time: {self.time_left}")
        self.countdown() # Start the recursive countdown

    def countdown(self):
        """
        Decrements the timer and updates the timer label.
        If time runs out, automatically calls check_answer.
        """
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            # Schedule the next countdown call after 1 second
            self.timer_id = self.master.after(1000, self.countdown)
        else:
            # Time's up, automatically check the answer (pass None for no selection)
            self.check_answer(None)

    def stop_timer(self):
        """
        Cancels any active timer.
        """
        if self.timer_id is not None:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None

    def enable_choice_buttons(self):
        """Enables all choice buttons."""
        for btn in self.choice_buttons:
            btn.config(state=tk.NORMAL, bg="#2196F3") # Reset color if it changed

    def disable_choice_buttons(self):
        """Disables all choice buttons."""
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED, bg="#9E9E9E") # Grey out buttons

    def update_score_display(self):
        """
        Updates the score label to reflect current progress.
        """
        self.score_label.config(text=f"Score: {self.score}/{self.current_question_index}")

    def end_game(self):
        """
        Ends the game, displays the final score, and prompts to play again.
        """
        self.stop_timer() # Ensure timer is off
        self.question_label.config(text="Quiz Finished!")
        self.feedback_label.config(text="")
        self.disable_choice_buttons() # Ensure buttons are disabled

        final_message = f"Your final score is: {self.score}/{self.num_questions_per_game}\n\nDo you want to play again?"
        if messagebox.askyesno("Quiz Over!", final_message):
            self.start_new_game()
        else:
            self.master.destroy() # Close the window

# Main part of the script to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WorldCapitalsQuiz(root)
    root.mainloop()
