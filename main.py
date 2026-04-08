#Setup
import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
Image = "blank_states_img.gif"
screen.addshape(Image)
turtle.shape(Image)

#Turtle that writes state on screen if guess = correct
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

#The data
data = pandas.read_csv("50_states.csv")
guessed_states = []
states_to_learn = data.state.tolist()

game_on = True
while game_on:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state").title()
    if guess_state == "Exit":
        break
        screen.bye()
    if guess_state in data["state"].values:
        x = data[data["state"] == guess_state]["x"].tolist()[0]
        y = data[data["state"] == guess_state]["y"].tolist()[0]
        writer.goto(x, y)
        writer.write(guess_state)
        guessed_states.append(guess_state)
        states_to_learn.remove(guess_state)
    else:
        print("no")
print(states_to_learn)

learning_csv = pandas.DataFrame(states_to_learn)
learning_csv.to_csv("learning_csv.csv")
