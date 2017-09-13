import os

# basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# screen size
SCREEN_W = 600
SCREEN_H = 450
WINDOW_SIZE = [SCREEN_W, SCREEN_H]

# tile sizes
DECK_TILE_WIDTH = 46
DECK_TILE_HEIGHT = 46

BOARD_TILE_WIDTH = 70
BOARD_TILE_HEIGHT = 70

MARGIN = 2

GREEK_CHAR_DICT = {
    'Α': {'points': 1, 'count': 12},
    'Ε': {'points': 1, 'count': 8},
    'Η': {'points': 1, 'count': 7},
    'Ι': {'points': 1, 'count': 8},
    'Ν': {'points': 1, 'count': 6},
    'Ο': {'points': 1, 'count': 9},
    'Σ': {'points': 1, 'count': 7},
    'Τ': {'points': 1, 'count': 8},
    'Κ': {'points': 2, 'count': 4},
    'Π': {'points': 2, 'count': 4},
    'Ρ': {'points': 2, 'count': 5},
    'Υ': {'points': 2, 'count': 4},
    'Λ': {'points': 3, 'count': 3},
    'Μ': {'points': 3, 'count': 3},
    'Ω': {'points': 3, 'count': 3},
    'Γ': {'points': 4, 'count': 2},
    'Δ': {'points': 4, 'count': 2},
    'Β': {'points': 8, 'count': 1},
    'Φ': {'points': 8, 'count': 1},
    'Χ': {'points': 8, 'count': 1},
    'Ζ': {'points': 10, 'count': 1},
    'Θ': {'points': 10, 'count': 1},
    'Ξ': {'points': 10, 'count': 1},
    'Ψ': {'points': 10, 'count': 1}
}

# load words from greek7.txt
GREEK7_WORDS = {}
greek7_path = os.path.normpath(os.path.dirname(__file__) + "/../res/words/greek7.txt")
with open(greek7_path, encoding="utf8") as rfile:
    for line in rfile:
        word = line.strip()
        # todo change
        GREEK7_WORDS[word] = 0

#-----------------------------BUTTON NAMES-------------------------------------

NEW_GAME = "NEW GAME"
LEADER_BOARD = "LEADER BOARD"
OPTIONS = "OPTIONS"
PICK_LETTER = "Pick letter"
END_ROUND = "End round"
CLEAR = "Clear"
BACKSPACE = "Backspace"