import turtle as t
import random


# Function to move a turtle forward
def move_forward(turtle):
    turtle.forward(random.randint(5, 15))


# Function to restart the race
def restart_race():
    for turtle in turtles:
        turtle.goto(-200, 70 - turtles.index(turtle) * 30)
    referee.clear()
    user_bet = t.textinput("Place Your Bet", "Enter the color you're betting on:").lower()

    while user_bet not in colors:
        user_bet = t.textinput("Invalid Bet", "Please enter a valid color:").lower()

    return user_bet


# Set up turtle screen
t.speed(0)
t.hideturtle()
t.bgcolor("skyblue")  # Set background color to sky blue
t.title("Turtle Race Game")

# Create 6 turtles with different colors
colors = ["red", "blue", "green", "orange", "purple", "brown"]
turtles = []

for i in range(6):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-200, 70 - i * 30)  # Starting line positions
    turtles.append(new_turtle)

# Finish line
finish_line = t.Turtle()
finish_line.penup()
finish_line.goto(200, 100)
finish_line.pendown()
finish_line.goto(200, -100)

# Referee
referee = t.Turtle()
referee.penup()
referee.hideturtle()
referee.goto(0, 120)

# Flags at the finish line
flag1 = t.Turtle()
flag1.shape("square")
flag1.color("black")
flag1.shapesize(stretch_wid=2, stretch_len=0.5)
flag1.penup()
flag1.goto(200, 60)

flag2 = t.Turtle()
flag2.shape("square")
flag2.color("black")
flag2.shapesize(stretch_wid=2, stretch_len=0.5)
flag2.penup()
flag2.goto(200, -60)

# Get initial user bet
user_bet = restart_race()

# Race loop
while True:
    winner_announced = False

    while not winner_announced:
        for turtle in turtles:
            move_forward(turtle)

            # Check if a turtle has crossed the finish line
            if turtle.xcor() > 200:
                winner_color = turtle.color()[0]
                referee.write(f"{winner_color.capitalize()} Turtle wins!", align="center", font=("Arial", 16, "normal"))

                # Check if the user's bet is correct
                if user_bet == winner_color:
                    t.textinput("Congratulations!", "You've won the bet!")
                else:
                    t.textinput("Better luck next time!",
                                f"The winner was {winner_color.capitalize()}, not {user_bet.capitalize()}.")

                winner_announced = True
                break

    # Ask the user if they want to restart the race
    restart_choice = t.textinput("Race Restart", "Do you want to restart the race? (yes/no)").lower()

    if restart_choice != 'yes':
        break  # Exit the loop if the user doesn't want to restart

    # Restart the race with a new user bet
    user_bet = restart_race()

t.mainloop()
