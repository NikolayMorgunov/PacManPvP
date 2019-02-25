import pygame
from consts import *
from ghosts import RedBlinky
from pacman import PacMan


def draw(coords, image_name):
    x, y = coords
    image = pygame.image.load(image_name).convert_alpha()
    rect = image.get_rect(center=(x * CELL_SIZE - CELL_SIZE // 2,
                                  y * CELL_SIZE - CELL_SIZE // 2))
    sc.blit(image, rect)


pacman1 = PacMan()  # Добавить требующиеся аргументы
pacman2 = PacMan()
red1 = RedBlinky()
red2 = RedBlinky()
blue1 = None  # Заменить None на соотвтствующие классы
blue2 = None
purple1 = None
purple2 = None
orange1 = None
orange2 = None

pygame.init()
sc = pygame.display.set_mode((WIGHT, HEIGHT))

clock = pygame.time.Clock()

is_game_over = False
is_restart = False

ghosts = [red1, red2, blue1, blue2, purple1, purple2, orange1, orange2]
walls = []
eats = []
boosts = []
turns = []

while not is_game_over:

    for wall in walls:
        draw(wall, None)  # Заменить None на имя png изображения

    for eat in eats:
        draw(eat, None)

    for boost in boosts:
        draw(boost, None)

    for event in pygame.event:

        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if pygame.K_DOWN:
                pacman2.move(3, walls)

            if pygame.K_LEFT:
                pacman2.move(4, walls)

            if pygame.K_UP:
                pacman2.move(1, walls)

            if pygame.K_RIGHT:
                pacman2.move(2, walls)

            if pygame.K_s:
                pacman1.move(3, walls)

            if pygame.K_a:
                pacman1.move(4, walls)

            if pygame.K_w:
                pacman1.move(1, walls)

            if pygame.K_d:
                pacman1.move(2, walls)

    for ghost in ghosts:
        pos = ghost.x, ghosts.y
        if pos in turns:
            # Сдесь должен быть метод вычисляющий для призрака новый путь
            pass

        if pos == pacman1:

            if not pacman1.die():
                is_game_over = True
                winner = 1

            is_restart = True

        if pos == pacman2:

            if not pacman2.die():

                if is_game_over:
                    winner = 0

                else:
                    is_game_over = True
                    winner = 2

            else:
                is_restart = True

        ghost.move(None, walls)  # За место None вычислить направление
        ghost.draw()

    pacman1.draw()
    pacman2.draw()
    clock.tick(FPS)
    sc.flip()
