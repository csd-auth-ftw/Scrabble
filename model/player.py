import itertools
from utilities import config
from model.bag import Bag

CPU_MODE_MIN = 1
CPU_MODE_MAX = 2
CPU_MODE_SMART = 3

class Player:
    def __init__(self, name):
        self.name = name
        self.is_playing = False
        self.score = 0
        self.words = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def append_word(self, word):
        self.words.append(word)

    def get_word(self):
        return self.words

    def get_last_word(self):
        return self.words[len(self.words) - 1] if len(self.words) > 0 else None

    def set_is_playing(self, state):
        self.is_playing = state

    def cpu_play(self, characters, mode):
        # make sure characters is an uppercase string
        if isinstance(characters, list):
            characters = "".join(characters)
        characters = characters.upper()

        wlens = range(2, 8)

        if mode == CPU_MODE_MAX:
            wlens = reversed(wlens)

        selected = None
        for l in wlens:
            for word in itertools.permutations(characters, l):
                # convert tupple to str
                word = ''.join(word)

                # check if valid word
                if word in config.GREEK7_WORDS:
                    score = Bag.count_score(word)

                    if selected == None or selected[1] < score:
                        selected = (word, score, l)

                    if mode < CPU_MODE_SMART:
                        return selected

        return selected
