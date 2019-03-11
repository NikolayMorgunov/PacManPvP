import pygame
from consts import CELL_SIZE, CELL_WIGHT, CELL_HEIGHT, SPACE


class AbstractAlive:
    def __init__(self, screen, x, y, course, image_name, speed):
        self.x = x
        self.y = y
        self.sc = screen
        self.course = course  # 1 - up; 2 - left; 3 - down; 4 - right;
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = [x * CELL_SIZE + SPACE, y * CELL_SIZE + SPACE, CELL_SIZE, CELL_SIZE]
        self.walls = []
        self.SPEED = speed

    def set_coords(self, x, y):
        self.x, self.y = x, y
        self.rect = [x * CELL_SIZE + SPACE, y * CELL_SIZE + SPACE, CELL_SIZE, CELL_SIZE]

    def get_coords(self):
        return self.x, self.y

    def draw(self, image):

        if self.y == 14 and self.x == -1 and self.course == 2:
            self.x = CELL_WIGHT
            self.rect[0] = self.x * CELL_SIZE + SPACE
            # print(self.rect)

        elif self.y == 14 and self.x == CELL_WIGHT and self.course == 4:
            self.x = -1
            self.rect[0] = self.x * CELL_SIZE + SPACE
            # print(self.rect)
        else:

            if self.x * CELL_SIZE + SPACE > self.rect[0]:

                if self.x == CELL_WIGHT - 1 and self.course == 2:
                    self.rect[0] = self.x * CELL_SIZE + SPACE

                else:
                    self.rect[0] += self.SPEED

            elif self.x * CELL_SIZE + SPACE < self.rect[0]:

                if not self.x and self.course == 4:
                    self.rect[0] = self.x * CELL_SIZE + SPACE

                else:
                    self.rect[0] -= self.SPEED

                    if self.x * CELL_SIZE > self.rect[0]:
                        self.rect[0] = self.x * CELL_SIZE + SPACE

            if self.y * CELL_SIZE + SPACE > self.rect[1]:
                self.rect[1] += self.SPEED

            elif self.y * CELL_SIZE + SPACE < self.rect[1]:
                self.rect[1] -= self.SPEED

                if self.y * CELL_SIZE + SPACE > self.rect[1]:
                    self.rect[1] = self.y * CELL_SIZE + SPACE

        self.sc.blit(image, self.rect)

    def move(self):
        if self.can_move(self.course):
            if self.course == 1:
                self.y -= 1
            elif self.course == 2:
                self.x -= 1
            elif self.course == 3:
                self.y += 1
            elif self.course == 4:
                self.x += 1
            if self.x < 0:
                self.x += CELL_WIGHT
            elif self.x > CELL_WIGHT - 1:
                self.x = 0
            if self.y < 0:
                self.y += CELL_HEIGHT
            elif self.y > CELL_HEIGHT - 1:
                self.y = 0

    def can_move(self, course):
        new_x, new_y = self.x, self.y
        if course == 1:
            new_y -= 1
        elif course == 2:
            new_x -= 1
        elif course == 3:
            new_y += 1
        elif course == 4:
            new_x += 1
        if (new_x, new_y) in self.walls:
            return False

        return True

    def set_walls(self, walls):
        self.walls = walls
