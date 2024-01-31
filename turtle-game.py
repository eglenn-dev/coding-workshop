from turtle import *
from random import randint
import time

# Starting position of the track
speed(0)
penup()
goto(-140, 140)
bgcolor("white")
pencolor("black")

# Generating the racetrack
for step in range(15):
	write(step, align ='center')
	right(90)
	
	# Create racing lines
	for num in range(8):
		penup()
		forward(10)
		pendown()
		forward(10)
	
	# Reset to position at top of racetrack
	penup()
	backward(160)
	left(90)
	forward(20)

# First player
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# Second player
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# Third player
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# Forth player
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# Turtles run at random speeds to the finish line
for turn in range(1, 100):
	player_1.forward(randint(1, 5))
	player_2.forward(randint(1, 5))
	player_3.forward(randint(1, 5))
	player_4.forward(randint(1, 5))

# Adds a pause at the end of the code so the screen stays open
time.sleep(20)