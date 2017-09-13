import pygame

from view.view import View
from utilities import config


class ScoreBoard(View):
    def __init__(self, player_a, player_b, pos_x, pos_y):
        super().__init__()
        self.player_a = player_a
        self.player_b = player_b
        self.player_a.append_word("dicks")
        self.player_a.is_playing = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.score_font = pygame.font.SysFont("monospace", 15)
        self.name_font = pygame.font.SysFont("sans-serif", 17)

    def render(self):

        if self.player_a.is_playing:
            pygame.draw.circle(self.screen, config.RED, (self.pos_x, self.pos_y), 5)

        player_name = self.name_font.render(self.player_a.get_name(), 1, config.GREEN)
        self.screen.blit(player_name, (self.pos_x + 20, self.pos_y))

        player_score = self.score_font.render(str(self.player_a.get_score()), 1, config.GREEN)
        self.screen.blit(player_score, (self.pos_x + 100, self.pos_y))

        player_last_word = self.name_font.render(self.player_a.get_last_word(), 1, config.GREEN)
        self.screen.blit(player_last_word, (self.pos_x + 200, self.pos_y))
