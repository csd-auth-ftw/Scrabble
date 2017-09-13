import pygame
from utilities import config


class View:
    #TODO
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)

    def render(self):
        print("render called")

    def on_destroy(self):
        print("on destroy")