from turtle import Turtle
ALIGNMENT = 'center'
FONT =('courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("data.txt")
        self.high_score = int(data.read())
        data.close()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()







