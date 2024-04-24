from random import randint

guesses = 0
number = randint(1, 50)

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    guesses += 1

    if guess < number:
        print("Your guess was too low")
    elif guess > number:
        print("Your guess was too high")
    else:
        print("Congratulations, you guessed the number!")
        print("It took you", guesses, "guesses.")
        break
