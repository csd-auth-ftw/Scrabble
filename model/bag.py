import random


class Bag:
    def __int__(self):
        self.collection = {}

    def __str__(self):
        return str(self.collection)

    def init_bag(self):
       self.collection = {
            'α': {'points': 1, 'count': 12},
            'ε': {'points': 1, 'count': 8},
            'η': {'points': 1, 'count': 7},
            'ι': {'points': 1, 'count': 8},
            'ν': {'points': 1, 'count': 6},
            'ο': {'points': 1, 'count': 9},
            'σ': {'points': 1, 'count': 7},
            'τ': {'points': 1, 'count': 8},
            'κ': {'points': 2, 'count': 4},
            'π': {'points': 2, 'count': 4},
            'ρ': {'points': 2, 'count': 5},
            'υ': {'points': 2, 'count': 4},
            'λ': {'points': 3, 'count': 3},
            'μ': {'points': 3, 'count': 3},
            'ω': {'points': 3, 'count': 3},
            'γ': {'points': 4, 'count': 2},
            'δ': {'points': 4, 'count': 2},
            'β': {'points': 8, 'count': 1},
            'φ': {'points': 8, 'count': 1},
            'χ': {'points': 8, 'count': 1},
            'ζ': {'points': 10, 'count': 1},
            'θ': {'points': 10, 'count': 1},
            'ξ': {'points': 10, 'count': 1},
            'ψ': {'points': 10, 'count': 1},
            '?': {'points': 0, 'count': 2}  # einai ta leuka(mpalader)
        }



    def get_letter(self):
        if not self.collection: return 0

        letter, points = random.choice(list(self.collection.items()))
        self.collection[letter]['count'] = self.collection[letter]['count'] - 1
        # mporoume eite na kanoume pop h na to midenizoume gia na kratame to gramma
        if self.collection[letter]['count'] == 0:
            self.collection.pop(letter)

        return letter, points['points']
