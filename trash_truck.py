import pygame
from coordinates import Coordinates, check_collision


class TrashTruck:
    def __init__(self, image_path: str, size: (int, int), coordinates: Coordinates):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.size = size
        self.rotation = 0
        self.flip = False

    def move(self, key_pressed, houses: []):
        directions = {
            # Key_Pressed : ( Coordinates, Rotation, Flip)
            pygame.K_LEFT: (self.coordinates.move_left(), 0, True),
            pygame.K_RIGHT: (self.coordinates.move_right(), 0, False),
            pygame.K_UP: (self.coordinates.move_up(), 90, False),
            pygame.K_DOWN: (self.coordinates.move_down(), 270, False)
        }

        for key, (coordinates, rotation, flip) in directions.items():
            if key_pressed[key]:
                if not check_collision(truck_coordinates=coordinates, houses=houses):
                    self.coordinates = coordinates
                    self.rotation = rotation
                    self.flip = flip
                    break

    def draw(self, window):
        if not self.flip:
            rotated_image = pygame.transform.rotate(self.original_image, self.rotation)
            scaled_image = pygame.transform.scale(rotated_image, self.size)
        else:
            flipped_image = pygame.transform.flip(self.original_image, True, False)
            scaled_image = pygame.transform.scale(flipped_image, self.size)

        window.blit(scaled_image, (self.coordinates.x, self.coordinates.y))
