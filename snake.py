SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
SCREEN_COLOUR = "powder blue"
SNAKE_COLOUR = "red"

import sys
import time
import random
import tkinter as tk


class main(tk.Tk):
    """ Game class. Inherits from tk.Tk """

    def __init__(self):
        """ Create game object """
        
        tk.Tk.__init__(self)

        self.create_screen()
        self.create_scoreboard()
        self.setup()
        self.create_snake()
        self.bind("<Any-KeyPress>", self.respond)


    def create_screen(self):
        """ Initial window creation """

        self.board = tk.Canvas(
            self,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            background=SCREEN_COLOUR
            )

        self.board.pack()


    def create_scoreboard(self):
        """ Intital scoreboard creation """
        
        self.scores = tk.Label(
            self,
            text="Score: {}".format(self.score)
            )
        

    def setup(self):
        """ General setup """

        self.x = SNAKE_SPEED
        self.y = 0
        # TODO: figure this out
##        self.roadmap = [(0,0)]
        self.length = 3
        self.target = None
        self.score = 0
        self.valid = 1
        

    def create_snake(self):
        """ Initial snake creation """

        self.snake = self.board.create_rectangle(
            1,
            1,
            11,
            11,
            fill=SNAKE_COLOUR
            )


    def respond(self, event=None):
        """ What happens on key-press """

        key = event.keysym

        if key == "Left":
            self.left()
        elif key == "Right":
            self.right()
        elif key == "Up":
            self.up()
        elif key == "Down":
            self.down()
        

    def update_scores(self):
        """ Update scoreboard """
        pass


    def left(self):
        self.x = -SNAKE_SPEED
        self.y = 0


    def right(self):
        self.x = SNAKE_SPEED
        self.y = 0


    def up(self):
        self.x = 0
        self.y = -SNAKE_SPEED


    def down(self):
        self.x = 0
        self.y = SNAKE_SPEED


    def move(self):
        """ Movement """

        self.board.move(
            self.snake,
            self.x,
            self.y
            )

        x1, y1, x2, y2 = self.board.coords(self.snake)

        if x1 <= 0 or y1 <= 0:
            self.x = 0
            self.y = 0
            self.loss()
        elif x2 >= SCREEN_WIDTH or y2 >= SCREEN_HEIGHT:
            self.x = 0
            self.y = 0
            self.loss()


    def loss(self):
        """ Game Over """

        self.board.create_text(
            screen_width / 2,
            screen_height / 2,
            text ="Game Over",
            font=("arial 60 bold"),
            fill="red"
            )
        self.valid = 0

        
    def re_update(self):
        """ Main game functionality """
        
        if self.valid == 0:
            time.sleep(1)
            self.destroy()
        self.move()
        self.update_snake()
        self.food()


    def food(self):
        """ Handles food generation and eating """
        
        # if there is no food on the board
        if self.target == None:
            x1 = random.randint(15, screen_width - 15)
            y1 = random.randint(15, screen_height - 15)
            self.target = self.board.create_oval(
                x1,
                y1,
                x1 + 10,
                y1 + 10,
                fill="yellow",
                tag="food"
                )

        # if there is food on the board
        if self.target:
            x1, y1, x2, y2 = self.board.coords(self.target)

            # checks if the snake is overlapping a food pellet
            if len(self.board.find_overlapping(x1, y1, x2, y2)) != 1:
                # TODO: call snake growth from here
                self.board.delete("food")
                self.target = None
                self.update_scoreboard()
            


##    def update_snake(self):
##        x1, y1, x2, y2 = self.board.coords(self.snake)
##        x2 = (x2 - ((x2 - x1) / 2))
##        y2 = (y2 - ((y2 - y1) / 2))
##        self.roadmap.append((x2, y2))
##        self.board.delete("body")
##
##        if len(self.roadmap) >= self.length:
##            self.roadmap = self.roadmap[-self.length:]
##
##        self.board.create_line(
##            tuple(self.roadmap),
##            tag="body",
##            width=10,
##            fill=snake_colour
##            )


if __name__ == "__main__":
    # instantiate game object
    root = main()

    # main game loop
    while True:
        try:
            # main logic
            root.update()
            root.update_idletasks()
            root.re_update()
            time.sleep(0.09)
        except:
            # ignore errors
            pass
