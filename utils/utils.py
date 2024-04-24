from collections import deque
from coordinates import Directions, Coordinates
from models.trash_truck import check_collision, WIDTH, HEIGHT, SQUARE_SIZE


def move_direction(start_coordinates, end_coordinates):
    if start_coordinates.x > end_coordinates.x and start_coordinates.y == end_coordinates.y:
        return Directions.LEFT.value
    if start_coordinates.x < end_coordinates.x and start_coordinates.y == end_coordinates.y:
        return Directions.RIGHT.value
    if start_coordinates.x == end_coordinates.x and start_coordinates.y > end_coordinates.y:
        return Directions.UP.value
    if start_coordinates.x == end_coordinates.x and start_coordinates.y < end_coordinates.y:
        return Directions.DOWN.value


def find_shortest_path(coordinates: Coordinates, houses, target, roads):
    start = (coordinates.x, coordinates.y)
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == target:
            return path[1:]
        if current in visited:
            continue
        visited.add(current)
        for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                          Directions.RIGHT.value]:
            neighbour = get_neighbour(current, direction)
            if neighbour[0] < 0 or neighbour[0] > WIDTH or neighbour[1] < 0 or neighbour[1] > HEIGHT:
                continue
            if neighbour not in roads:
                continue
            if (neighbour not in visited and
                    not check_collision(truck_coordinates=Coordinates(neighbour[0], neighbour[1]), houses=houses)):
                queue.append(path + [neighbour])
    return []


def get_neighbour(position, direction):
    if direction == Directions.UP.value:
        return position[0], position[1] - SQUARE_SIZE
    elif direction == Directions.DOWN.value:
        return position[0], position[1] + SQUARE_SIZE
    elif direction == Directions.LEFT.value:
        return position[0] - SQUARE_SIZE, position[1]
    elif direction == Directions.RIGHT.value:
        return position[0] + SQUARE_SIZE, position[1]


def calc_rotation(direction):
    if direction == Directions.UP.value:
        return 90
    elif direction == Directions.DOWN.value:
        return 270
    elif direction == Directions.LEFT.value:
        return 180
    else:
        return 0


def check_flip(direction):
    return direction == Directions.LEFT.value
