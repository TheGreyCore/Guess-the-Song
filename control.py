import random

from PIL import Image, ImageDraw, ImageFont
from random import choice
import pandas

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
        print("Init")

    def random_song(self, ):
        correct_answer_id = random.randint(0, 3)
        not_taken_songs_names = names.copy()

        for i in range(0,4):
            song_name = random.choice(not_taken_songs_names)
            not_taken_songs_names.remove(song_name)
            if correct_answer_id == i:
                generate_buttons_images(song_name, True, f"Button_{i}")
            else:
                generate_buttons_images(song_name, False, f"Button_{i}")
        return [names[correct_answer_id], paths[correct_answer_id]]

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