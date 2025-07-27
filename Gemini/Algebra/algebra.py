import random

def run_quiz():
    """
    Runs a basic algebra quiz game with 5 questions.
    """
    score = 0
    questions = []

    # Generate 5 unique algebra questions
    for i in range(5):
        operation = random.choice(['+', '-', '*'])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        # Ensure division results in an integer if 'x' is on the left
        if operation == '/':
            # Make sure num1 is a multiple of num2 for clean division
            num1 = num2 * random.randint(1, 5)
            # Choose to place 'x' in different positions
            if random.random() < 0.5: # x is the result
                question_text = f"What is {num1} / {num2}?"
                correct_answer = num1 / num2
            else: # x is the divisor or dividend
                if random.random() < 0.5: # x is the divisor
                    question_text = f"{num1} / x = {num1 // num2}. What is x?"
                    correct_answer = num2
                else: # x is the dividend (not directly covered by num1 / x, needs more complex setup)
                    # For simplicity, let's stick to x = result or x = divisor for division for now
                    # Or just generate different questions if division gets too complex for 'basic'
                    question_text = f"What is {num1} / {num2}?"
                    correct_answer = num1 / num2

        elif operation == '+':
            # Randomly decide where 'x' goes in the equation
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
            # Randomly decide where 'x' goes in the equation
            if random.random() < 0.33: # x - num2 = result
                result = num1 - num2
                question_text = f"x - {num2} = {result}. What is x?"
                correct_answer = num1
            elif random.random() < 0.66: # num1 - x = result
                # Ensure result is positive for cleaner problems
                if num1 < num2: # Swap if num1 is smaller to avoid negative results for num1 - x
                    num1, num2 = num2, num1
                result = num1 - num2
                question_text = f"{num1} - x = {result}. What is x?"
                correct_answer = num2
            else: # x = num1 - num2
                question_text = f"What is {num1} - {num2}?"
                correct_answer = num1 - num2

        elif operation == '*':
            # Randomly decide where 'x' goes in the equation
            if random.random() < 0.33: # x * num2 = result
                result = num1 * num2
                question_text = f"x * {num2} = {result}. What is x?"
                correct_answer = num1
            elif random.random() < 0.66: # num1 * x = result
                result = num1 * num2
                question_text = f"{num1} * x = {result}. What is x?"
                correct_answer = num2
            else: # x = num1 * num2
                question_text = f"What is {num1} * {num2}?"
                correct_answer = num1 * num2

        questions.append({"question": question_text, "answer": correct_answer})

    print("Welcome to the Basic Algebra Quiz!")
    print("Let's get started. Please enter whole numbers for your answers.")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        try:
            user_answer = float(input("Your answer: ")) # Use float to handle division results
            # For simplicity in basic algebra, convert correct_answer to int if it's a whole number
            # and compare with user_answer as int if possible.
            # Otherwise, direct float comparison is fine for basic checks.
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
