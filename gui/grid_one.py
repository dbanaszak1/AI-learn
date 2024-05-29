from enum import Enum

class road_type(Enum):
    asphalt = 0
    paved = 1
    dirt = 2

GRID_SIZE = 32

GRID_ONE = [[road_type.asphalt.value for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for i in range(4, 24):
    for j in range(4, 8):
        GRID_ONE[i][j] = road_type.dirt.value
    for j in range(8, 12):
        GRID_ONE[i][j] = road_type.paved.value
    for j in range(12, 16):
        GRID_ONE[i][j] = road_type.dirt.value
    for j in range(20, 24):
        GRID_ONE[i][j] = road_type.dirt.value

for i in range(0, 28):
    for j in range(28, 32):
        GRID_ONE[i][j] = road_type.dirt.value

for i in range(28, 32):
    for j in range(32):
        GRID_ONE[i][j] = road_type.paved.value

def get_road_type(x, y):
    x = int(x/25)
    y = int(y/25)
    return GRID_ONE[y][x]

def check_row(x: int):
    count_a = 0
    count_b = 0
    count_c = 0
    x = int(x/32)
    for i in range(32):
        if GRID_ONE[x][i] == 0:
            count_a += 1
        elif GRID_ONE[x][i] == 1:
            count_b += 1
        else:
            count_c += 1
    if max(count_a, count_b, count_c) == count_a:
        return 1
    elif max(count_a, count_b, count_c) == count_b:
        return 2
    else:
        return 3

def check_col(x: int):
    x = int(x/32)
    count_a = 0
    count_b = 0
    count_c = 0
    for i in range(32):
        if GRID_ONE[i][x] == 0:
            count_a += 1
        elif GRID_ONE[i][x] == 1:
            count_b += 1
        else:
            count_c += 1
    if max(count_a, count_b, count_c) == count_a:
        return 1
    elif max(count_a, count_b, count_c) == count_b:
        return 2
    else:
        return 3