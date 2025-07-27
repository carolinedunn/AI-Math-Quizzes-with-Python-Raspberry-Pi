import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-'])

    if operation == '+':
        correct_answer = num1 + num2
    else:
        # Ensure subtraction doesn't result in negative numbers
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2

    return f"What is {num1} {operation} {num2}?", correct_answer

def math_quiz():
    score = 0
    print("🔢 Welcome to the Math Quiz! Let's test your addition and subtraction skills.\n")

    for i in range(1, 6):
        question, answer = generate_question()
        print(f"Question {i}: {question}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Nope, the correct answer was {answer}.\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    print(f"🏁 Quiz complete! You scored {score} out of 5.\n")

math_quiz()
