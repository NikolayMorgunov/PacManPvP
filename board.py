from consts import CELL_SIZE, CELL_WIGHT, CELL_HEIGHT


class Board:
    def __init__(self, pacmans:tuple, ghosts:tuple):
        self.wight = CELL_WIGHT
        self.height = CELL_HEIGHT
        self.cell_size = CELL_SIZE
