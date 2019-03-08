from abstracts_class import AbstractAlive
from consts import BOOST_COST, EAT_COST


class PacMan(AbstractAlive):
    def __init__(self, screen, x, y, image_name, course=4):
        super().__init__(screen, x, y, course, image_name)
        self.is_boosted = False
        self.score = 0
        self.hp = 3

    def move(self, eats, boosts):
        super().move()
        coords = self.x, self.y

        if coords in eats:
            eats.remove(coords)
            self.score += EAT_COST

        elif coords in boosts:
            boosts.remove(coords)
            self.is_boosted = True
            self.score += BOOST_COST

        return eats, boosts

    def die(self):
        self.hp -= 1
        return bool(self.hp)
