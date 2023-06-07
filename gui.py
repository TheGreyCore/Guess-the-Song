from tkinter import Tk, Button, Canvas, PhotoImage, messagebox
from control import Control
from time import sleep

FONT = "Bahnschrift"
BACKGROUND = "#ccd6a6"

control = Control()
correct_answer = control.random_song()
control.play_new_song(correct_answer[1])


class GUI:
    def __init__(self):

        # Windows settings
        self.root = Tk()
        self.root.title("Guess the Song!")
        self.root.iconbitmap("source/ico/logo.ico")
        self.root.config(padx=20, pady=20, background=BACKGROUND)

        # Create buttons with answers
        images = []
        self.buttons = []
        for i in range(0, 4):
            images.append(PhotoImage(file=f"source/buttons/Button_{i}_1"))
            self.buttons.append(Button(
                self.root,
                image=images[i],
                highlightthickness=0,
                bd=0,
                activebackground=BACKGROUND,
            )
            )

        # Add function to them
        self.buttons[0].config(command=lambda: self.press_answer_button(0))
        self.buttons[1].config(command=lambda: self.press_answer_button(1))
        self.buttons[2].config(command=lambda: self.press_answer_button(2))
        self.buttons[3].config(command=lambda: self.press_answer_button(3))

        # Set position
        self.buttons[0].grid(row=0, column=0)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=1, column=0)
        self.buttons[3].grid(row=1, column=1)

        # Create Play and pause button
        button_play_image = PhotoImage(file="source/buttons/play_button.png")
        self.button_play = Button(
            self.root,
            image=button_play_image,
            highlightthickness=0,
            bd=0,
            command=lambda: control.play_or_stop_music()
        )
        self.button_play.grid(row=2, column=0)

        # Create information panel
        panel_small = PhotoImage(file="source/template/buttons/panel_short.png")
        self.information_panel = Canvas(width=320, height=120, background=BACKGROUND, highlightthickness=0)
        self.information_panel.create_image(160, 60, image=panel_small)
        self.score_bar_text = self.information_panel.create_text(160, 60, text="R: 0 W:0", font=(FONT, 20))
        self.information_panel.grid(row=2, column=1)

        # Loop GUI
        self.root.mainloop()

    def press_answer_button(self, button_id):

        # Set red stroke for button - if incorrect answer, green when correct
        new_button_image = PhotoImage(file=f"source/buttons/Button_{button_id}_2")
        self.buttons[button_id].configure(image=new_button_image)
        self.buttons[button_id].image = new_button_image

        if control.check_answer(button_id):
            self.root.update()
            sleep(1)
            global correct_answer
            correct_answer = control.random_song()

            try:
                control.play_new_song(correct_answer[1])
            except FileNotFoundError:
                messagebox.showerror(title="Error", message=f"Song file not found!")

            images = []
            for i in range(0, 4):
                images.append(PhotoImage(file=f"source/buttons/Button_{i}_1"))
                self.buttons[i].configure(image=images[i])
                self.buttons[i].image = images[i]

        self.update_score_bar()

    def update_score_bar(self):
        self.information_panel.itemconfig(self.score_bar_text, text=f"R:{control.score[0]} W:{control.score[1]}")