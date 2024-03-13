import pygame


def check_collision(truck_coordinates, houses):
    for house_coordinates in houses:
        if truck_coordinates[0] == house_coordinates.x and truck_coordinates[1] == house_coordinates.y:
            return True
    return False


class TrashTruck:
    def __init__(self, image_path, size, starting_coordinates):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = list(starting_coordinates)
        self.size = size
        self.rotation = 0
        self.flip = False

    def move(self, key_pressed, houses):
        directions = {
            # Key_Pressed : ( Coordinate X, Coordinate Y, Rotation, Flip)
            pygame.K_LEFT: (self.coordinates[0] - self.size[0], self.coordinates[1], 0, True),
            pygame.K_RIGHT: (self.coordinates[0] + self.size[0], self.coordinates[1], 0, False),
            pygame.K_UP: (self.coordinates[0], self.coordinates[1] - self.size[1], 90, False),
            pygame.K_DOWN: (self.coordinates[0], self.coordinates[1] + self.size[1], 270, False)
        }

        for key, (new_x, new_y, rotation, flip) in directions.items():
            if key_pressed[key]:
                if (0 <= new_x < 800 - self.size[0]) and (0 <= new_y < 800 - self.size[1]):
                    if not check_collision(truck_coordinates=(new_x, new_y), houses=houses):
                        self.coordinates = (new_x, new_y)
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

        window.blit(scaled_image, self.coordinates)
