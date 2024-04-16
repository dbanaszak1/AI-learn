import pygame
from coordinates import Coordinates, check_collision, Directions
import asyncio

class TrashTruck:
    def __init__(self, image_path: str, size: (int, int), coordinates: Coordinates, direction: Directions = Directions.RIGHT.value):
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
                    self.rotation =  self.calc_rotation(self.coordinates.direction)
                    self.flip =  self.check_flip(self.coordinates.direction)
                    await asyncio.sleep(0.15)
                    # print("direction: ", self.coordinates.direction)
                    # print("rotation: ", self.rotation)
                    # print("flip: ", self.flip)
                    # print("x: ", self.coordinates.x)
                    # print("y: ", self.coordinates.y)
                    break

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
