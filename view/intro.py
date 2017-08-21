import pygame

from model import button
from utils import config
from view.view import View


class Intro(View):
    def __init__(self, event_manager):
        # clear the screen first
        self.event_manager = event_manager
        self.menu_font = pygame.font.Font(None, 40)
        self.options = [button.Button(self.menu_font, config.NEW_GAME, (140, 105)),
                        button.Button(self.menu_font, config.LOAD_GAME, (135, 155)),
                        button.Button(self.menu_font, config.OPTIONS, (145, 205))]

        for option in self.options:
            self.event_manager.RegisterButtonListener(option, self)

    def render(self):
        self.screen = pygame.display.get_surface()
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        screen.fill(config.WHITE)

        for option in self.options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw(self.screen)

    def on_destroy(self):
        for option in self.options:
            self.event_manager.UnregisterButtonListener(option)
