import pygame
from consts import *
from ghosts import RedBlinky, BlueInky, OrangeBlinky, PinkPinky
from pacman import PacMan


def draw(screen, coords, image):
    x, y = coords

    rect = image.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2 + SPACE,
                                  y * CELL_SIZE + CELL_SIZE // 2 + SPACE))
    screen.blit(image, rect)


def draw_text(screen, text, coord, size=25, color=(255, 255, 255)):
    text_surf = pygame.font.Font(None, size).render(text,
                                                    True, color)
    screen.blit(text_surf, coord)


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

    for phantom in sorted(ghosts, key=lambda specter: (specter.is_scared,
                                                       abs(x - specter.x) ** 2 + abs(y - specter.y) ** 2))[:4]:
        phantom.is_scared = True


def is_touch(obj1, obj2):
    x1, y1 = obj1.rect[:2]
    x2, y2 = obj2.rect[:2]

    if y1 == y2 and (x2 <= x1 <= x2 + CELL_SIZE or x1 <= x2 <= x1 + CELL_SIZE):
        return True

    elif x1 == x2 and (y2 <= y1 <= y2 + CELL_SIZE or y1 <= y2 <= y1 + CELL_SIZE):
        return True

    return False


pygame.init()
sc = pygame.display.set_mode((WIGHT, HEIGHT))

end_image = pygame.image.load('image/end.png').convert_alpha()

pacman1 = PacMan(sc, 4, 27, IMAGE_NAME_PACMAN_1, 2)
pacman2 = PacMan(sc, 47, 4, IMAGE_NAME_PACMAN_2)
red1 = RedBlinky(sc, 5, 4, IMAGE_NAME_RED_GHOST_1)
red2 = RedBlinky(sc, 45, 27, IMAGE_NAME_RED_GHOST_2)
blue1 = BlueInky(sc, 6, 4, IMAGE_NAME_BLUE_GHOST_1)
blue2 = BlueInky(sc, 46, 27, IMAGE_NAME_BLUE_GHOST_2)
pink1 = PinkPinky(sc, 7, 4, IMAGE_NAME_PINK_GHOST_1)
pink2 = PinkPinky(sc, 47, 27, IMAGE_NAME_PINK_GHOST_2)
orange1 = OrangeBlinky(sc, 8, 4, IMAGE_NAME_ORANGE_GHOST_1)
orange2 = OrangeBlinky(sc, 48, 27, IMAGE_NAME_ORANGE_GHOST_2)

pacman1.hp_coord = [0, SPACE]
pacman2.hp_coord = [CELL_SIZE * CELL_WIGHT + SPACE, SPACE]

wall_image = pygame.transform.scale(pygame.image.load('image/wall.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
eat_image = pygame.transform.scale(pygame.image.load('image/eat.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
boost_image = pygame.transform.scale(pygame.image.load('image/boost.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))

clock = pygame.time.Clock()

is_game_over = False
is_restart = False
is_end = False

ghosts = [red1, red2, blue1, blue2, orange1, orange2, pink1, pink2]
walls = []
eats = []
boosts = []
# wall_turn_to_right = [(0, 0), (2, 2), (10, 2), (13, 2), (42, 2), (45, 2)]
next_pacman1_course = 4
next_pacman2_course = 2
total_fps = 0
time = 0

write_map('map.txt')

pacman2.set_walls(walls)
pacman1.set_walls(walls)

for ghost in ghosts:
    ghost.set_walls(walls)

while not is_end:

    while not is_game_over:
        time += clock.tick()
        total_fps += 1
        sc.fill((0, 0, 0))

        draw_text(sc, f'Pac-Man 1   Score: {pacman1.score}', [SPACE, SPACE // 3])
        draw_text(sc, f'Pac-Man 2   Score: {pacman2.score}', [(CELL_WIGHT - 8) * CELL_SIZE, SPACE // 3])
        pacman1.draw_hp()
        pacman2.draw_hp()

        if is_restart:
            is_restart = False
            pacman2.set_coords(47, 4)
            pacman2.course = 4
            pacman1.set_coords(4, 27)
            pacman1.course = 2
            red1.set_coords(5, 4)
            red2.set_coords(45, 27)
            blue1.set_coords(6, 4)
            blue2.set_coords(46, 27)
            pink1.set_coords(7, 4)
            pink2.set_coords(47, 27)
            orange1.set_coords(8, 4)
            orange2.set_coords(48, 27)
            time = 0
            continue

        for wall in walls:
            draw(sc, wall, wall_image)

        for eat in eats:
            draw(sc, eat, eat_image)

        for boost in boosts:
            draw(sc, boost, boost_image)

        if not eats:
            is_game_over = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:

                    if pacman2.can_move(3):
                        pacman2.course = 3

                    next_pacman1_course = 3

                elif event.key == pygame.K_LEFT:

                    if pacman2.can_move(2):
                        pacman2.course = 2

                    next_pacman1_course = 2

                elif event.key == pygame.K_UP:

                    if pacman2.can_move(1):
                        pacman2.course = 1

                    next_pacman1_course = 1

                elif event.key == pygame.K_RIGHT:

                    if pacman2.can_move(4):
                        pacman2.course = 4

                    next_pacman1_course = 4

                elif event.key == pygame.K_s:

                    if pacman1.can_move(3):
                        pacman1.course = 3

                    next_pacman2_course = 3

                elif event.key == pygame.K_a:

                    if pacman1.can_move(2):
                        pacman1.course = 2

                    next_pacman2_course = 2

                elif event.key == pygame.K_w:

                    if pacman1.can_move(1):
                        pacman1.course = 1

                    next_pacman2_course = 1

                elif event.key == pygame.K_d:

                    if pacman1.can_move(4):
                        pacman1.course = 4

                    next_pacman2_course = 4

                elif event.key == pygame.K_i:
                    print(pacman1.get_coords())
                    print(eats)

        if total_fps >= FPS // 3:
            for ghost in ghosts:
                ghost.choose_dir()
                ghost.move()

            total_fps = 0
            pacman1.image_index += 1
            pacman1.image_index %= 4
            pacman2.image_index += 1
            pacman2.image_index %= 4

            if pacman2.can_move(next_pacman1_course):
                pacman2.course = next_pacman1_course

            if pacman1.can_move(next_pacman2_course):
                pacman1.course = next_pacman2_course

            eats, boosts = pacman2.move(eats, boosts)
            eats, boosts = pacman1.move(eats, boosts)

        elif not total_fps % (FPS // 5):
            pacman1.image_index += 1
            pacman1.image_index %= 4
            pacman2.image_index += 1
            pacman2.image_index %= 4

        for pac in [pacman2, pacman1]:

            if pac.is_boosted:
                pac.is_boosted = False
                scared_ghost(pac)

        pacman2.draw()
        pacman1.draw()

        if is_touch(pacman2, pacman1):

            if pacman2.score > pacman1.score:

                if pacman1.die():
                    is_restart = True

                else:
                    is_game_over = True
                    winner = 1

                continue

            elif pacman2.score < pacman1.score:

                if pacman2.die():
                    is_restart = True

                else:
                    is_game_over = True
                    winner = 2

                continue

        for ghost in ghosts:

            if is_touch(ghost, pacman2):
                print(2)
                # if ghost.is_scared:
                #     ghost.die()
                #
                # else:

                if not pacman2.die():
                    is_game_over = True
                    winner = 1

                is_restart = True

            elif is_touch(ghost, pacman1):
                print(1)
                # if ghost.is_scared:
                #     ghost.die()
                #
                # else:

                if not pacman1.die():

                    if is_game_over:
                        winner = 0

                    else:
                        is_game_over = True
                        winner = 2

                else:
                    is_restart = True

            ghost.draw()

        time %= 250
        pygame.display.flip()

    if pacman1.hp == pacman2.hp:
        if pacman1.score == pacman2.score:
            winner = 0

        elif pacman1.score > pacman2.score:
            winner = 1

        else:
            winner = 2

    elif pacman1.hp > pacman2.hp:
        winner = 1

    else:
        winner = 2

    clock.tick(FPS)

    sc.blit(end_image, (0, 0, 1240, 760))

    if winner:
        win_text = f'Победил игрок {winner}'

    else:
        win_text = 'Ничья'

    fontObj = pygame.font.Font('freesansbold.ttf', 50)

    textSurfaceObj = fontObj.render(win_text, True,
                                    pygame.Color('yellow' if winner == 1 else
                                                 'green' if winner == 2 else
                                                 'white'))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIGHT - 250, 40)

    sc.blit(textSurfaceObj, textRectObj)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                pacman1.score = pacman2.score = 0
                is_restart = False
                is_game_over = False
                pacman2.set_coords(47, 4)
                pacman2.course = 4
                pacman2.hp = MAX_HP
                pacman1.set_coords(4, 27)
                pacman1.course = 2
                pacman1.hp = MAX_HP
                red1.set_coords(5, 4)
                red2.set_coords(45, 27)
                blue1.set_coords(6, 4)
                blue2.set_coords(46, 27)
                pink1.set_coords(7, 4)
                pink2.set_coords(47, 27)
                orange1.set_coords(8, 4)
                orange2.set_coords(48, 27)
                time = 0
                ghosts = [red1, red2, blue1, blue2, orange1, orange2, pink1, pink2]
                walls = []
                eats = []
                boosts = []
                write_map('map.txt')
