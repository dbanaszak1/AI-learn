from enum import Enum
from gui.grid_one import GRID_ONE

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 25

class Action(Enum):
    forward = "forward"
    left = "turn left"
    right = "turn right"

class Directions(Enum):
    UP = 0
    DOWN = 2
    LEFT = 1
    RIGHT = 3

class Coordinates:
    def __init__(self, x: int = 0, y: int = 0, direction: Directions = Directions.DOWN, action = None):
        self.x = x
        self.y = y
        self.direction = direction
        self.action = action
        self.f = float('inf')  # Total cost of the cell (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination
        self.parent_x = -1
        self.parent_y = -1
        self.parent_dir = Directions.DOWN
        self.x_grid = int(self.x/25)
        self.y_grid = int(self.y/25)

    def rotate_left(self):
        if self.direction == Directions.UP.value:
            return Coordinates(self.x, self.y, Directions.LEFT.value)
        elif self.direction == Directions.LEFT.value:
            return Coordinates(self.x, self.y, Directions.DOWN.value)
        elif self.direction == Directions.DOWN.value:
            return Coordinates(self.x, self.y, Directions.RIGHT.value)
        elif self.direction == Directions.RIGHT.value:
            return Coordinates(self.x, self.y, Directions.UP.value)

    def rotate_right(self):
        if self.direction == Directions.UP.value:
            return Coordinates(self.x, self.y, Directions.RIGHT.value)
        elif self.direction == Directions.RIGHT.value:
            return Coordinates(self.x, self.y, Directions.DOWN.value)
        elif self.direction == Directions.DOWN.value:
            return Coordinates(self.x, self.y, Directions.LEFT.value)
        elif self.direction == Directions.LEFT.value:
            return Coordinates(self.x, self.y, Directions.UP.value)

    def move_forward(self):
        if self.direction == Directions.UP.value and self.y - SQUARE_SIZE > 0:
            return Coordinates(self.x, self.y - SQUARE_SIZE, self.direction)
        elif self.direction == Directions.DOWN.value and self.y + SQUARE_SIZE < HEIGHT:
            return Coordinates(self.x, self.y + SQUARE_SIZE, self.direction)
        elif self.direction == Directions.LEFT.value and self.x - SQUARE_SIZE > 0:
            return Coordinates(self.x - SQUARE_SIZE, self.y, self.direction)
        elif self.direction == Directions.RIGHT.value and self.x + SQUARE_SIZE < WIDTH:
            return Coordinates(self.x + SQUARE_SIZE, self.y, self.direction)
        return Coordinates(self.x, self.y, self.direction)

def check_collision(truck_coordinates: Coordinates, houses):
    for house in houses:
        if truck_coordinates.x == house.coordinates.x and truck_coordinates.y == house.coordinates.y:
            return True
    return False
