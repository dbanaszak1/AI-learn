import asyncio
import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from coordinates import Coordinates
from trashtype import Trash, GlassTrash, PaperTrash, BioTrash, MixedTrash, PlasticTrash, MetalTrash

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INCINERATOR_IMAGE_TURNED_ON_PATH = os.path.join(base_dir, "assets\images\incinerator_on.png")
INCINERATOR_IMAGE_TURNED_OFF_PATH = os.path.join(base_dir, "assets\images\incinerator_off.png")

class Incinerator:
    def __init__(self, coordinates: Coordinates, is_turned_on: bool = False, size: (int, int) = (1,1), initial_contents: list = []):
        self.is_turned_on = False
        self.original_image = pygame.image.load(INCINERATOR_IMAGE_TURNED_ON_PATH if is_turned_on else INCINERATOR_IMAGE_TURNED_OFF_PATH)
        self.size = size
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.rotation = 0
        self.burning_per_second = 1
        self.max_capacity = 100
        self.contents = initial_contents
        self.is_gate_open = False

    def check_can_burn(self, trash):
        trash_type_checks = {
            "glass": lambda trash: False,
            "paper": lambda trash: isinstance(trash, PaperTrash),
            "bio": lambda trash: False,
            "mixed": lambda trash: isinstance(trash, MixedTrash),
            "plastic": lambda trash: False,
            "metal": lambda trash: False,
        }

        return trash_type_checks.get(trash.trash_type, lambda trash: False)(trash)

    def switch(self):
        self.is_turned_on = not self.is_turned_on
        self.original_image = pygame.image.load(INCINERATOR_IMAGE_TURNED_ON_PATH if self.is_turned_on else INCINERATOR_IMAGE_TURNED_OFF_PATH)
        self.image = pygame.transform.scale(self.original_image, self.size)
        if (self.is_turned_on):
            asyncio.run(self.burn(self.contents[0]))

    async def burn(self, trash):
        await asyncio.sleep(1)
        self.contents.remove(trash)
        print("Burned", trash.trash_type)
        if (len(self.contents) == 0):
            self.is_turned_on = False
        elif (self.is_turned_on):
            print(len(self.contents), "to go")
            await self.burn(self.contents[0])

    def add_trash(self, trash):
        if self.check_can_burn(trash):
            self.contents.append(trash)
            return True
        else:
            print(trash.trash_type, "cannot be burned!")
            return False
