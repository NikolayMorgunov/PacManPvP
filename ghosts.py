import random
from abstracts_class import AbstractAlive
from consts import GHOST_MOVE_SPEED


class Ghost(AbstractAlive):
    def __init__(self, screen, x, y, image_name, course=1):
        super().__init__(screen, x, y, course, image_name, GHOST_MOVE_SPEED)
        self.x_home = x
        self.y_home = y
        self.is_scared = False
        self.running_home = False
        self.width = 54
        self.height = 30
        self.target_brick = (0, 0)

    def draw(self):
        super().draw(self.image)

    def die(self):
        self.running_home = True

    def choose_dir(self):

        posible_turns = []

        if self.course != 3:
            if (self.x, self.y - 1) not in self.walls:
                posible_turns.append(((self.x, self.y - 1), 1))
        if self.course != 4:
            if (self.x - 1, self.y) not in self.walls:
                posible_turns.append((((self.x - 1) % self.width, self.y), 2))
        if self.course != 1:
            if (self.x, self.y + 1) not in self.walls:
                posible_turns.append(((self.x, self.y + 1), 3))
        if self.course != 2:
            if (self.x + 1, self.y) not in self.walls:
                posible_turns.append((((self.x + 1) % self.width, self.y), 4))

        self.course = random.choice(posible_turns)[1]

    def get_coords(self):
        return super().get_coords()

    def collision(self, pacman1, pacman2):

        if pacman1.get_coords() == (self.x, self.y):
            if self.is_scared:
                self.running_home = True
            else:
                pacman1.die()
        if pacman2.get_coords() == (self.x, self.y):
            if self.is_scared:
                self.running_home = True
            else:
                pacman2.die()

    def is_home(self):
        if self.x == self.x_home and self.y == self.y_home:
            self.is_scared = False
            self.running_home = False

    def move(self):
        super().move()
        self.set_coords(self.x, self.y)


class RedBlinky(Ghost):
    pass


class PinkPinky(Ghost):
    pass


class OrangeBlinky(Ghost):
    pass


class BlueInky(Ghost):
    pass
