import random

def guess(x):
    number = random.randint(1,x)
    guess = 0

    while guess != number:
        guess = int(input("Guess a number: "))
        if guess < int(number):
            print("Guess again, number is too low")
        elif guess > int(number):
            print ("Guess again, number is too high")
        else: 
            print("You have guessed correctly, yay!") 
guess(5)
