import pygame

from model.button import Button
from utils import config
from view.view import View
from controller.events import ClickEvent, NewGameEvent, PressEvent


class Intro(View):
    def __init__(self, event_manager):
        # clear the screen first
        self.event_manager = event_manager
        self.menu_font = pygame.font.Font(None, 40)
        self.options = [Button(self.menu_font, config.NEW_GAME, (140, 105), self.on_new_game_click),
                        Button(self.menu_font, config.LOAD_GAME, (135, 155), self.on_load_game_click),
                        Button(self.menu_font, config.OPTIONS, (145, 205), self.on_options_click)]

        for option in self.options:
            self.event_manager.register(ClickEvent, option)

        self.event_manager.register(PressEvent, self)

    def on_new_game_click(self, button, event):
        self.event_manager.post(NewGameEvent())

    def on_load_game_click(self, button, event):
        print("Load Game")

    def on_options_click(self, button, event):
        print("Options")

    def on_press(self, event):
        print("i pressed key with code:" + str(event.keyCode))

    def on_press_space(self, event):
        print("i pressed space")

    def on_press_enter(self, event):
        print("i pressed enter")

    def render(self):
        self.screen = pygame.display.get_surface()
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        screen.fill(config.WHITE)

        for option in self.options:
            option.render(self.screen)

    def on_destroy(self):
        for option in self.options:
            self.event_manager.remove(ClickEvent, option)
