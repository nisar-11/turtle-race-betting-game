from turtle import Turtle, Screen  # Import the Turtle and Screen modules
import random  # Import the random module for generating random numbers
import turtle

# Set up the screen
turtle.title("Turtle Race")  # Title of the Turtle graphics window
screen = Screen()  # Create a screen object
screen.setup(500, 400)  # Set up the screen size (width=500, height=400)
race_on = False  # Flag to indicate if the race is active

# Get user's bet
user_bet = screen.textinput("Make your BET", "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "purple", "orange", "black"]  # List of turtle colors
y_positions = [-100, -60, -20, 20, 60, 100]  # List of starting Y positions for turtles
turtles = []  # List to store turtle objects
indexs = [0, 1, 2, 3, 4, 5]  # Index list for turtles

# Create turtles and set their properties
for index in range(6):
    tim = Turtle("turtle")  # Create a turtle with the shape "turtle"
    tim.flag = 0  # Custom attribute to track if the turtle crossed the finish line
    turtles.append(tim)  # Add the turtle to the list
    tim.penup()  # Lift the pen so turtles don't draw on movement
    tim.color(colors[index])  # Set the color of the turtle
    tim.goto(-236, y_positions[index])  # Position the turtle at the starting line

# Start the race if the user has made a bet
if user_bet:
    race_on = True

flag = 0  # Counter for turtles crossing the finish line
winner_not_found = True  # Flag to indicate if a winner is yet to be determined
count = 0  # Counter to track if all turtles have crossed the finish line

# Race loop
while race_on:
    distance = random.randint(0, 10)  # Generate a random distance for a turtle to move
    index = random.choice(indexs)  # Randomly select a turtle
    turtles[index].forward(distance)  # Move the selected turtle forward

    for turtle in turtles:
        if winner_not_found:  # Check for the first winner
            if turtle.xcor() > 250:  # If the turtle crosses the finish line
                winning_color = turtle.pencolor()  # Get the winning turtle's color
                # Check if the user's bet matches the winning color
                if winning_color == user_bet:
                    print(f"You won the bet, the winner is {winning_color} turtle")
                else:
                    print(f"You lost the bet, The winner is {winning_color} turtle")
                winner_not_found = False  # Stop checking for winners

        if turtle.xcor() > 250:  # Increment flag if a turtle crosses the finish line
            turtle.flag += 1
        if turtle.flag == 6:  # If all turtles have crossed the finish line
            count += 1
        if count == 6:  # End the race when all turtles have crossed
            race_on = False
