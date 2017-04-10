class Board:
    def __init__(self, row=20, col=20):
        self.row = row
        self.col = col
        self.grid = []

    def init_grid(self):
        self.grid = [[0 for x in range(self.row)] for y in range(self.col)]

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
