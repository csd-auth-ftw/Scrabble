import pygame
import config

class Deck:
    def __init__(self, screen, x, y):
        self.tiles = []
        self.tiles_number = 7
        self.screen = screen
        self.x = x
        self.y = y

    def render(self):
        # render background
        for i in range(self.tiles_number):
            left = self.x + (config.MARGIN + config.WIDTH) * i + config.MARGIN
            top = self.y + config.MARGIN
            pygame.draw.rect(self.screen, (0, 255, 0), [left, top, config.WIDTH, config.HEIGHT])

        # render tiles
        for t in self.tiles:
            if t is not None:
                t.render()

        pass