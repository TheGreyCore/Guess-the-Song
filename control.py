from random import randint, choice
from PIL import Image, ImageDraw, ImageFont
from pandas import read_csv
from pygame import mixer
from pygame import error as py_error

mixer.init()

DATA_PATH = "songs/list.csv"
data = read_csv(DATA_PATH)
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
        self.score = [0, 0] # score[0] == Correct answers , score[1] == Incorrect  answers

    def random_song(self):
        self.correct_answer_id = randint(0, 3)
        not_taken_songs_names = names.copy()
        correct_song_name = choice(not_taken_songs_names)
        not_taken_songs_names.remove(correct_song_name)
        generate_buttons_images(correct_song_name, True, f"Button_{self.correct_answer_id}")

        for i in range(0, 4):
            if self.correct_answer_id == i:
                pass
            else:
                song_name = choice(not_taken_songs_names)
                not_taken_songs_names.remove(song_name)
                generate_buttons_images(song_name, False, f"Button_{i}")

        return [correct_song_name, paths[names.index(correct_song_name)]]

    def play_or_stop_music(self):
        if self.play_status:
            mixer.music.pause()
            self.play_status = False
        else:
            mixer.music.unpause()
            self.play_status = True

    def play_new_song(self, song_path):
        try:
            mixer.music.load(f"songs/{song_path}")
            mixer.music.play(loops=2)
            self.play_status = True
        except py_error as error:
            return error

    def check_answer(self, button_id):
        if self.correct_answer_id == button_id:
            self.score[0] += 1
            return True
        else:
            self.score[1] += 1
            return False


def generate_buttons_images(text, green_or_red, button_name):
    # Function for generating images for buttons
    def add_image_text(button_template, num):
        image_text = ImageDraw.Draw(button_template)
        text_length = image_text.textlength(text, font=BUTTON_FONT) // 2

        image_text.text(
            (button_template.size[0] // 2 - text_length,  # X
             button_template.size[1] // 2 - BUTTON_FONT_SIZE / 2),  # Y
            text,  # TEXT
            fill=(0, 0, 0),  # COLOR
            font=BUTTON_FONT,  # FONT
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

