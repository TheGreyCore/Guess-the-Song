# Guess The Song game by Dmitri Matetski
# The game is made for learning purposes

import pygame
from gui import GUI

gui = GUI()

pygame.mixer.init()


def stop():
    pygame.mixer.music.stop()


def play():
    # pygame.mixer.music.load(control.song_path)
    pygame.mixer.music.play(loops=2)
