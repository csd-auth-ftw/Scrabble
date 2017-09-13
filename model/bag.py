import random
from utilities import config


class Bag:
    def __init__(self):
        self.collection = config.GREEK_CHAR_DICT

    def __str__(self):
        return str(self.collection)

    def get_char(self):
        if not self.collection: return 0

        letter, points = random.choice(list(self.collection.items()))
        self.collection[letter]['count'] = self.collection[letter]['count'] - 1
        # mporoume eite na kanoume pop h na to midenizoume gia na kratame to gramma
        if self.collection[letter]['count'] == 0:
            self.collection.pop(letter)

        return letter, points['points']

    @staticmethod
    def count_score(word):
        if isinstance(word, str):
            word = list(word)

        score = 0
        for c in word:
            c = c.upper()
            score += config.GREEK_CHAR_DICT[c]['points']

        return score