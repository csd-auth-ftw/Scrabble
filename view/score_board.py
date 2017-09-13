import pygame

from view.view import View
from utilities import config


class ScoreBoard(View):
    def __init__(self, player_a, player_b, pos_x, pos_y, width=300, height=60):
        super().__init__()

        self.player_a = player_a
        self.player_b = player_b
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        # fonts
        self.score_font = pygame.font.SysFont('monospace', 20)
        self.score_font.set_bold(True)
        self.str_font = pygame.font.SysFont('sans-serif', 18)

        # element sizes
        self.sizes = {
            'row_height': 30,
            'is_playing_width': 20,
            'name_width': 100,
            'score_width': 70
        }

    def render_player(self, player, row):
        # TODO maybe move vars
        padding_top = 5
        padding_left = 15
        padding_str_top = 3
        padding_indicator_top = 8
        score_width = 50
        score_height = 20

        row_y = self.pos_y + (row * self.sizes['row_height']) + padding_top

        # render playing indicator
        if player.is_playing:
            is_playing_pos = (self.pos_x + padding_left, row_y + padding_indicator_top)
            pygame.draw.circle(self.screen, config.RED, is_playing_pos, 5)

        # render name column
        name_render = self.str_font.render(player.get_name(), 1, config.GREEN)
        name_pos = (self.pos_x + self.sizes['is_playing_width'] + padding_left, row_y + padding_str_top)
        self.screen.blit(name_render, name_pos)

        # render score column
        score_render = self.score_font.render(str(player.get_score()), 1, config.BLACK)
        score_pos = (name_pos[0] + self.sizes['name_width'], row_y)
        pygame.draw.rect(self.screen, config.WHITE, [name_pos[0] + self.sizes['name_width'], row_y, score_width, score_height])
        self.screen.blit(score_render, score_pos)

        # render last_word column
        last_word_render = self.str_font.render(player.get_last_word(), 1, config.GREEN)
        last_word_pos = (score_pos[0] + self.sizes['score_width'], row_y + padding_str_top)
        self.screen.blit(last_word_render, last_word_pos)

    def render(self):
        # draw background
        bg_color = (20, 20, 20)  # TODO move variable
        pygame.draw.rect(self.screen, bg_color, [self.pos_x, self.pos_y, self.width, self.height])

        # draw player scores
        self.render_player(self.player_a, 0)
        self.render_player(self.player_b, 1)