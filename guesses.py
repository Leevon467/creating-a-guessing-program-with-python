from random import randint
guesses = 1
number = randint(1, 50)

guess = int(input("guess a number between 1 and 50"))

while guess != number:
    if guess < number:
        print("your guess was too low")
        guess = int(input("Guess again"))
        guesses = guesses + 1

    elif guess > number:
        print("your guess was too high")
        guess = int(input("Guess again"))
        guesses = guesses + 1

    print()
    print("congratulations, you guessed the number")
    print("it only took you", guesses, "guesses")