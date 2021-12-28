import pygame
from sys import exit

# in this game first you have to choose the living cells by left clicking after you are done press enter
# if you want to delete living cells you can do it by right clicking
# if you press r you reset the game completely but if you press a you can append some cells
# if you press q you close the game
pygame.init()

# n, m, ticks and pixel_size can be changed
n, m = 50, 80
pixel_size = 20
bg_color = (0, 0, 0)
game_ticks = 10
event_ticks = 60
active_ticks = event_ticks
living_cell_color = (255, 255, 255)
# 0 is a dead cell and 1 is a living cell
array = [[0 for j in range(m)] for i in range(n)]
living_cells = {}

screen = pygame.display.set_mode((m * pixel_size, n * pixel_size))
pygame.display.set_caption("Game of Life")
finished = False
clicking = False


def check_events():
    global clicking, array, living_cells, finished, active_ticks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                clicking = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not clicking:
                finished = True
                active_ticks = game_ticks
            elif event.key == pygame.K_q:
                exit()
            elif event.key == pygame.K_r:
                clicking = False
                finished = False
                array = [[0 for j in range(m)] for i in range(n)]
                living_cells = {}
                active_ticks = event_ticks
            elif event.key == pygame.K_a:
                clicking = False
                finished = False
                active_ticks = event_ticks
    if not finished:
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // pixel_size
            y = mouse_pos[1] // pixel_size
            array[y][x] = 1
            living_cells[f"""{y}, {x}"""] = [y, x]
            clicking = True
        elif pygame.mouse.get_pressed(num_buttons=3)[2]:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // pixel_size
            y = mouse_pos[1] // pixel_size
            if f"""{y}, {x}""" in living_cells:
                array[y][x] = 0
                del living_cells[f"""{y}, {x}"""]
            clicking = True


def update_screen():
    global screen
    screen.fill(bg_color)
    # drawing living cells
    for key in living_cells.keys():
        pygame.draw.rect(screen, living_cell_color,
                         pygame.Rect(living_cells[key][1] * pixel_size, living_cells[key][0] * pixel_size,
                                     pixel_size, pixel_size))

    pygame.display.update()


def alive_neighbors(y, x):
    count = 0
    if y > 0:
        if array[y - 1][x] == 1:
            count += 1
        if x > 0:
            if array[y - 1][x - 1] == 1:
                count += 1
            if array[y][x - 1] == 1:
                count += 1
        if x < m - 1:
            if array[y - 1][x + 1] == 1:
                count += 1
            if array[y][x + 1] == 1:
                count += 1
    if y < n - 1:
        if array[y + 1][x] == 1:
            count += 1
        if x > 0:
            if array[y + 1][x - 1] == 1:
                count += 1
        if x < m - 1:
            if array[y + 1][x + 1] == 1:
                count += 1
    return count


def dead_neighbors():
    d_cells = {}
    for value in living_cells.values():
        y = value[0]
        x = value[1]
        if y > 0:
            if array[y - 1][x] == 0:
                d_cells[f"""{y - 1}, {x}"""] = [y - 1, x]
            if x > 0:
                if array[y - 1][x - 1] == 0:
                    d_cells[f"""{y - 1}, {x - 1}"""] = [y - 1, x - 1]
                if array[y][x - 1] == 0:
                    d_cells[f"""{y}, {x - 1}"""] = [y, x - 1]
            if x < m - 1:
                if array[y - 1][x + 1] == 0:
                    d_cells[f"""{y - 1}, {x + 1}"""] = [y - 1, x + 1]
                if array[y][x + 1] == 0:
                    d_cells[f"""{y}, {x + 1}"""] = [y, x + 1]
        if y < n - 1:
            if array[y + 1][x] == 0:
                d_cells[f"""{y  + 1}, {x}"""] = [y + 1, x]
            if x > 0:
                if array[y + 1][x - 1] == 0:
                    d_cells[f"""{y + 1}, {x - 1}"""] = [y + 1, x - 1]
            if x < m - 1:
                if array[y + 1][x + 1] == 0:
                    d_cells[f"""{y + 1}, {x + 1}"""] = [y + 1, x + 1]
    return d_cells


def game_of_life_simulation():
    global array, living_cells
    if finished:
        new_living_cells = {}
        dead_cells = []
        for value in living_cells.values():
            num_alive = alive_neighbors(value[0], value[1])
            if num_alive == 2 or num_alive == 3:
                new_living_cells[f"""{value[0]}, {value[1]}"""] = value
            else:
                dead_cells.append(value)
        d_neighbors = dead_neighbors()
        for value in d_neighbors.values():
            num_alive = alive_neighbors(value[0], value[1])
            if num_alive == 3:
                new_living_cells[f"""{value[0]}, {value[1]}"""] = value
        for cell in dead_cells:
            array[cell[0]][cell[1]] = 0
        for value in new_living_cells.values():
            array[value[0]][value[1]] = 1
        living_cells = new_living_cells


clock = pygame.time.Clock()
while True:
    clock.tick(active_ticks)
    check_events()
    game_of_life_simulation()
    update_screen()
