import random
from abstract_alive import AbstractAlive


class Ghost(AbstractAlive):
    def __init__(self, screen, x, y, image_name, course=1):
        super().__init__(screen, x, y, course, image_name)
        self.scared = False
        self.direct = (0, -1)

    def get_coords(self):
        return super().get_coords()

    def choose_pac_target(self, pac_coords_1, pac_coords_2):
        dist_to_pac_1 = (pac_coords_1[0] - self.x) ** 2 + (pac_coords_1[1] - self.y) ** 2
        dist_to_pac_2 = (pac_coords_2[0] - self.x) ** 2 + (pac_coords_2[1] - self.y) ** 2

        if dist_to_pac_1 > dist_to_pac_2:
            self.pac_target = pac_coords_2

        elif dist_to_pac_1 < dist_to_pac_2:
            self.pac_target = pac_coords_1

        else:
            self.pac_target = random.choice[pac_coords_1, pac_coords_2]

    def draw(self):
        super().draw()

    def move(self, course):
        super().move(course)
