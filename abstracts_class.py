import pygame
from consts import CELL_SIZE


class AbstractAlive:
    def __init__(self, screen, x, y, course, image_name):
        self.x = x
        self.y = y
        self.sc = screen
        self.course = course  # 1 - up; 2 - left; 3 - down; 4 - right;
        self.image = pygame.image.load(image_name).convert_alpha()

    def get_coords(self):
        return self.x, self.y

    def draw(self):
        image = pygame.transform.rotate(self.image, 90 * self.course)
        rect = image.get_rect(center=(self.x * CELL_SIZE - CELL_SIZE // 2,
                                      self.y * CELL_SIZE - CELL_SIZE // 2))
        self.sc.blit(image, rect)

    def move(self, course, walls):
        if self.can_move(course, walls):

            if course == 1:
                self.y -= 1

            elif course == 2:
                self.x -= 1

            elif course == 3:
                self.y += 1

            elif course == 4:
                self.x += 1

            self.x %= 54
            self.y %= 30

    def can_move(self, course, walls):
        new_x, new_y = self.x, self.y

        if course == 1:
            new_y -= 1

        elif course == 2:
            new_x -= 1

        elif course == 3:
            new_y += 1

        elif course == 4:
            new_x += 1

        if (new_x, new_y) not in walls:
            return True

        return False


# class AbstractEat:
#     def __init__(self, screen, x, y, cost, image_name):
#         self.sc = screen
#         self.x = x
#         self.y = y
#         self.cost = cost
#         self.image = pygame.image.load(image_name).convert_alpha()
#
#     def draw(self):
#         rect = self.image.get_rect(center=(self.x * CELL_SIZE - CELL_SIZE // 2,
#                                            self.y * CELL_SIZE - CELL_SIZE // 2))
#         self.sc.blit(self.image, rect)