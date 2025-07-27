import random

def get_capitals_data():
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

def normalize_answer(answer):
    """
    Normalizes a user's answer for easier comparison (lowercase, stripped).
    """
    return answer.strip().lower()

def run_quiz():
    """
    Runs the main quiz game.
    """
    capitals = get_capitals_data()
    all_countries = list(capitals.keys())

    # Ensure we have enough countries for the quiz (at least 50 if possible)
    if len(all_countries) < 50:
        print("Warning: Not enough unique countries in the database for 50 questions.")
        num_questions_total = len(all_countries)
    else:
        num_questions_total = 50

    print("Welcome to the World Capitals Quiz!")
    print(f"You'll be tested on {num_questions_total} country capitals.")
    print("Let's begin!\n")

    play_again = "yes"
    while play_again.lower() == "yes":
        random.shuffle(all_countries) # Shuffle for new order each game
        countries_for_quiz = all_countries[:num_questions_total]
        score = 0
        total_questions_answered = 0

        for i, country in enumerate(countries_for_quiz):
            correct_capital = capitals[country]
            question_number_in_round = (total_questions_answered % 5) + 1

            # Ask the question
            user_answer = input(f"Question {total_questions_answered + 1}: What is the capital of {country}? ")

            # Check the answer
            if normalize_answer(user_answer) == normalize_answer(correct_capital):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The capital of {country} is {correct_capital}.")

            total_questions_answered += 1

            # Score after every 5 questions
            if total_questions_answered % 5 == 0:
                print(f"\n--- Round Score ---")
                print(f"You've answered 5 questions in this round.")
                # Calculate score for the current 5-question segment
                round_score = score - (total_questions_answered - 5)
                if total_questions_answered == 5: # First round
                    round_score = score
                print(f"Your score for the last 5 questions: {round_score}/5")
                print(f"Your overall score so far: {score}/{total_questions_answered}")
                print("-------------------\n")

        print("\n--- Quiz Finished! ---")
        print(f"You answered {total_questions_answered} questions.")
        print(f"Your final score is: {score}/{total_questions_answered}")
        print("---------------------\n")

        play_again = input("Do you want to play again? (yes/no): ")
        print()

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    run_quiz()
