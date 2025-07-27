import random

def run_quiz():
    """
    Runs a basic algebra quiz game with 5 questions, focusing on addition and subtraction.
    """
    score = 0
    questions = []

    # Generate 5 unique algebra questions
    for i in range(5):
        # Only include addition and subtraction operations
        operation = random.choice(['+', '-'])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if operation == '+':
            # Randomly decide where 'x' goes in the equation
            if random.random() < 0.33: # x + num2 = result
                result = num1 + num2
                question_text = f"x + {num2} = {result}. What is x?"
                correct_answer = num1
            elif random.random() < 0.66: # num1 + x = result
                result = num1 + num2
                question_text = f"{num1} + x = {result}. What is x?"
                correct_answer = num2
            else: # x = num1 + num2 (direct calculation)
                question_text = f"What is {num1} + {num2}?"
                correct_answer = num1 + num2

        elif operation == '-':
            # Randomly decide where 'x' goes in the equation
            if random.random() < 0.33: # x - num2 = result
                result = num1 - num2
                question_text = f"x - {num2} = {result}. What is x?"
                correct_answer = num1
            elif random.random() < 0.66: # num1 - x = result
                # Ensure result is positive for cleaner problems when x is subtracted
                if num1 < num2: # Swap if num1 is smaller to avoid negative results for num1 - x
                    num1, num2 = num2, num1
                result = num1 - num2
                question_text = f"{num1} - x = {result}. What is x?"
                correct_answer = num2
            else: # x = num1 - num2 (direct calculation)
                question_text = f"What is {num1} - {num2}?"
                correct_answer = num1 - num2

        questions.append({"question": question_text, "answer": correct_answer})

    print("Welcome to the Basic Algebra Quiz!")
    print("This quiz focuses on addition and subtraction.")
    print("Let's get started. Please enter whole numbers for your answers.")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        try:
            user_answer = float(input("Your answer: ")) # Use float to handle any potential non-integer answers if needed later
            # For basic algebra, we expect whole numbers as answers.
            # Convert both to int for comparison if they are whole numbers to avoid float comparison issues.
            if user_answer == int(user_answer) and q['answer'] == int(q['answer']):
                if int(user_answer) == int(q['answer']):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer was {int(q['answer'])}.")
            else: # If answers are floats (e.g., from future division problems), compare directly
                if user_answer == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer was {q['answer']}.")

        except ValueError:
            print("Invalid input. Please enter a number.")
            print(f"The correct answer was {q['answer']}.") # Still show correct answer

    print(f"\n--- Quiz Complete! ---")
    print(f"You scored {score} out of {len(questions)}.")
    if score == len(questions):
        print("Excellent work! You got all of them right!")
    elif score >= len(questions) / 2:
        print("Good job! Keep practicing!")
    else:
        print("Keep practicing, you'll get there!")

if __name__ == "__main__":
    run_quiz()
