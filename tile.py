import pygame


class Tile:
    def __init__(self, screen, x, y, width, height, letter=None, letter_value=None, player=None, margin=3):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.letter = letter
        self.player = player
        self.letter_value = letter_value  # TODO get it from somewhere else
        self.margin = margin

    def put_letter(self, letter, letter_value, player):
        self.letter = letter
        self.letter_value = letter_value
        self.player = player

    # TODO
    def move(self):
        pass

    def get_letter(self):
        return self.letter

    def empty(self):
        self.letter = None
        self.letter_value = None
        self.player = None

    def is_empty(self):
        return self.letter == None

    def render(self):
        # check if empty tile
        if self.letter == None:
            return

        # background outer
        bg_color_outer = (205, 205, 205)
        rect_outer = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, bg_color_outer, rect_outer)

        # background
        bg_color = (255, 255, 255)
        rect = pygame.Rect(self.x + self.margin, self.y + self.margin, self.width - self.margin*2, self.height - self.margin*2)
        pygame.draw.rect(self.screen, bg_color, rect)

        # letter
        myfont = pygame.font.SysFont("monospace", 26, bold=True)
        letter_sur = myfont.render(self.letter.upper(), 1, (0, 0, 0))
        lw, lh = letter_sur.get_size()
        self.screen.blit(letter_sur, (self.x + (self.width - lw)/2, self.y + (self.height - lh)/2))

        # letter value
        # TODO position it based on letter position
        myfont = pygame.font.SysFont("monospace", 13, bold=True)
        value_sur = myfont.render(str(self.letter_value), 1, (0, 0, 0))
        vw, vh = value_sur.get_size()
        self.screen.blit(value_sur, (self.x + self.width - self.margin*2 - vw + 3, self.y + self.height - self.margin*2 - vh  + 3))