from abstracts_class import AbstractAlive


class PacMan(AbstractAlive):
    def __init__(self, screen, x, y, course=4):
        super().__init__(screen, x, y, course, 'pac-man.png')
        self.is_boosted = False
        self.score = 0
        self.hp = 3

    def get_coords(self):
        return super().get_coords()

    def move(self, course, walls, eats, boosts):
        super().move(course, walls)
        self.course = course
        coords = self.x, self.y

        if coords in eats:
            eats.remove(coords)

        elif coords in boosts:
            boosts.remove(coords)
            self.is_boosted = True

        return eats, boosts

    def die(self):
        self.hp -= 1
        return bool(self.hp)
