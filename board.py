from consts import CELL_SIZE, WIGHT, HEIGHT


class Board:
    def __init__(self, pacmans:tuple, ghosts:tuple):
        self.wight = WIGHT
        self.height = HEIGHT
        self.cell_size = CELL_SIZE
