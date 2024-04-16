from enum import Enum

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 25

class Directions(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

class Coordinates:
    def __init__(self, x: int, y: int, direction: Directions = Directions.RIGHT.value):
        self.x = x
        self.y = y
        self.direction = direction

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

def check_collision(truck_coordinates: Coordinates, houses: []):
    for house in houses:
        if truck_coordinates.x == house.coordinates.x and truck_coordinates.y == house.coordinates.y:
            return True
    return False
