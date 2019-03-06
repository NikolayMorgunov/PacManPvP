import random
from abstracts_class import AbstractAlive


class Ghost(AbstractAlive):
    def __init__(self, screen, x, y, image_name, course=1):
        super().__init__(screen, x, y, course, image_name)
        self.x_home = x
        self.y_home = y
        self.scared = False
        self.running_home = False
        self.width = 54
        self.height = 30
        self.target_brick = (0, 0)

    def die(self):
        self.running_home = True

    def choose_dir(self):
        print(self.x, self.y)
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

        if not self.scared:
            tuple_dir = min(posible_turns,
                        key=lambda x: (x[0][0] - self.target_brick[0]) ** 2 + (x[0][1] - self.target_brick[1]) ** 2)
            self.course = tuple_dir[1]
        else:
            self.course = random.choice(posible_turns)[1]

    def get_coords(self):
        return super().get_coords()

    def get_target_brick(self):
        return self.target_brick

    def choose_pac_target(self, pac_coords_1, pac_coords_2):
        dist_to_pac_1 = (pac_coords_1[0] - self.x) ** 2 + (pac_coords_1[1] - self.y) ** 2
        dist_to_pac_2 = (pac_coords_2[0] - self.x) ** 2 + (pac_coords_2[1] - self.y) ** 2
        if dist_to_pac_1 > dist_to_pac_2:
            return pac_coords_2

        elif dist_to_pac_1 < dist_to_pac_2:
            return pac_coords_1
        else:
            return random.choice[pac_coords_1, pac_coords_2]

    def collision(self, pac_coords_x, pac_coords_y):
        pacman_killed = True
        if pac_coords_x == self.x and pac_coords_y == self.y:
            if self.scared:
                self.running_home = True
                pacman_killed = False
        return pacman_killed

    def is_home(self):
        if self.x == self.x_home and self.y == self.y_home:
            self.scared = False
            self.running_home = False

    def what_to_do(self, time):
        first_scatter = 7000
        first_chase = 20000
        second_scatter = 7000
        second_chase = 20000
        third_scatter = 5000
        third_chase = 20000
        fourth_scatter = 5000

        if time <= first_scatter or (
                first_scatter + first_chase
        ) < time <= (
                first_scatter + first_chase + second_scatter
        ) or (
                first_scatter + first_chase + second_scatter + second_chase
        ) < time <= (
                first_scatter + first_chase + second_scatter + second_chase + third_scatter
        ) or (
                first_scatter + first_chase + second_scatter + second_chase + third_scatter + third_chase
        ) < time <= (
                first_scatter + first_chase + second_scatter + second_chase + third_scatter +
                third_chase + fourth_scatter):
            return False

        else:
            return True


class RedBlinky(Ghost):
    def chose_target_brick(self, pac_coords_1, pac_coords_2, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
        else:
            self.target_brick = (self.width - 1, 0)


class PinkPinky(Ghost):
    def chose_target_brick(self, pac_coords_1, pac_coords_2, time):
        pacman_dir = sorted([pac_coords_1, pac_coords_2],
                            key=lambda specter: abs(self.x - specter[0]) ** 2 + abs(self.y - specter[1]) ** 2)
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
            self.target_brick = ((self.target_brick[0] + pacman_dir[0] * 4),
                                 (self.target_brick[0] + pacman_dir[0] * 4))

        else:
            self.target_brick = (0, 0)


class OrangeBlinky(Ghost):
    def chose_target_brick(self, pac_coords_1, pac_coords_2, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)

            if ((self.x - self.target_brick[0]) ** 2 + (self.y - self.target_brick[1]) ** 2) <= 16:
                self.target_brick = (0, self.height - 1)
        else:
            self.target_brick = (0, 0)


class BlueInky(Ghost):
    def chose_target_brick(self, pac_coords_1, pac_coords_2, time, red):
        pacman_dir = sorted([pac_coords_1, pac_coords_2],
                            key=lambda specter: abs(self.x - specter[0]) ** 2 + abs(self.y - specter[1]) ** 2)
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
            self.target_brick = ((2 * (self.target_brick[0] + pacman_dir[0] * 2) - red.x),
                                 (2 * (self.target_brick[1] + pacman_dir[1] * 2) - red.y))
        else:
            self.target_brick = (self.width - 1, self.height - 1)
