from tkinter import Tk, Button, Canvas, Label, PhotoImage

FONT = "Bahnschrift"
BACKGROUND = "#ccd6a6"


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Guess the Game")
        self.root.config(padx=20, pady=20, background=BACKGROUND, )

        panel_small = PhotoImage(file="images/panel_short.png")
        # Buttons
        self.button_var_1 = Button(self.root, image=panel_small, highlightthickness=0, bd=0)
        self.button_var_1.grid(row=0, column=0)
        self.button_var_2 = Button(self.root, image=panel_small, highlightthickness=0, bd=0)
        self.button_var_2.grid(row=0, column=1)
        self.button_var_3 = Button(self.root, image=panel_small, highlightthickness=0, bd=0)
        self.button_var_3.grid(row=1, column=0)
        self.button_var_4 = Button(self.root, image=panel_small, highlightthickness=0, bd=0)
        self.button_var_4.grid(row=1, column=1)

        button_play_image = PhotoImage(file="images/play_button.png")
        self.button_play = Button(self.root, image=button_play_image, highlightthickness=0, bd=0)
        self.button_play.grid(row=3, column=0)

        # Labels
        self.label_var_1 = Label(self.root, text="Variant A", background="white", font=(FONT, 20))
        self.label_var_1.grid(row=0, column=0)
        self.label_var_1 = Label(self.root, text="Variant B", background="white", font=(FONT, 20))
        self.label_var_1.grid(row=0, column=1)
        self.label_var_1 = Label(self.root, text="Variant C", background="white", font=(FONT, 20))
        self.label_var_1.grid(row=1, column=0)
        self.label_var_1 = Label(self.root, text="Variant D", background="white", font=(FONT, 20))
        self.label_var_1.grid(row=1, column=1)

        # Canvas
        self.canvas = Canvas(width=320, height=120, background=BACKGROUND, highlightthickness=0)
        self.canvas.create_image(160, 60, image=panel_small)
        self.canvas.create_text(160, 60, text="R: 0 W:0", font=(FONT, 20))
        self.canvas.grid(row=3, column=1)

        self.root.mainloop()
