import random

def generate_expression():
    # Generate expressions using PEMDAS operators
    operations = ['+', '-', '*', '/']
    expr = ""
    for _ in range(3):  # create a 4-part expression with 3 operations
        num = random.randint(1, 10)
        op = random.choice(operations)
        expr += f"{num} {op} "
    expr += str(random.randint(1, 10))  # final number
    return expr

def main():
    score = 0
    print("Welcome to the PEMDAS Quiz! Solve the following 5 expressions:")
    print("Use correct order of operations (PEMDAS).\n")

    for i in range(1, 6):
        expr = generate_expression()
        try:
            correct_answer = eval(expr)
        except ZeroDivisionError:
            continue  # skip this expression if it contains division by zero

        print(f"Question {i}: What is the result of {expr}?")
        try:
            user_answer = float(input("Your answer: "))
        except ValueError:
            print("Invalid input. Moving to next question.")
            continue

        if abs(user_answer - correct_answer) < 0.01:  # allow small margin of error
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer:.2f}\n")

    print(f"Quiz complete! Your score: {score} out of 5.")

if __name__ == "__main__":
    main()
