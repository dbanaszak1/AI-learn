import pygame
from models.road import Road

BLOCK_COLOR = (11, 12, 15)
all_roads_board_one = []


def draw_road_one(WINDOW, cooridnates, block_size):
    cords_x = cooridnates.x
    cords_y = cooridnates.y

    road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, cords_y)
    road.draw()
    all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y + block_size*23, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x + block_size*18, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y - block_size*27, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x - block_size*10, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y + block_size*23, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x + block_size*20, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y - block_size*18, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x - block_size*28, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y + block_size*6, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x + block_size*24, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y + block_size*18, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x - block_size*6, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y - block_size*2, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x - block_size*6, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y - block_size*28, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y - block_size
        all_roads_board_one.append((cords_x, cords_y))

    cords_x = 50
    cords_y = 475

    for i in range(cords_x, cords_x + block_size*8, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x + block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_y, cords_y - block_size*2, -block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, cords_x, i)
        road.draw()
        cords_y = cords_y - block_size
        all_roads_board_one.append((cords_x, cords_y))

    for i in range(cords_x, cords_x + block_size*4, block_size):
        road = Road(WINDOW, BLOCK_COLOR, block_size, i, cords_y)
        road.draw()
        cords_x = cords_x + block_size
        all_roads_board_one.append((cords_x, cords_y))

    return all_roads_board_one
