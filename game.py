import random

print("🎯 Number Guessing Game")

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low ⬇️")
            elif guess > number:
                print("Too high ⬆️")
            else:
                print("Correct 🎉")
                print("Attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing 👋")
        break