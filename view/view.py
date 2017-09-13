import pygame
from utilities import config


class View:
    def __init__(self, event_manager=None):
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        self.event_manager = event_manager

    def render(self):
        pass

    def on_destroy(self):
        pass