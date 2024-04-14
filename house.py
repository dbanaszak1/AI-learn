import pygame
from trashcan import YellowTrashCan, BlueTrashCan, BrownTrashCan, GreenTrashCan, RedTrashCan
from coordinates import Coordinates
import random

HOUSE_SIZE = (25, 25)
TRASHCAN_OFFSET = 50
TRASHCAN_SIZE = (15, 15)

class House:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
        self.trash_cans = {}
        self.generateTrashCans()

    def generateTrashCans(self):
        directions = [
            (25, 0),
            (-25, 0),
            (0, -25),
            (0, 25)
        ]
        colors = [YellowTrashCan, BlueTrashCan, BrownTrashCan, GreenTrashCan, RedTrashCan]
        for direction in directions:
            x = self.coordinates.x + direction[0]
            y = self.coordinates.y + direction[1]
            color = random.choice(colors)
            colors.remove(color)

            self.trash_cans[color(Coordinates(x, y))] = Coordinates(x, y)

    def draw(self, surface):
        # House draw
        house_image = pygame.image.load("assets/images/house.png")
        house_image = pygame.transform.scale(house_image, HOUSE_SIZE)
        surface.blit(house_image, (self.coordinates.x, self.coordinates.y))

        # Cans draw
        for trash_can, coordinates in self.trash_cans.items():
            trash_image = pygame.image.load(trash_can.photo)
            trash_image = pygame.transform.scale(trash_image, TRASHCAN_SIZE)
            surface.blit(trash_image, (coordinates.x, coordinates.y))


