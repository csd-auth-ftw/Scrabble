from utilities import config
import pygame

from utilities.utils import read_from_file
from view.view import View


class LeaderBoard(View):

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.font = pygame.font.SysFont("monospace", 40)
        self.scores = []


    def read_scores(self):
        print(read_from_file("score.txt"))

    def render(self):
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        self.screen.fill(config.WHITE)

        label_score = self.font.render("Score", 1, config.BLACK)
        self.screen.blit(label_score,(100,100))

    def on_destroy(self):
        pass