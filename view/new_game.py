import pygame

from controller.events import ClickEvent, TileRemovedEvent, MainMenuEvent
from model.bag import Bag
from model.player import Player, CPU_MODE_SMART
from utilities import config, utils
from view.board import Board
from view.button import Button
from view.deck import Deck
from view.score_board import ScoreBoard
from view.view import View
import os


class NewGame(View):
    def __init__(self, event_manager):
        super().__init__(event_manager)

        self.game_finished = False
        self.playing = False
        self.turn = 0

        self.clock = pygame.time.Clock()
        self.std_font = pygame.font.SysFont("sans-serif", 22)
        self.button_font = pygame.font.SysFont("monospace", 24)
        self.button_font.set_bold(True)
        self.board = Board(self.event_manager, 50, 100, 1, 7)

        self.options = [Button(self.button_font, config.END_ROUND, (235, 200), self.on_end_round_click),
                        Button(self.button_font, config.CLEAR, (150, 250), self.on_clear_click),
                        Button(self.button_font, config.BACKSPACE, (350, 250), self.on_backspace_click)
                        ]

        # init players
        self.player_a = Player('Player 1')
        self.player_b = Player('PC')
        self.render_sleep = 0

        # todo remove
        self.player_a.is_playing = True

        self.score_board = ScoreBoard(self.player_a, self.player_b, 20, 20)
        self.deck = Deck(self.event_manager, 50, 350)
        self.bag = Bag()
        self.set_deck()

        for option in self.options:
            self.event_manager.register(ClickEvent, option)

    def on_clear_click(self, button, event):
        self.board.on_press_esc(event)

    def on_end_round_click(self, button, event):
        if not self.playing:
            self.play()

    def on_backspace_click(self, button, event):
        self.board.on_press_backspace(event)

    def get_player(self):
        return self.player_a if self.player_a.is_playing else self.player_b

    def set_deck(self):
        player = self.get_player()
        deck = []

        if self.bag.remaining_chars() < config.MAX_WORD_LEN:
            return None

        if len(player.unused_words) != config.MAX_WORD_LEN:
            for i in range(len(player.unused_words)):
                deck.append(player.unused_words[i])
                self.deck.append_character(player.unused_words[i])
        else:
            for i in range(len(player.unused_words)):
                self.bag.collection.append(player.unused_words[i])

        while not self.deck.get_free_tile() == -1:
            word = self.bag.get_char()
            deck.append(word)
            self.deck.append_character(word)

        return deck

    def flip_players(self):
        self.player_a.is_playing = not self.player_a.is_playing
        self.player_b.is_playing = not self.player_b.is_playing

    def play(self):

        self.playing = True
        self.turn += 1

        word, word_score = self.board.get_word()

        # check user word and update score
        if word in config.GREEK7_WORDS:
            self.player_a.add_score(word_score)
            self.player_a.append_word(word)

        # clear deck and board
        self.player_a.unused_words = self.deck.clear()
        self.board.clear()

        # computer turn
        self.flip_players()

        if self.bag.remaining_chars() < config.MAX_WORD_LEN:
            return self.end_game()

        deck_cpu = self.set_deck()
        # TODO add back to bag deck_cpu not used chars
        word_cpu = self.player_a.cpu_play([i[0] for i in deck_cpu], CPU_MODE_SMART)

        if word_cpu is None:
           return self.end_game()
        else:
            for i in range(len(word_cpu[0])):
                for j in range(len(deck_cpu)):
                    if deck_cpu[j][0] == word_cpu[0][i]:
                        deck_cpu.pop(j)
                        break

            self.player_b.unused_words = deck_cpu

            self.player_b.append_word(word_cpu[0])
            self.player_b.add_score(word_cpu[1])
            self.board.set_word(word_cpu[0])

        self.render_sleep = 1

    def end_game(self):
        data = [self.player_a.score, self.player_b.score, self.turn]
        utils.write_to_file(config.SCORES_PATH,data)
        self.game_finished = True


    def render(self):

        # draw background
        self.render_background()

        # draws the score board
        self.score_board.render()

        if self.game_finished:
            end_font = pygame.font.SysFont('sans-serif', 100)
            end_font.set_bold(True)
            winner = self.player_a.get_name() if self.player_a.score >= self.player_b.score else self.player_b.get_name()
            rendered_message = end_font.render(winner + " WIN !", 1, config.WHITE)
            self.screen.blit(rendered_message, (config.SCREEN_W / 2 - rendered_message.get_rect().width / 2, config.SCREEN_H / 2 - 20))
            pygame.display.flip()

            pygame.time.delay(3000)
            self.event_manager.post(MainMenuEvent())
        else:
            # draws the board
            self.board.render()

            # draws the options
            for option in self.options:
                option.render(self.screen)

            # draws the decks
            self.deck.render()

            # draws the number of remaining chars
            self.render_remaining_chars()

            # checks if CPU is playing
            self.check_sleep()

        # limit to 60 frames per second
        self.clock.tick(60)

        # go ahead and update the screen with what we've drawn
        pygame.display.flip()



    def on_destroy(self):
        print("destroy new_game view")

        # call nested views on_destroy
        self.score_board.on_destroy()
        self.board.on_destroy()
        self.deck.on_destroy()

        for option in self.options:
            self.event_manager.remove(ClickEvent, option)

    def check_sleep(self):
        if self.render_sleep > 0:
            self.render_sleep += 1

            if self.render_sleep > 3 and not self.game_finished:
                pygame.time.delay(1000)
                self.render_sleep = 0
                self.board.clear()
                self.deck.clear()
                self.flip_players()
                self.playing = False

                if self.set_deck() is None:
                    return self.end_game()

    def render_remaining_chars(self):
        rem_chars_render = self.std_font.render("remaining: " + str(self.bag.remaining_chars()), 1, (255, 255, 255))
        self.screen.blit(rem_chars_render, (config.SCREEN_W - 140, config.SCREEN_H - 100))

    def render_background(self):
        img_path = os.path.normpath(os.path.dirname(__file__) + "/../res/images/green_fabric.jpg")
        img = pygame.image.load(img_path)
        self.screen.fill(config.BLACK)
        for x in range(0, config.SCREEN_W, img.get_rect().width):
            for y in range(0, config.SCREEN_H, img.get_rect().height):
                self.screen.blit(img, (x, y))
