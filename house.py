import pygame
from trashcan import YellowTrashCan, BlueTrashCan, BrownTrashCan, GreenTrashCan, RedTrashCan
import random

HOUSE_SIZE = (25, 25)


class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trash_cans = []

    def generateTrashCans(self):
        # TODO: generate trashcans - at most 1 of each colour
        rand = random.randint(0, 1)

    def draw(self, surface):
        house_image = pygame.image.load("assets/images/house.png")
        house_image = pygame.transform.scale(house_image, HOUSE_SIZE)
        surface.blit(house_image, (self.x, self.y))
