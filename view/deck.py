import pygame

from utilities import config
from view import tile
from view.view import View


class Deck(View):
    def __init__(self, screen, x, y):

        self.tiles = []
        self.tiles_number = 7
        self.screen = screen
        self.x = x
        self.y = y
        self.init_deck()

    def init_deck(self):
        for i in range(self.tiles_number):
            left = self.x + (config.MARGIN + config.WIDTH) * i + config.MARGIN
            top = self.y + config.MARGIN - 75
            t = tile.Tile(self.screen, left, top, config.WIDTH, config.HEIGHT)
            self.tiles.append(t)

    def get_free_tile(self):
        for i in range(self.tiles_number):
            if self.tiles[i].is_empty():
                return i
        return -1

    def append_character(self, character):
        pos = self.get_free_tile()

        if pos == -1:
            return False

        self.tiles[pos] = character
        return True

    def render(self):
        # render background
        for i in range(self.tiles_number):
            left = self.x + (config.MARGIN + config.WIDTH) * i + config.MARGIN
            top = self.y + config.MARGIN - 75
            pygame.draw.rect(self.screen, (0, 255, 0), [left, top, config.WIDTH, config.HEIGHT])

        # render tiles
        for t in self.tiles:
            if t is not None:
                t.render()
        pass
