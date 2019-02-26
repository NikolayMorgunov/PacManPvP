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

    def die(self):
        self.running_home = True

    def get_coords(self):
        return super().get_coords()

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

    def draw(self):
        super().draw()

    def move(self, course, walls):
        super().move(course, walls)


class RedBlinky(Ghost):
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

    def chose_target_brick(self, pac_coords_1, pac_coords_2, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
        else:
            self.target_brick = (self.width - 1, 0)


class PinkPinky(Ghost):
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

    def chose_target_brick(self, pac_coords_1, pac_coords_2, pacman_dir, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
            self.target_brick = ((self.target_brick[0] + pacman_dir[0] * 4), (self.target_brick[0] + pacman_dir[0] * 4))

        else:
            self.target_brick = (0, 0)


class OrangeBlinky(Ghost):
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

    def chose_target_brick(self, pac_coords_1, pac_coords_2, pacman_dir, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)

            if ((self.x - self.target_brick[0]) ** 2 + (self.y - self.target_brick[1]) ** 2) <= 16:
                self.target_brick = (0, self.highth - 1)

        else:
            self.target_brick = (0, 0)


class BlueInky(Ghost):
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

    def chose_target_brick(self, pac_coords_1, pac_coords_2, pacman_dir, time):
        if self.what_to_do(time):
            self.target_brick = self.choose_pac_target(pac_coords_1, pac_coords_2)
            self.target_brick = ((self.target_brick[0] + pacman_dir[0] * 2), (self.target_brick[0] + pacman_dir[0] * 2))

        else:
            self.target_brick = (self.width - 1, self.highth - 1)  # ещё не готово!!!
