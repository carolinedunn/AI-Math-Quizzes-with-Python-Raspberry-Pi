import random

# Dictionary of states and their capitals
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    # Add more states if you'd like!
}

def quiz(num_questions=5):
    print("🌟 Welcome to the State Capitals Quiz! 🌟")
    states = list(state_capitals.keys())
    score = 0

    for _ in range(num_questions):
        state = random.choice(states)
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == state_capitals[state].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Nope! The capital is {state_capitals[state]}.\n")

    print(f"🎉 You got {score} out of {num_questions} correct!")

quiz()
