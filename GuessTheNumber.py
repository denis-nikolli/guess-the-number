import random

print("Welcome to the Number Guessing Game!")

play_again = "Yes"

while play_again.lower() == "yes":
    number = random.randint(1, 10)
    guess = None
    tries = 0
    max_tries = 3

    print("\nI'm thinking of a number between 1 and 10.")
    print(f"You have {max_tries} tries to guess it.")

    while guess != number and tries < max_tries:
        try:
            guess = int(input("Your guess: "))
            tries += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
    

    if guess == number:         
        print(f"You guessed it in {tries} tries!")
    else:
        print(f"X You're out of tries! The number was {number}.")
    
    play_again = input("Do you want to play again? (Yes/No): ")

print("Thanks for playing!")

















































































































            
