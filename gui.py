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
        self.root = Tk()
        self.root.title("Guess the Song!")
        self.root.config(padx=20, pady=20, background=BACKGROUND)
        panel_small = PhotoImage(file="source/template/buttons/panel_short.png")

        # Buttons
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

        self.buttons[0].config(command=lambda: self.press_answer_button(0))
        self.buttons[1].config(command=lambda: self.press_answer_button(1))
        self.buttons[2].config(command=lambda: self.press_answer_button(2))
        self.buttons[3].config(command=lambda: self.press_answer_button(3))

        self.buttons[0].grid(row=0, column=0)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=1, column=0)
        self.buttons[3].grid(row=1, column=1)

        button_play_image = PhotoImage(file="images/play_button.png")
        self.button_play = Button(
            self.root,
            image=button_play_image,
            highlightthickness=0,
            bd=0,
            command=lambda: control.play_or_stop_music(correct_answer[1])
        )
        self.button_play.grid(row=3, column=0)

        # Canvas
        self.canvas = Canvas(width=320, height=120, background=BACKGROUND, highlightthickness=0)
        self.canvas.create_image(160, 60, image=panel_small)
        self.canvas.create_text(160, 60, text="R: 0 W:0", font=(FONT, 20))
        self.canvas.grid(row=3, column=1)

        self.root.mainloop()

    def press_answer_button(self, button_id):
        if control.check_answer(button_id):
            correct_image = PhotoImage(file=f"source/buttons/Button_{button_id}_2")
            self.buttons[button_id].configure(image=correct_image)
            self.buttons[button_id].image = correct_image
            self.root.update()
            sleep(1)

            global correct_answer
            correct_answer = control.random_song()
            error = control.play_new_song(correct_answer[1])
            if error:
                messagebox.showerror(title="Error", message=f"Check your mp3 file!\n Error: {error}")

            images = []
            for i in range(0, 4):
                images.append(PhotoImage(file=f"source/buttons/Button_{i}_1"))
                self.buttons[i].configure(image=images[i])
                self.buttons[i].image = images[i]
        else:
            image = PhotoImage(file=f"source/buttons/Button_{button_id}_2")
            self.buttons[button_id].configure(image=image)
            self.buttons[button_id].image = image
