import pygame
from consts import *
from ghosts import RedBlinky, BlueInky, OrangeBlinky, PinkPinky
from pacman import PacMan


def draw(coords, image_name):
    x, y = coords
    image = pygame.transform.scale(pygame.image.load(image_name).convert_alpha(), (CELL_SIZE, CELL_SIZE))
    image.set_colorkey((255, 255, 255))
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


pygame.init()
sc = pygame.display.set_mode((WIGHT, HEIGHT))

pacman1 = PacMan(sc, 4, 27, 2)
pacman2 = PacMan(sc, 47, 4)
red1 = RedBlinky(sc, 5, 4, 'ghost.png')
red2 = RedBlinky(sc, 45, 26, 'ghost.png')
blue1 = BlueInky(sc, 6, 4, 'ghost.png')
blue2 = BlueInky(sc, 46, 26, 'ghost.png')
purple1 = PinkPinky(sc, 7, 4, 'ghost.png')
purple2 = PinkPinky(sc, 47, 26, 'ghost.png')
orange1 = OrangeBlinky(sc, 8, 4, 'ghost.png')
orange2 = OrangeBlinky(sc, 48, 26, 'ghost.png')

clock = pygame.time.Clock()

is_game_over = False
is_restart = False

ghosts = [red1, red2, blue1, blue2, purple1, purple2, orange1, orange2]
walls = []
eats = []
boosts = []
turns = []

write_map('map.txt')

while not is_game_over:
    sc.fill((0, 0, 0))

    # for wall in walls:
    #     draw(wall, 'wall.png')  # Заменить None на имя png изображения
    #
    # for eat in eats:
    #     draw(eat, 'eat.png')

    for boost in boosts:
        draw(boost, 'boost.png')

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                eats, boosts = pacman2.move(3, walls, eats, boosts)
                print('down')

            elif event.key == pygame.K_LEFT:
                eats, boosts = pacman2.move(2, walls, eats, boosts)
                print('left')

            elif event.key == pygame.K_UP:
                eats, boosts = pacman2.move(1, walls, eats, boosts)
                print('up')

            elif event.key == pygame.K_RIGHT:
                eats, boosts = pacman2.move(4, walls, eats, boosts)
                print('right')

            elif event.key == pygame.K_s:
                eats, boosts = pacman1.move(3, walls, eats, boosts)
                print('s')

            elif event.key == pygame.K_a:
                eats, boosts = pacman1.move(2, walls, eats, boosts)
                print('a')

            elif event.key == pygame.K_w:
                eats, boosts = pacman1.move(1, walls, eats, boosts)
                print('w')

            elif event.key == pygame.K_d:
                eats, boosts = pacman1.move(4, walls, eats, boosts)
                print('d')

    for ghost in ghosts:
        pos = ghost.x, ghost.y

        # if pos in turns:
        #     # Сдесь должен быть метод вычисляющий для призрака новый путь
        #     pass
        #
        # ghost.move(1, walls)  # За место 1 вычислить направление
        #
        # pos = ghost.x, ghost.y
        #
        # if pos == pacman1:
        #
        #     if not pacman1.die():
        #         is_game_over = True
        #         winner = 1
        #
        #     is_restart = True
        #
        # if pos == pacman2:
        #
        #     if not pacman2.die():
        #
        #         if is_game_over:
        #             winner = 0
        #
        #         else:
        #             is_game_over = True
        #             winner = 2
        #
        #     else:
        #         is_restart = True

        ghost.draw()

    pacman1.draw()
    pacman2.draw()
    pygame.display.flip()
    clock.tick(FPS)
