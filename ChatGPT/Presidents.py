def main():
    score = 0
    print("🇺🇸 Welcome to the U.S. Presidents Trivia Quiz! 🇺🇸")
    print("Answer the following 5 questions:\n")

    # Question 1
    answer = input("1. Who was the first President of the United States? ")
    if answer.strip().lower() == "george washington":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is George Washington.\n")

    # Question 2
    answer = input("2. Which U.S. President issued the Emancipation Proclamation? ")
    if answer.strip().lower() == "abraham lincoln":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is Abraham Lincoln.\n")

    # Question 3
    answer = input("3. Who was the only U.S. President to serve more than two terms? ")
    if answer.strip().lower() == "franklin d. roosevelt" or answer.strip().lower() == "franklin delano roosevelt":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is Franklin D. Roosevelt.\n")

    # Question 4
    answer = input("4. Who was President during the September 11 attacks in 2001? ")
    if answer.strip().lower() == "george w. bush":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is George W. Bush.\n")

    # Question 5
    answer = input("5. Who was the first African American President of the United States? ")
    if answer.strip().lower() == "barack obama":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is Barack Obama.\n")

    # Final Score
    print(f"🎉 Quiz complete! Your score: {score}/5")
    if score == 5:
        print("🏆 Excellent! You're a presidential pro!")
    elif score >= 3:
        print("👍 Good job! You know your history.")
    else:
        print("📚 Keep learning! History is fascinating.")

if __name__ == "__main__":
    main()
