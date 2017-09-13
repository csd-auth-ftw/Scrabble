from view import deck


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
