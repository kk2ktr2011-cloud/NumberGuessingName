import random

number = random.randint(1, 100)
attempts = 5

print("Welcome To This Game of Number Guessing!\nYou will have five chances to guess the number between 1 and 100.\nGood Luck!")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    attempts -= 1  
else:
    print(f"Sorry, you've run out of attempts. The number was {number}.")
    