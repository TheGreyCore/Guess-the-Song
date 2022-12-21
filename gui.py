from tkinter import Tk, Button, Canvas, PhotoImage
from control import Control
import pygame

FONT = "Bahnschrift"
BACKGROUND = "#ccd6a6"

control = Control()
correct_answer = control.random_song()
pygame.mixer.init()
def stop():
    pygame.mixer.music.stop()


def play():
    pygame.mixer.music.load(f"songs/{correct_answer[1]}")
    pygame.mixer.music.play(loops=2)

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Guess the Song!")
        self.root.config(padx=20, pady=20, background=BACKGROUND)

        panel_small = PhotoImage(file="source/template/buttons/panel_short.png")

        # Buttons
        images = []
        self.buttons = []
        for i in range (0, 4):
            images.append(PhotoImage(file=f"source/buttons/Button_{i}_1"))
            self.buttons.append(Button(self.root, image=images[i], highlightthickness=0, bd=0))

        self.buttons[0].grid(row=0, column=0)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=1, column=0)
        self.buttons[3].grid(row=1, column=1)

        button_play_image = PhotoImage(file="images/play_button.png")
        self.button_play = Button(self.root, image=button_play_image, highlightthickness=0, bd=0)
        self.button_play.grid(row=3, column=0)

        # Canvas
        self.canvas = Canvas(width=320, height=120, background=BACKGROUND, highlightthickness=0)
        self.canvas.create_image(160, 60, image=panel_small)
        self.canvas.create_text(160, 60, text="R: 0 W:0", font=(FONT, 20))
        self.canvas.grid(row=3, column=1)

        self.root.mainloop()

play()