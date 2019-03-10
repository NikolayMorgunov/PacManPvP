from abstracts_class import AbstractAlive
from consts import BOOST_COST, EAT_COST, MAX_HP, IMAGE_LIVING_HEART, IMAGE_DEAD_HEART
import pygame


class PacMan(AbstractAlive):
    def __init__(self, screen, x, y, image_name, course=4):
        super().__init__(screen, x, y, course, image_name)
        self.is_boosted = False
        self.score = 0
        self.hp = MAX_HP
        self.hp_coord = (0, 0)
        self.image_living_heart = pygame.image.load(IMAGE_LIVING_HEART).convert_alpha()
        self.image_dead_heart = pygame.image.load(IMAGE_DEAD_HEART).convert_alpha()

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

    def draw(self):
        image = pygame.transform.rotate(self.image, 90 * self.course)
        super().draw(image)

    def draw_hp(self):

        for index_heart in range(self.hp):
            # if index_heart < self.hp:
            self.sc.blit(self.image_living_heart,
                         (self.hp_coord[0], self.hp_coord[1] + index_heart * 20))
            #
            # else:
            #     self.sc.blit(self.image_dead_heart,
            #                  (self.hp_coord[0], self.hp_coord[1] + index_heart * 20))
