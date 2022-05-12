import turtle
from game import GameBrain

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
game_brain = GameBrain()

turtle.shape(image)

while game_brain.score < 50:
    guess = screen.textinput("Guess a State", f"{game_brain.score}/50 states").title()

    if guess == "Exit":
        break
    if game_brain.state_check(guess):
        game_brain.get_cord(guess)
        game_brain.writing(guess)
        game_brain.score_increase()

    else:
        print("Wrong answer")

game_brain.create()

turtle.mainloop()
