import pygame
from consts import CELL_SIZE
from abstract_alive import AbstractAlive


class PacMan(AbstractAlive):
    def __init__(self, screen, x, y, course=1):
        super().__init__(screen, x, y, course, 'pac-man.png')

    def get_coords(self):
        return super().get_coords()

    def draw(self):
        image = pygame.transform.rotate(self.image, 90 * self.course)
        rect = image.get_rect(center=(self.x * CELL_SIZE - CELL_SIZE // 2,
                                      self.x * CELL_SIZE - CELL_SIZE // 2))
        self.sc.blit(image, rect)

    def move(self, course):
        super().move(course)
