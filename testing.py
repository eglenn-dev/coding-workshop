# Welcome to Python!
from datetime import datetime

# What information do we want from the user?
first_name = ""
last_name = ""
birth_year = 0

# Getting user information
print("Welcome to my Python program! We are going to write a sentence about you!\n")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
birth_year = int(input("What year were you born? "))

# Calculate age
current_year = datetime.now().year
age = current_year - birth_year

print(f"Your name is {first_name} {last_name} and you are {age} years old this year! Next year, you will turn {age + 1}!")


