import tkinter as tk
import random

# Complete data: state => capital + 3 other cities
state_data = {
    "Alabama": {"capital": "Montgomery", "cities": ["Birmingham", "Mobile", "Huntsville"]},
    "Alaska": {"capital": "Juneau", "cities": ["Anchorage", "Fairbanks", "Sitka"]},
    "Arizona": {"capital": "Phoenix", "cities": ["Tucson", "Mesa", "Flagstaff"]},
    "Arkansas": {"capital": "Little Rock", "cities": ["Fayetteville", "Fort Smith", "Jonesboro"]},
    "California": {"capital": "Sacramento", "cities": ["Los Angeles", "San Diego", "San Francisco"]},
    "Colorado": {"capital": "Denver", "cities": ["Boulder", "Colorado Springs", "Aurora"]},
    "Connecticut": {"capital": "Hartford", "cities": ["Bridgeport", "New Haven", "Stamford"]},
    "Delaware": {"capital": "Dover", "cities": ["Wilmington", "Newark", "Middletown"]},
    "Florida": {"capital": "Tallahassee", "cities": ["Miami", "Orlando", "Tampa"]},
    "Georgia": {"capital": "Atlanta", "cities": ["Savannah", "Augusta", "Macon"]},
    "Hawaii": {"capital": "Honolulu", "cities": ["Hilo", "Kailua", "Lahaina"]},
    "Idaho": {"capital": "Boise", "cities": ["Idaho Falls", "Twin Falls", "Pocatello"]},
    "Illinois": {"capital": "Springfield", "cities": ["Chicago", "Peoria", "Rockford"]},
    "Indiana": {"capital": "Indianapolis", "cities": ["Fort Wayne", "Evansville", "South Bend"]},
    "Iowa": {"capital": "Des Moines", "cities": ["Cedar Rapids", "Davenport", "Sioux City"]},
    "Kansas": {"capital": "Topeka", "cities": ["Wichita", "Overland Park", "Lawrence"]},
    "Kentucky": {"capital": "Frankfort", "cities": ["Louisville", "Lexington", "Bowling Green"]},
    "Louisiana": {"capital": "Baton Rouge", "cities": ["New Orleans", "Lafayette", "Shreveport"]},
    "Maine": {"capital": "Augusta", "cities": ["Portland", "Bangor", "Lewiston"]},
    "Maryland": {"capital": "Annapolis", "cities": ["Baltimore", "Frederick", "Rockville"]},
    "Massachusetts": {"capital": "Boston", "cities": ["Worcester", "Springfield", "Lowell"]},
    "Michigan": {"capital": "Lansing", "cities": ["Detroit", "Grand Rapids", "Ann Arbor"]},
    "Minnesota": {"capital": "St. Paul", "cities": ["Minneapolis", "Duluth", "Rochester"]},
    "Mississippi": {"capital": "Jackson", "cities": ["Biloxi", "Hattiesburg", "Tupelo"]},
    "Missouri": {"capital": "Jefferson City", "cities": ["St. Louis", "Kansas City", "Springfield"]},
    "Montana": {"capital": "Helena", "cities": ["Billings", "Bozeman", "Missoula"]},
    "Nebraska": {"capital": "Lincoln", "cities": ["Omaha", "Bellevue", "Kearney"]},
    "Nevada": {"capital": "Carson City", "cities": ["Las Vegas", "Reno", "Henderson"]},
    "New Hampshire": {"capital": "Concord", "cities": ["Manchester", "Nashua", "Portsmouth"]},
    "New Jersey": {"capital": "Trenton", "cities": ["Newark", "Jersey City", "Paterson"]},
    "New Mexico": {"capital": "Santa Fe", "cities": ["Albuquerque", "Las Cruces", "Roswell"]},
    "New York": {"capital": "Albany", "cities": ["New York City", "Buffalo", "Rochester"]},
    "North Carolina": {"capital": "Raleigh", "cities": ["Charlotte", "Durham", "Wilmington"]},
    "North Dakota": {"capital": "Bismarck", "cities": ["Fargo", "Grand Forks", "Minot"]},
    "Ohio": {"capital": "Columbus", "cities": ["Cleveland", "Cincinnati", "Toledo"]},
    "Oklahoma": {"capital": "Oklahoma City", "cities": ["Tulsa", "Norman", "Lawton"]},
    "Oregon": {"capital": "Salem", "cities": ["Portland", "Eugene", "Bend"]},
    "Pennsylvania": {"capital": "Harrisburg", "cities": ["Philadelphia", "Pittsburgh", "Allentown"]},
    "Rhode Island": {"capital": "Providence", "cities": ["Warwick", "Cranston", "Pawtucket"]},
    "South Carolina": {"capital": "Columbia", "cities": ["Charleston", "Greenville", "Spartanburg"]},
    "South Dakota": {"capital": "Pierre", "cities": ["Sioux Falls", "Rapid City", "Aberdeen"]},
    "Tennessee": {"capital": "Nashville", "cities": ["Memphis", "Knoxville", "Chattanooga"]},
    "Texas": {"capital": "Austin", "cities": ["Houston", "Dallas", "San Antonio"]},
    "Utah": {"capital": "Salt Lake City", "cities": ["Provo", "Ogden", "St. George"]},
    "Vermont": {"capital": "Montpelier", "cities": ["Burlington", "Barre", "St. Albans"]},
    "Virginia": {"capital": "Richmond", "cities": ["Virginia Beach", "Norfolk", "Roanoke"]},
    "Washington": {"capital": "Olympia", "cities": ["Seattle", "Spokane", "Tacoma"]},
    "West Virginia": {"capital": "Charleston", "cities": ["Morgantown", "Huntington", "Parkersburg"]},
    "Wisconsin": {"capital": "Madison", "cities": ["Milwaukee", "Green Bay", "Kenosha"]},
    "Wyoming": {"capital": "Cheyenne", "cities": ["Casper", "Laramie", "Gillette"]}
}


class MCStateCapitalQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("State Capitals: Multiple Choice")
        self.score = 0
        self.question_count = 0
        self.max_questions = 5
        self.states = list(state_data.keys())

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.buttons = []
        for _ in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), command=lambda b=_: self.check_answer(b))
            btn.pack(pady=3)
            self.buttons.append(btn)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_count < self.max_questions:
            self.current_state = random.choice(self.states)
            self.question_label.config(text=f"What is the capital of {self.current_state}?")
            self.correct = state_data[self.current_state]["capital"]
            wrong_answers = random.sample(state_data[self.current_state]["cities"], 3)
            choices = wrong_answers + [self.correct]
            random.shuffle(choices)

            for i, btn in enumerate(self.buttons):
                btn.config(text=choices[i])
        else:
            self.end_quiz()

    def check_answer(self, index):
        selected = self.buttons[index].cget("text")
        if selected == self.correct:
            self.feedback_label.config(text="Correct!")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong. It's {self.correct}.")
        self.question_count += 1
        self.root.after(1000, self.next_question)

    def end_quiz(self):
        self.question_label.config(text="Quiz Complete!")
        for btn in self.buttons:
            btn.pack_forget()
        self.feedback_label.pack_forget()
        self.score_label.config(text=f"You scored {self.score} out of {self.max_questions}.")

root = tk.Tk()
quiz_app = MCStateCapitalQuiz(root)
root.mainloop()
