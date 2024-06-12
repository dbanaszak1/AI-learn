import pygame
import datetime
import random
import os
import asyncio
from joblib import load


IMAGES_PATH = "./assets/images/"


class TrashCan:
    def __init__(self, color: (int, int, int), expected_trash: str, photo: str):
        self.color = color
        self.expected_trash = expected_trash
        self.photo = photo
        self.trash_photo = None
        self.pickup()
        self.capacity = 0
        self.maxCapacity = 100
        self.time = datetime.datetime.now()
        self.update_capacity()
        self.lastPickup = 0
        self.pickup_available = 1
        self.update_last_pickup()


    def pickup(self):
        self.capacity = 0
        self.lastPickup = 0

    def update_capacity(self):
        trash_added = random.randint(10, 20)
        self.capacity = min(self.maxCapacity, self.capacity + trash_added)

    def update_last_pickup(self):
        self.lastPickup = self.lastPickup + 1

    def draw_capacity(self, surface, coordinates):
        font = pygame.font.SysFont(None, 18)
        text = font.render(f"{self.capacity}", True, (255, 255, 255))
        surface.blit(text, (coordinates.x, coordinates.y + 20))

    def draw_last_pickup(self, surface, coordinates):
        font = pygame.font.SysFont(None, 18)
        text = font.render(f"{self.lastPickup}", True, (255, 255, 255))
        surface.blit(text, (coordinates.x, coordinates.y))


class YellowTrashCan(TrashCan):
    def __init__(self, expected_trash="plastic", photo=None):
        if expected_trash is None:
            expected_trash = "plastic"
        if photo is None:
            photo = IMAGES_PATH + 'trash-can-yellow.png'
        super().__init__((255, 255, 0), expected_trash, photo)


class BlueTrashCan(TrashCan):
    def __init__(self, expected_trash="paper", photo=None):
        if expected_trash is None:
            expected_trash = "paper"
        if photo is None:
            photo = IMAGES_PATH + 'trash-can-blue.png'
        super().__init__((0, 0, 255), expected_trash, photo)


class BrownTrashCan(TrashCan):
    def __init__(self, expected_trash="BIO", photo=None):
        if expected_trash is None:
            expected_trash = "BIO"
        if photo is None:
            photo = IMAGES_PATH + 'trash-can-brown.png'
        super().__init__((165, 42, 42), expected_trash, photo)


class RedTrashCan(TrashCan):
    def __init__(self, expected_trash="mixed", photo=None):
        if expected_trash is None:
            expected_trash = "mixed"
        if photo is None:
            photo = IMAGES_PATH + 'trash-can-red.png'
        super().__init__((255, 0, 0), expected_trash, photo)


class GreenTrashCan(TrashCan):
    def __init__(self, expected_trash="glass", photo=None):
        if expected_trash is None:
            expected_trash = "glass"
        if photo is None:
            photo = IMAGES_PATH + 'trash-can-green.png'
        super().__init__((0, 255, 0), expected_trash, photo)
