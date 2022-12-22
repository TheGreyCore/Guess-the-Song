import random
from PIL import Image, ImageDraw, ImageFont
import pandas
import pygame

pygame.mixer.init()

DATA_PATH = "songs/list.csv"
data = pandas.read_csv(DATA_PATH)
    # .to_dict('list')
del data['Unnamed: 0']

names = []
for name in data["Names"]:
    names.append(name)

paths = []
for path in data["Paths"]:
    paths.append(path)

# Button settings
BUTTON_TEMPLATE_PATH = "source/template/buttons/"
BUTTON_FONT_PATH = "source/fonts/Unbounded-VariableFont_wght.ttf"
BUTTON_FONT_SIZE = 14
BUTTON_FONT = ImageFont.truetype(BUTTON_FONT_PATH, BUTTON_FONT_SIZE)
class Control:

    def __init__(self):
        self.song_name = None
        self.song_path = None
        self.play_status = False
        self.correct_answer_id = None

    def random_song(self):
        self.correct_answer_id = random.randint(0, 3)
        not_taken_songs_names = names.copy()
        correct_song_name = random.choice(not_taken_songs_names)
        not_taken_songs_names.remove(correct_song_name)
        print(correct_song_name)
        generate_buttons_images(correct_song_name, True, f"Button_{self.correct_answer_id}")

        for i in range(0,4):
            if self.correct_answer_id == i:
                pass
            else:
                song_name = random.choice(not_taken_songs_names)
                not_taken_songs_names.remove(song_name)
                generate_buttons_images(song_name, False, f"Button_{i}")

        return [correct_song_name, paths[names.index(correct_song_name)]]

    def play_button(self, song_path: None):
        if self.play_status:
            pygame.mixer.music.stop()
            self.play_status = False
        else:
            pygame.mixer.music.load(f"songs/{song_path}")
            pygame.mixer.music.play(loops=2)
            self.play_status = True

    def check_answer(self, button_id):
        if self.correct_answer_id == button_id:
            return True
        else:
            return False


def generate_buttons_images(text, green_or_red, button_name):
    # Function for generating images for button canvas
    def add_image_text(button_template, num):
        image_text = ImageDraw.Draw(button_template)
        text_length = image_text.textlength(text, font=BUTTON_FONT) // 2

        image_text.text(
            (button_template.size[0] // 2 - text_length,  # X
            button_template.size[1] // 2 - BUTTON_FONT_SIZE/2),  # Y
            text,  # TEXT
            fill=(0, 0, 0),  # COLOR
            font=BUTTON_FONT, # FONT
            align="center"
            )

        image.save(f"source/buttons/{button_name}_{num}", "PNG")

    # Save main image
    with Image.open(f"{BUTTON_TEMPLATE_PATH}panel_short.png") as image:
        add_image_text(button_template=image, num=1)

    # Save additional image for pressed button
    if green_or_red:
        # If this correct  option
        with Image.open(f"{BUTTON_TEMPLATE_PATH}panel_short_green.png") as image:
            add_image_text(button_template=image, num=2)
    else:
        # If this wrong option
        with Image.open(f"{BUTTON_TEMPLATE_PATH}panel_short_red.png") as image:
            add_image_text(button_template=image, num=2)
