import pygame
from consts import CELL_SIZE
from abstracts_class import AbstractAlive


class PacMan(AbstractAlive):
    def __init__(self, screen, x, y, course=1):
        super().__init__(screen, x, y, course, 'pac-man.png')
        self.is_boosted = False
        self.score = 0
        self.hp = 3

    def get_coords(self):
        return super().get_coords()

    def draw(self):
        image = pygame.transform.rotate(self.image, 90 * self.course)
        rect = image.get_rect(center=(self.x * CELL_SIZE - CELL_SIZE // 2,
                                      self.x * CELL_SIZE - CELL_SIZE // 2))
        self.sc.blit(image, rect)

    def move(self, course, walls):
        super().move(course, walls)

    def die(self):
        self.hp -= 1
        return bool(self.hp)
