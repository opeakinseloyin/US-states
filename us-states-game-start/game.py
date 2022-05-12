import pandas
from turtle import Turtle

data = pandas.read_csv("50_states.csv")


class GameBrain(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.states = data["state"].to_list()
        self.x_list = data["x"].to_list()
        self.y_list = data["y"].to_list()
        self.position = ()
        self.score = 0
        self.right_answer = []
        self.number = []
        self.new_data = []

    def state_check(self, guess):
        if self.states.count(guess) > 0:
            self.right_answer.append(guess)
            return True
        else:
            return False

    def get_cord(self, guess):
        number = self.states.index(guess)
        self.number.append(number)
        x = self.x_list[number]
        y = self.y_list[number]
        self.position = (x, y)

    def writing(self, guess):
        self.goto(self.position)
        self.write(f"{guess}", "center", font=("Courier", 8, "normal"))

    def score_increase(self):
        self.score += 1

    def create(self):
        self.new_data = data.drop(self.number)
        self.new_data.to_csv("new_data.csv")
