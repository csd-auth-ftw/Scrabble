import tile
import config
import pygame


class Board:
    def __init__(self, screen, row=20, col=20):
        self.screen = screen
        self.row = row
        self.col = col
        self.grid = []

    def init_grid(self):
        for x in range(self.row):
            self.grid.append([])
            for y in range(self.col):
                left = (config.MARGIN + config.WIDTH) * x + config.MARGIN
                top = (config.MARGIN + config.HEIGHT) * y + config.MARGIN
                t = tile.Tile(self.screen, left, top, config.WIDTH, config.HEIGHT)
                self.grid[x].append(t)

    def render(self):
        # render background
        for row in range(self.row):
            for column in range(self.col):
                color = config.WHITE
                pygame.draw.rect(self.screen,
                                 color,
                                 [(config.MARGIN + config.WIDTH) * column + config.MARGIN,
                                  (config.MARGIN + config.HEIGHT) * row + config.MARGIN,
                                  config.WIDTH,
                                  config.HEIGHT])

        # render tiles
        for x in range(self.row):
            for y in range(self.col):
                self.grid[x][y].render()

    def get_grid(self):
        return self.grid

    def get_val(self, pos_x, pos_y):
        return self.grid[pos_x][pos_y]

    def set_grid(self, pos_x, pos_y, value):
        self.grid[pos_x][pos_y] = value  # TODO check for valid pos

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
