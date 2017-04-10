import pygame

import board
import config


class Controller(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.board = board.Board(15, 15)

    def start_screen(self):
        self.board.init_grid()

        screen = pygame.display.set_mode(config.WINDOW_SIZE)

        done = False
        display_start_screen = True

        while done == False and display_start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (config.WIDTH + config.MARGIN)
                    row = pos[1] // (config.HEIGHT + config.MARGIN)

                    print("Click ", pos, "Grid coordinates: ", row, column)

            screen.fill(config.BLACK)

            self.draw_grid(screen)

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def draw_grid(self, screen):

        # Draw the grid
        for row in range(self.board.get_row()):
            for column in range(self.board.get_row()):
                color = config.WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(config.MARGIN + config.WIDTH) * column + config.MARGIN,
                                  (config.MARGIN + config.HEIGHT) * row + config.MARGIN,
                                  config.WIDTH,
                                  config.HEIGHT])
