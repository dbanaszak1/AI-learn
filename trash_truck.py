import pygame
from coordinates import Coordinates, check_collision, Directions, SQUARE_SIZE, WIDTH, HEIGHT
import asyncio
from collections import deque


class TrashTruck:
    def __init__(self, image_path: str, size: (int, int), coordinates: Coordinates,
                 direction: Directions = Directions.RIGHT.value):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.size = size
        self.rotation = self.calc_rotation(self.coordinates.direction)
        self.flip = self.check_flip(self.coordinates.direction)

    async def move(self, key_pressed, houses: []):
        directions = {
            # Key_Pressed : ( Coordinates, Rotation, Flip)
            pygame.K_LEFT: (self.coordinates.rotate_left()),
            pygame.K_RIGHT: (self.coordinates.rotate_right()),
            pygame.K_UP: (self.coordinates.move_forward()),
        }

        for key, (coordinates) in directions.items():
            if key_pressed[key]:
                if not check_collision(truck_coordinates=coordinates, houses=houses):
                    self.coordinates = coordinates
                    self.rotation = self.calc_rotation(self.coordinates.direction)
                    self.flip = self.check_flip(self.coordinates.direction)
                    await asyncio.sleep(0.15)
                    # print("direction: ", self.coordinates.direction)
                    # print("rotation: ", self.rotation)
                    # print("flip: ", self.flip)
                    # print("x: ", self.coordinates.x)
                    # print("y: ", self.coordinates.y)
                    break

    async def follow_path(self, houses, draw, target):
        path = self.find_shortest_path(houses, target)
        print(path)
        if path:
            for next_square in path:
                self.coordinates.direction = self.move_direction(self.coordinates,
                                                                 Coordinates(next_square[0], next_square[1]))
                self.rotation = self.calc_rotation(self.coordinates.direction)
                self.flip = self.check_flip(self.coordinates.direction)
                self.coordinates = Coordinates(next_square[0], next_square[1])
                await asyncio.sleep(0.15)
                draw()

    def move_direction(self, start_coordinates, end_coordinates):
        if start_coordinates.x > end_coordinates.x and start_coordinates.y == end_coordinates.y:
            return Directions.LEFT.value
        if start_coordinates.x < end_coordinates.x and start_coordinates.y == end_coordinates.y:
            return Directions.RIGHT.value
        if start_coordinates.x == end_coordinates.x and start_coordinates.y > end_coordinates.y:
            return Directions.UP.value
        if start_coordinates.x == end_coordinates.x and start_coordinates.y < end_coordinates.y:
            return Directions.DOWN.value

    def find_shortest_path(self, houses, target):
        start = (self.coordinates.x, self.coordinates.y)
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
                neighbour = self.get_neighbour(current, direction)
                if neighbour[0] < 0 or neighbour[0] > WIDTH or neighbour[1] < 0 or neighbour[1] > HEIGHT:
                    continue
                if (neighbour not in visited and
                        not check_collision(truck_coordinates=Coordinates(neighbour[0], neighbour[1]), houses=houses)):
                    queue.append(path + [neighbour])
        return []

    def get_neighbour(self, position, direction):
        if direction == Directions.UP.value:
            return position[0], position[1] - SQUARE_SIZE
        elif direction == Directions.DOWN.value:
            return position[0], position[1] + SQUARE_SIZE
        elif direction == Directions.LEFT.value:
            return position[0] - SQUARE_SIZE, position[1]
        elif direction == Directions.RIGHT.value:
            return position[0] + SQUARE_SIZE, position[1]

    def calc_rotation(self, direction):
        if direction == Directions.UP.value:
            return 90
        elif direction == Directions.DOWN.value:
            return 270
        elif direction == Directions.LEFT.value:
            return 180
        else:
            return 0

    def check_flip(self, direction):
        return direction == Directions.LEFT.value

    def draw(self, window):
        if not self.flip:
            rotated_image = pygame.transform.rotate(self.original_image, self.rotation)
            scaled_image = pygame.transform.scale(rotated_image, self.size)
        else:
            flipped_image = pygame.transform.flip(self.original_image, True, False)
            scaled_image = pygame.transform.scale(flipped_image, self.size)

        window.blit(scaled_image, (self.coordinates.x, self.coordinates.y))
