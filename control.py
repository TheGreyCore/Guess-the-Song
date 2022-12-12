from random import choice
import pandas

PATH = "songs/list.csv"
data = pandas.read_csv(PATH).to_dict('list')
del data['Unnamed: 0']


class Control:

    def __init__(self):
        self.song_name = None
        self.song_path = None

    def random_song(self):
        self.song_name = choice(list(data))
        self.song_path = data[self.song_name][0]
        del data[self.song_name]