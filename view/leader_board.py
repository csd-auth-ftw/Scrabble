from controller.events import MainMenuEvent, ClickEvent
from utilities import config
import pygame

from utilities.utils import read_from_file
from view.button import Button
from view.view import View


class LeaderBoard(View):

    def __init__(self, event_manager):
        super().__init__()
        self.event_manager = event_manager
        self.font = pygame.font.SysFont("monospace", 40)
        self.score_font = pygame.font.SysFont("sans-serif",30)
        self.button_font = pygame.font.SysFont("monospace", 24)

        self.options = [Button(self.button_font, config.BACK, (100, 20), self.on_back_clicked)]

        self.scores = []
        self.read_scores()

        for option in self.options:
            self.event_manager.register(ClickEvent, option)

    def read_scores(self):
        self.scores = read_from_file(config.SCORES_PATH)
        print(self.scores)

    def on_back_clicked(self, button, event):
        self.event_manager.post(MainMenuEvent())

    def render(self):
        self.screen.fill(config.WHITE)

        label_title = self.font.render("Score", 1, config.BLACK)
        self.screen.blit(label_title,(100,100))

        # draws the options
        for option in self.options:
            option.render(self.screen)

        max = 5
        lines = len(self.scores) if len(self.scores) < max else max
        for i in range(lines):
            msg = "Game  #%d - score: user %s vs pc %s - turns: %d" %(len(self.scores) - i, self.scores[i][0], self.scores[i][1], self.scores[i][2])
            label_score = self.score_font.render(msg, 1 ,config.BLACK)
            self.screen.blit(label_score, (100, 150 + i * 20))

    def on_destroy(self):
        pass