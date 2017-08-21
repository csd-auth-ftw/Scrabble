import pygame

from controller.events import TickEvent, NewGameEvent
from utils import config
from view.intro import Intro
from view.new_game import NewGame


class PygameView:
    def __init__(self, event_manager):
        pygame.init()
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.active_view = Intro(self.event_manager)
        self.window = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
        pygame.display.set_caption("Scrabble")

    def Notify(self, event):
        if isinstance(event, TickEvent):
            #draw everything
            self.active_view.render()
            pygame.display.update()
        elif isinstance(event, NewGameEvent):
            print("pygame view new game")
            self.active_view.on_destroy()
            self.active_view = NewGame(self.event_manager)
