import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    max_attempts = 10
    secret_number = random.randint(lower_limit, upper_limit)

    print(f"Welcome to Guess the Number!\nThe secret number is between {lower_limit} and {upper_limit}.\n")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt #{attempt}: Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number!")
            return

    print(f"\nGame over! You couldn't guess the number. The secret number was {secret_number}.")

guess_the_number()
