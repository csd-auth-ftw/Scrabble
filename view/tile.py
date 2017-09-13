import pygame

from view.view import View


class Tile(View):
    def __init__(self, x, y, width, height, char=None, value = -1, margin=3):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.char = char
        self.char_value = value
        self.margin = margin

    def set_char(self, char = None, value = -1):
        self.char = char
        self.char_value = value # TODO get char value

    # TODO
    def move(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def get_char(self):
        return self.char

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def clear(self):
        self.char = None
        self.char_value = None

    def has_char(self):
        return self.char == None

    def render(self):
        if self.has_char():
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
        letter_sur = myfont.render(self.char.upper(), 1, (0, 0, 0))
        lw, lh = letter_sur.get_size()
        self.screen.blit(letter_sur, (self.x + (self.width - lw)/2, self.y + (self.height - lh)/2))

        # letter value
        # TODO position it based on letter position
        myfont = pygame.font.SysFont("monospace", 13, bold=True)
        value_sur = myfont.render(str(self.char_value), 1, (0, 0, 0))
        vw, vh = value_sur.get_size()
        self.screen.blit(value_sur, (self.x + self.width - self.margin*2 - vw + 3, self.y + self.height - self.margin*2 - vh  + 3))