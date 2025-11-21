import random
def number_game():
    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Enter your guess:"))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again. \n")
        else:
            print(f" Correct! you guessed the number in {attempts} attemps")
            break
number_game()