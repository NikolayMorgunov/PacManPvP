import pygame
from consts import *
from ghosts import RedBlinky, BlueInky, OrangeBlinky, PinkPinky
from pacman import PacMan


def draw(coords, image):
    x, y = coords

    rect = image.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2,
                                  y * CELL_SIZE + CELL_SIZE // 2))
    sc.blit(image, rect)


def write_map(file_name):

    with open(file_name) as inp:
        text = inp.read().split('\n')

        for line_num, line in enumerate(text):

            for symbol_num, symbol in enumerate(line):
                coord = (symbol_num, line_num)

                if symbol == WALL_SYMBOL:
                    walls.append(coord)

                elif symbol == EAT_SYMBOL:
                    eats.append(coord)

                elif symbol == BOOST_SYMBOL:
                    boosts.append(coord)


def scared_ghost(pacman):
    x, y = pacman.x, pacman.y

    for phantom in sorted(ghosts, key=lambda specter: (specter.scared,
                                                       abs(x - specter.x) ** 2 + abs(y - specter.y) ** 2))[:4]:
        phantom.scared = True


pygame.init()
sc = pygame.display.set_mode((WIGHT, HEIGHT))

pacman1 = PacMan(sc, 47, 4, 'pac-man.png')
pacman2 = PacMan(sc, 4, 27, 'pac-man.png', 2)
red1 = RedBlinky(sc, 5, 4, 'ghost.png')
red2 = RedBlinky(sc, 45, 26, 'ghost.png')
blue1 = BlueInky(sc, 6, 4, 'ghost.png')
blue2 = BlueInky(sc, 46, 26, 'ghost.png')
purple1 = PinkPinky(sc, 7, 4, 'ghost.png')
purple2 = PinkPinky(sc, 47, 26, 'ghost.png')
orange1 = OrangeBlinky(sc, 8, 4, 'ghost.png')
orange2 = OrangeBlinky(sc, 48, 26, 'ghost.png')

wall_image = pygame.transform.scale(pygame.image.load('wall.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
wall_image.set_colorkey((255, 255, 255))
eat_image = pygame.transform.scale(pygame.image.load('eat.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
eat_image.set_colorkey((255, 255, 255))
boost_image = pygame.transform.scale(pygame.image.load('boost.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
boost_image.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()

is_game_over = False
is_restart = False

ghosts = [red1, red2, blue1, blue2, purple1, purple2, orange1, orange2]
walls = []
eats = []
boosts = []
turns = []

next_pacman1_course = 4
next_pacman2_course = 2

write_map('map.txt')

total_fps = 0
while not is_game_over:
    total_fps += 1

    sc.fill((0, 0, 0))

    for wall in walls:
        draw(wall, wall_image)  # Заменить None на имя png изображения

    for eat in eats:
        draw(eat, eat_image)

    for boost in boosts:
        draw(boost, boost_image)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:

                if pacman1.can_move(3, walls):
                    pacman1.course = 3

                next_pacman1_course = 3

                print('down')

            elif event.key == pygame.K_LEFT:

                if pacman1.can_move(2, walls):
                    pacman1.course = 2

                next_pacman1_course = 2

                print('left')

            elif event.key == pygame.K_UP:

                if pacman1.can_move(1, walls):
                    pacman1.course = 1

                next_pacman1_course = 1

                print('up')

            elif event.key == pygame.K_RIGHT:

                if pacman1.can_move(4, walls):
                    pacman1.course = 4

                next_pacman1_course = 4

            elif event.key == pygame.K_s:

                if pacman2.can_move(3, walls):
                    pacman2.course = 3

                next_pacman2_course = 3

            elif event.key == pygame.K_a:

                if pacman2.can_move(2, walls):
                    pacman2.course = 2

                next_pacman2_course = 2

            elif event.key == pygame.K_w:

                if pacman2.can_move(1, walls):
                    pacman2.course = 1

                next_pacman2_course = 1

            elif event.key == pygame.K_d:

                if pacman2.can_move(4, walls):
                    pacman2.course = 4

                next_pacman2_course = 4

    if total_fps >= FPS // 4:
        total_fps = 0

        if pacman1.can_move(next_pacman1_course, walls):
            pacman1.course = next_pacman1_course

        if pacman2.can_move(next_pacman2_course, walls):
            pacman2.course = next_pacman2_course

        eats, boosts = pacman1.move(walls, eats, boosts)
        eats, boosts = pacman2.move(walls, eats, boosts)

    for pac in [pacman1, pacman2]:

        if pac.is_boosted:
            scared_ghost(pac)

    for ghost in ghosts:
        pos = ghost.x, ghost.y

        if pos in turns:
            # Сдесь должен быть метод вычисляющий для призрака новый путь
            pass

        ghost.move(1, walls)  # За место 1 вычислить направление

        pos = ghost.x, ghost.y

        if pos == pacman1:

            if ghost.scared:
                ghost.die()

            else:

                if not pacman1.die():
                    is_game_over = True
                    winner = 1

                is_restart = True

        if pos == pacman2:

            if ghost.scared:
                ghost.die()

            else:
                if not pacman2.die():

                    if is_game_over:
                        winner = 0

                    else:
                        is_game_over = True
                        winner = 2

                else:
                    is_restart = True

        ghost.draw()

    pacman1.draw()
    pacman2.draw()
    pygame.display.flip()
    clock.tick(FPS)
