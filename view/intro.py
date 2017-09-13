import pygame

from controller.events import ClickEvent, NewGameEvent, LeaderBoardEvent
from utilities import config
from view.button import Button
from view.view import View


class Intro(View):
    def __init__(self, event_manager):
        super().__init__(event_manager)

        # clear the screen first
        self.menu_font = pygame.font.SysFont("monospace", 40)
        self.options = [Button(self.menu_font, config.NEW_GAME, (50, 50), self.on_new_game_click),
                        Button(self.menu_font, config.LEADER_BOARD, (50, 100), self.on_leader_board_click),
                        Button(self.menu_font, config.OPTIONS, (50, 150), self.on_options_click)]

        for option in self.options:
            self.event_manager.register(ClickEvent, option)

    def on_new_game_click(self, button, event):
        self.event_manager.post(NewGameEvent())

    def on_leader_board_click(self, button, event):
        self.event_manager.post(LeaderBoardEvent())

    def on_options_click(self, button, event):
        print("Options")

    def render(self):
        self.screen = pygame.display.get_surface()
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        screen.fill(config.WHITE)

        for option in self.options:
            option.render(self.screen)

    def on_destroy(self):
        for option in self.options:
            self.event_manager.remove(ClickEvent, option)
