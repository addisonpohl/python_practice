# Guessing Game: The user must guess the number between 1-20
import random

number = random.randint(1, 20)
tries = 1
print("Guess a number between 1 and 20")
print(number)

while True:
    guess = int(input("Number: "))
    if guess > number:
        print("Lower")
        tries += 1
    elif guess < number:
        print("Higher")
        tries += 1
    else:
        print(f"Nice job! You got it in {tries} tries!")
        break
