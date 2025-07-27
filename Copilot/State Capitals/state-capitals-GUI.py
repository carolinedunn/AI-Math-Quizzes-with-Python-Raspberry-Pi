import tkinter as tk
import random

# Dictionary of U.S. states and capitals
state_capitals = {
    "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
    "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
    "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
    "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
    "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
    "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul", "Mississippi": "Jackson",
    "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
    "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
    "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City",
    "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
    "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City",
    "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston",
    "Wisconsin": "Madison", "Wyoming": "Cheyenne"
}

class StateCapitalQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("State Capitals Quiz")
        self.score = 0
        self.question_count = 0
        self.max_questions = 5
        self.states = list(state_capitals.keys())

        self.question_label = tk.Label(root, text="What is the capital of...", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack(pady=5)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_btn.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_count < self.max_questions:
            self.current_state = random.choice(self.states)
            self.question_label.config(text=f"What is the capital of {self.current_state}?")
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = state_capitals[self.current_state].lower()

        if user_answer == correct_answer:
            self.feedback_label.config(text="Correct!")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong. It's {state_capitals[self.current_state]}.")

        self.question_count += 1
        self.root.after(1000, self.next_question)

    def end_quiz(self):
        self.question_label.config(text="Quiz Complete!")
        self.answer_entry.pack_forget()
        self.submit_btn.pack_forget()
        self.feedback_label.pack_forget()
        self.score_label.config(text=f"You scored {self.score} out of {self.max_questions}.")

root = tk.Tk()
quiz_app = StateCapitalQuiz(root)
root.mainloop()
