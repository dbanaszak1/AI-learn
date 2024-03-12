import pygame

class TrashCan:
    def __init__(self, color, expected_trash):
        self.color = color
        self.expected_trash = expected_trash
        self.actual_trash = 0

    def add_trash(self):
        self.actual_trash += 1

    def remove_trash(self):
        if self.actual_trash > 0:
            self.actual_trash -= 1

    def draw(self, surface, x, y, size):
        pygame.draw.rect(surface, self.color, (x, y, size, size))