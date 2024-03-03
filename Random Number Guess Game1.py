#Imports the random module
import random
#Keeps track of how many guesses you've made
counter = 1
guess = 0
stop = 1
while stop !=0:
#Generates the random number
    rannum = random.randint(1, 100)
#This loop will continue until you guess correctly. It will also tell you
#if your guess is too high or low
    while guess != rannum:
        guess = int(input("Guess the number between 1 and 100 "))
        if guess == rannum:
            print("Correct! Congration you dun it! ", "You guessed the number in", counter, "attempts. ")
        elif guess >= rannum:
            print("Too high.")
            counter = counter + 1
        elif guess <= rannum:
            print("Too low.")
            counter = counter + 1
#This is where you can either continue guessing a new number or quit
    stop = int(input("Enter any number to continue or 0 to stop "))
