

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 25


class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_down(self):
        if self.y + SQUARE_SIZE >= HEIGHT:
            return Coordinates(self.x, self.y)

        return Coordinates(self.x, self.y + SQUARE_SIZE)

    def move_up(self):
        if self.y - SQUARE_SIZE < 0:
            return Coordinates(self.x, self.y)

        return Coordinates(self.x, self.y - SQUARE_SIZE)

    def move_left(self):
        if self.x - SQUARE_SIZE < 0:
            return Coordinates(self.x, self.y)

        return Coordinates(self.x - SQUARE_SIZE, self.y)

    def move_right(self):
        if self.x + SQUARE_SIZE >= WIDTH:
            return Coordinates(self.x, self.y)

        return Coordinates(self.x + SQUARE_SIZE, self.y)


def check_collision(truck_coordinates: Coordinates, houses: []):
    for house in houses:
        if truck_coordinates.x == house.coordinates.x and truck_coordinates.y == house.coordinates.y:
            return True
    return False
