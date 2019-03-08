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


def is_touch_between_packmans():
    x1, y1 = pacman1.rect[:2]
    x2, y2 = pacman2.rect[:2]

    if y1 == y2 and (x2 <= x1 <= x2 + CELL_SIZE or x1 <= x2 <= x1 + CELL_SIZE):
        return True

    elif x1 == x2 and (y2 <= y1 <= y2 + CELL_SIZE or y1 <= y2 <= y1 + CELL_SIZE):
        return True

    return False


pygame.init()
sc = pygame.display.set_mode((WIGHT, HEIGHT))

pacman1 = PacMan(sc, 47, 4, IMAGE_NAME_PACMAN_1)
pacman2 = PacMan(sc, 4, 27, IMAGE_NAME_PACMAN_2, 2)
red1 = RedBlinky(sc, 5, 4, IMAGE_NAME_RED_GHOST_1)
red2 = RedBlinky(sc, 45, 26, IMAGE_NAME_RED_GHOST_2)
blue1 = BlueInky(sc, 6, 4, IMAGE_NAME_BLUE_GHOST_1)
blue2 = BlueInky(sc, 46, 26, IMAGE_NAME_BLUE_GHOST_2)
pink1 = PinkPinky(sc, 7, 4, IMAGE_NAME_PINK_GHOST_1)
pink2 = PinkPinky(sc, 47, 26, IMAGE_NAME_PINK_GHOST_2)
orange1 = OrangeBlinky(sc, 8, 4, IMAGE_NAME_ORANGE_GHOST_1)
orange2 = OrangeBlinky(sc, 48, 26, IMAGE_NAME_ORANGE_GHOST_2)

wall_image = pygame.transform.scale(pygame.image.load('wall.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
wall_image.set_colorkey((255, 255, 255))
eat_image = pygame.transform.scale(pygame.image.load('eat.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
eat_image.set_colorkey((255, 255, 255))
boost_image = pygame.transform.scale(pygame.image.load('boost.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
boost_image.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()

is_game_over = False
is_restart = False

ghosts = [red1, red2, blue1, blue2, pink1, pink2, orange1, orange2]
walls = []
eats = []
boosts = []
turns = []

next_pacman1_course = 4
next_pacman2_course = 2
total_fps = 0
time = 0

write_map('map.txt')

pacman1.set_walls(walls)
pacman2.set_walls(walls)

for ghost in ghosts:
    ghost.set_walls(walls)

while not is_game_over:
    time += clock.tick()

    if is_restart:
        is_restart = False
        pacman1.set_coords(47, 4)
        pacman1.course = 4
        pacman2.set_coords(4, 27)
        pacman2.course = 2
        red1.set_coords(5, 4)
        red2.set_coords(45, 26)
        blue1.set_coords(6, 4)
        blue2.set_coords(46, 26)
        pink1.set_coords(7, 4)
        pink2.set_coords(47, 26)
        orange1.set_coords(8, 4)
        orange2.set_coords(48, 26)
        time = 0
        continue

    sc.fill((0, 0, 0))
    total_fps += 1

    for wall in walls:
        draw(wall, wall_image)

    for eat in eats:
        draw(eat, eat_image)

    for boost in boosts:
        draw(boost, boost_image)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:

                if pacman1.can_move(3):
                    pacman1.course = 3

                next_pacman1_course = 3

                print('down')

            elif event.key == pygame.K_LEFT:

                if pacman1.can_move(2):
                    pacman1.course = 2

                next_pacman1_course = 2

                print('left')

            elif event.key == pygame.K_UP:

                if pacman1.can_move(1):
                    pacman1.course = 1

                next_pacman1_course = 1

                print('up')

            elif event.key == pygame.K_RIGHT:

                if pacman1.can_move(4):
                    pacman1.course = 4

                next_pacman1_course = 4

            elif event.key == pygame.K_s:

                if pacman2.can_move(3):
                    pacman2.course = 3

                next_pacman2_course = 3

            elif event.key == pygame.K_a:

                if pacman2.can_move(2):
                    pacman2.course = 2

                next_pacman2_course = 2

            elif event.key == pygame.K_w:

                if pacman2.can_move(1):
                    pacman2.course = 1

                next_pacman2_course = 1

            elif event.key == pygame.K_d:

                if pacman2.can_move(4):
                    pacman2.course = 4

                next_pacman2_course = 4

            elif event.key == pygame.K_i:
                print(pacman1.score, pacman2.score)

    if total_fps >= FPS // 3:
        total_fps = 0

        if pacman1.can_move(next_pacman1_course):
            pacman1.course = next_pacman1_course

        if pacman2.can_move(next_pacman2_course):
            pacman2.course = next_pacman2_course

        eats, boosts = pacman1.move(eats, boosts)
        eats, boosts = pacman2.move(eats, boosts)

    for pac in [pacman1, pacman2]:

        if pac.is_boosted:
            pac.is_boosted = False
            scared_ghost(pac)

    pacman1.draw()
    pacman2.draw()

    if is_touch_between_packmans():

        if pacman1.score > pacman2.score:

            if pacman2.die():
                is_restart = True
                print('1')
            else:
                is_game_over = True

        elif pacman1.score < pacman2.score:

            if pacman1.die():
                is_restart = True
                print('2')

            else:
                is_game_over = True

    for ghost in ghosts:
        total_way = 0
        pos = ghost.x, ghost.y
        type_of_ghost = type(ghost)

        for i in range(-1, 2):

            for j in range(-1, 2):

                if i * -1 != j and (i and j) and (pos[0] + i, pos[1] + j) in walls:
                    total_way += 1

        if total_way > 2:

            if type_of_ghost == BlueInky:
                ghost.chose_target_brick(pacman1.get_coords(), pacman2.get_coords(), time, red1.get_coords())

            else:
                ghost.chose_target_brick(pacman1.get_coords(), pacman2.get_coords(), time)

        ghost.choose_dir()
        ghost.move()

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

    pygame.display.flip()
    clock.tick(FPS)
