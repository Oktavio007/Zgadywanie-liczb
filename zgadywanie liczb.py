import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number: ")

    try:
        guess = int(guess)
    except ValueError:
        print("It's not a number!")
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You win!")
        break
