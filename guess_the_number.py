# Things that will make the game work
from random import *
import os
import time
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome instructions
print("Welcome to the random number guessing game!\n")
print("You will get to choose a small number and a big one, then we'll select a random number in between that you will have to guess.\n\n")
time.sleep(2)

# Getting info for game
small = int(input("Small number: "))
large = int(input("Large number: "))
lives = int(input("Amount of guesses: "))

# Generating random numbers
random_number = randint(small, large)
guesses = 0

# Game instructions
while True:
    clear_console()
    print(f"Please enter a guess between {small} and {large}")
    guess = int(input("Guess: "))
    if random_number == guess:
        print("\nYou guessed the number! Congrats!")
        print(f"It took you {guesses} amount of guesses")
        break
    elif (guesses >= lives):
        print("You ran out of guesses.")
        print(f"The number was {random_number}")
        break
    else:
        clear_console()
        print("That is not the number.")
        guesses += 1
        time.sleep(2)
