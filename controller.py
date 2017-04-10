import pygame

import bag
import board
import deck
import config
import event_manager


class Controller(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.event_manager = event_manager.EventManager()
        self.font = pygame.font.Font(None, 24)
        self.board = board.Board(self.screen, 15, 15)
        self.deckA = deck.Deck(self.screen, 100, 730)
        self.bag = bag.Bag()

        # set event handlers
        self.event_manager.on(pygame.MOUSEBUTTONDOWN, self.on_click_handler)
        self.event_manager.on_key_down(pygame.K_SPACE, self.on_press_space)

    def start_screen(self):
        self.board.init_grid()
        self.deckA.init_deck()
        self.bag.init_bag()

        screen = pygame.display.set_mode(config.WINDOW_SIZE)

        done = False
        display_start_screen = True

        while not done and display_start_screen:
            done = self.event_manager.check()

            # clears the screen
            screen.fill(config.BLACK)

            # draws the board
            self.board.render()

            # draws the decks
            self.deckA.render()

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def on_click_handler(self, event):
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (config.WIDTH + config.MARGIN)
        row = pos[1] // (config.HEIGHT + config.MARGIN)

        print("Click ", pos, "Grid coordinates: ", row, column)

    def on_press_space(self, event):

        for i in range(self.deckA.tiles_number):
            deck_tile = self.deckA.tiles[i]
            letter, letter_value = self.bag.get_letter()
            if deck_tile.is_empty():
                deck_tile.put_letter(letter, letter_value, 1)
            else:
                deck_tile.empty()
