import pygame
import os
from coordinates import Coordinates, check_collision, Directions, SQUARE_SIZE, WIDTH, HEIGHT
import asyncio
from utils.utils import move_direction, check_flip, calc_rotation, a_star_search
from gui.grid_one import get_road_type

current_directory = os.getcwd()
PATH_TO_TRASH_TRUCK_IMAGE = os.path.join(current_directory, "assets", "images", "trash-truck.png")

class TrashTruck:
    def __init__(self, size, coordinates: Coordinates):
        self.original_image = pygame.image.load(PATH_TO_TRASH_TRUCK_IMAGE)
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.size = size
        self.rotation = calc_rotation(self.coordinates.direction)
        self.flip = check_flip(self.coordinates.direction)

    async def move(self, key_pressed, houses):
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
                    self.rotation = calc_rotation(self.coordinates.direction)
                    self.flip = check_flip(self.coordinates.direction)
                    await asyncio.sleep(0.15)
                    break
              
    async def follow_path(self, houses, drawWindow):
        count = 1
        for house in houses :
            print("destination: house", count)
            path = a_star_search(self.coordinates, house.coordinates)
            if path:
                for next_move in path:
                    self.coordinates = move_direction(self.coordinates, next_move)
                    self.rotation = calc_rotation(self.coordinates.direction)
                    self.flip = check_flip(self.coordinates.direction)
                    current_place = next_move
                    await asyncio.sleep(0.075)
                    drawWindow()
            count += 1
            await asyncio.sleep(0.15)

    def draw(self, window):
        if not self.flip:
            rotated_image = pygame.transform.rotate(self.original_image, self.rotation)
            scaled_image = pygame.transform.scale(rotated_image, self.size)
        else:
            flipped_image = pygame.transform.flip(self.original_image, True, False)
            scaled_image = pygame.transform.scale(flipped_image, self.size)

        window.blit(scaled_image, (self.coordinates.x, self.coordinates.y))
