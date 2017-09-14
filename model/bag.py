import random
from utilities import config


class Bag:
    def __init__(self):
        self.collection = []
        self.init_char()

    def __str__(self):
        return str(self.collection)

    def init_char(self):
        for key in config.GREEK_CHAR_DICT.keys():
            char = config.GREEK_CHAR_DICT[key]
            for i in range(char['count']):
                self.collection.append((key, char['points']))

    def get_char(self):
        if not self.collection: return 0
        pos = random.randint(0, len(self.collection) - 1)
        selected = self.collection[pos]
        del self.collection[pos]

        return selected

    def append_chars(self, char_list):
        for char in char_list:
            self.collection.append((char,config.GREEK_CHAR_DICT[char]['points']))

    @staticmethod
    def count_score(word):
        if isinstance(word, str):
            word = list(word)

        score = 0
        for c in word:
            c = c.upper()
            score += config.GREEK_CHAR_DICT[c]['points']

        return score
