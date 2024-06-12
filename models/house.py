import pygame
import os
from .trashcan import YellowTrashCan, BlueTrashCan, BrownTrashCan, GreenTrashCan, RedTrashCan
from coordinates import Coordinates
import random
import asyncio

HOUSE_SIZE = (25, 25)
TRASHCAN_OFFSET = 50
TRASHCAN_SIZE = (15, 15)

current_directory = os.getcwd()
PATH_TO_HOUSE_IMAGE = os.path.join(current_directory, "assets", "images", "house.png")


class House:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
        self.trash_cans = {}
        self.generateTrashCans()
        self.update_trash_cans_capacity_task = asyncio.create_task(self.update_trash_cans_capacity())

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
            self.trash_cans[color()] = Coordinates(x, y)

    async def update_trash_cans_capacity(self):
        while True:
            await asyncio.sleep(10)
            for trash_can in self.trash_cans:
                trash_can.update_capacity()
                trash_can.update_last_pickup()

    def draw(self, surface):
        # House draw
        house_image = pygame.image.load(PATH_TO_HOUSE_IMAGE)
        house_image = pygame.transform.scale(house_image, HOUSE_SIZE)
        surface.blit(house_image, (self.coordinates.x, self.coordinates.y))

        # Cans draw
        for trash_can, coordinates in self.trash_cans.items():
            trash_image = pygame.image.load(trash_can.photo)
            trash_image = pygame.transform.scale(trash_image, TRASHCAN_SIZE)
            surface.blit(trash_image, (coordinates.x, coordinates.y))
            trash_can.draw_capacity(surface, coordinates)
            trash_can.draw_last_pickup(surface, coordinates)
