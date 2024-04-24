import pygame

LINE_COLOR = (255, 255, 255)


class Road:
    def __init__(self, window, block_color, block_size, coordinate_x, coordinate_y):
        self.window = window
        self.block_color = block_color
        self.block_size = block_size
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def draw(self):
        pygame.draw.rect(self.window, self.block_color,
                         pygame.Rect(self.coordinate_x, self.coordinate_y, self.block_size, self.block_size))
