import pygame

from view.view import View
from utilities import config


class ScoreBoard(View):
    def __init__(self, player_a, player_b, pos_x, pos_y):
        super().__init__()

        self.player_a = player_a
        self.player_b = player_b
        self.pos_x = pos_x
        self.pos_y = pos_y

        # fonts
        self.score_font = pygame.font.SysFont('monospace', 15)
        self.str_font = pygame.font.SysFont('sans-serif', 17)

        # element sizes
        self.sizes = {
            'row_height': 30,
            'is_playing_width': 40,
            'name_width': 100,
            'score_width': 100
        }

    def render_player(self, player, row):
        row_y = self.pos_y + (row * self.sizes['row_height'])

        # render playing indicator
        if player.is_playing:
            is_playing_pos = (self.pos_x, row_y)
            pygame.draw.circle(self.screen, config.RED, is_playing_pos, 5)

        # render name column
        name_render = self.str_font.render(player.get_name(), 1, config.GREEN)
        name_pos = (self.pos_x + self.sizes['is_playing_width'], row_y)
        self.screen.blit(name_render, name_pos)

        # render score column
        score_render = self.score_font.render(str(player.get_score()), 1, config.GREEN)
        score_pos = (name_pos[0] + self.sizes['name_width'], row_y)
        self.screen.blit(score_render, score_pos)

        # render last_word column
        last_word_render = self.str_font.render(player.get_last_word(), 1, config.GREEN)
        last_word_pos = (score_pos[0] + self.sizes['score_width'], row_y)
        self.screen.blit(last_word_render, last_word_pos)

    def render(self):
        self.render_player(self.player_a, 0)
        self.render_player(self.player_b, 1)