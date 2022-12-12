# Guess The Song game by Dmitri Matetski
# The game is made for learning purposes

import tkinter
import pygame
from control import Control

# ------------------
# Colours
BACKGROUND = "#404258"

FONT = "Bahnschrift"

root = tkinter.Tk()
root.title('Guess The Song')
root.geometry("1000x600")
root.config(padx=50, pady=50, bg=BACKGROUND)
control = Control()
pygame.mixer.init()


def stop():
    pygame.mixer.music.stop()


def play():
    pygame.mixer.music.load(control.song_path)
    pygame.mixer.music.play(loops=2)


def check():
    if entry.get().lower() == control.song_name:
        control.random_song()
        log.config(text="Correct!", fg='#7CFC00')
        print(control.song_name)
        play()
        entry.delete(0, tkinter.END)
    else:
        log.config(text="Incorrect!", fg='#f00')


label_song = tkinter.Label(root, text="Guess the song", bg=BACKGROUND, font=(FONT, 35))
label_song.grid(row=0, column=1)
log = tkinter.Label(root, text="", bg=BACKGROUND)
log.grid(row=1, column=1)
play_button = tkinter.Button(root, text="Play", width=5, command=play)
play_button.grid(row=1, column=0)
stop_button = tkinter.Button(root, text="Stop", width=5, command=stop)
stop_button.grid(row=2, column=0)
check_button = tkinter.Button(root, text="Check", width=5, command=check)
check_button.grid(row=3, column=0)
entry = tkinter.Entry(width=50)
entry.grid(row=3, column=1, columnspan=2)
entry.focus()
control.random_song()
print(control.song_name)

root.mainloop()
