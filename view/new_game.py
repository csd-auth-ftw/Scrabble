import pygame

from controller.events import PressEvent, ClickEvent
from utilities import config
from model.bag import Bag
from model.player import Player
from model.button import Button
from view.board import Board
from view.deck import Deck
from view.score_board import ScoreBoard
from view.view import View


class NewGame(View):
    def __init__(self, event_manager):
        super().__init__(event_manager)

        self.clock = pygame.time.Clock()
        self.button_font = pygame.font.SysFont("monospace", 24)
        self.board = Board(self.event_manager, 100, 100, 1, 7)

        self.options = [Button(self.button_font, config.PICK_LETTER, (635, 105), self.on_pick_letter_click),
                        Button(self.button_font, config.END_ROUND, (635, 155), self.on_end_round_click),
                        ]

        # init players
        self.player_a = Player('Player 1')
        self.player_b = Player('PC')

        # todo remove
        self.player_a.append_word('japan')
        self.player_b.is_playing = True
        self.player_a.set_score(1220)
        self.player_b.append_word('nigeria')
        self.player_a.set_score(890)

        self.score_board = ScoreBoard(self.player_a, self.player_b, 20, 20)
        self.deck = Deck(self.event_manager, 50, 350)
        self.bag = Bag()

        for option in self.options:
            self.event_manager.register(ClickEvent, option)


    def on_pick_letter_click(self, button, event):
        # TODO self.player_a.pick_letter(self.bag)
        pass

    def on_end_round_click(self, button, event):
        print("end round")

    def on_press_space(self, event):
        self.player_a.pick_letter(self.bag)

    def on_press_enter(self, event):
        print("i pressed enter")

    def render(self):
        self.screen.fill(config.BLACK)

        # draws the score board
        self.score_board.render()

        # draws the board
        self.board.render()

        # draws the options
        for option in self.options:
            option.render(self.screen)

        # draws the decks
        self.deck.render()

        # Limit to 60 frames per second
        self.clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def on_destroy(self):
        print("destroy new_game view")

        # call nested views on_destroy
        self.score_board.on_destroy()
        self.board.on_destroy()
        self.deck.on_destroy()

        for option in self.options:
            self.event_manager.remove(ClickEvent, option)
        