import random

def number_guessing_game():
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    max_attempts = 10

    print("Guess the number between 1 and 100.")
    print(f"You have {max_attempts} tries.")

    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries!")
            return

    print(f"Sorry, you've used all your tries. The number was {secret_number}.")


number_guessing_game()

