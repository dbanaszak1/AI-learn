import pygame
import datetime


# TODO: proper inheritance

class TrashCan:
    def __init__(self, color: (int, int, int), expectedTrash: str, photo: str):
        self.color = color
        self.expectedTrash = expectedTrash
        self.photo = photo
        self.trash_photo = None
        self.temperature = 0
        self.actualCapacity = 0
        self.maxCapacity = 100
        self.isEmpty = True
        self.time = datetime.datetime.now()

    def emptyTrashCan(self):
        self.isEmpty = True

    def fillTrashcan(self, temp, trashPhoto):
        self.isEmpty = False
        self.temperature = temp


class YellowTrashCan(TrashCan):
    def __init__(self, expectedTrash=None, photo=None):
        if expectedTrash is None:
            expectedTrash = "plastic"
        if photo is None:
            photo = 'assets/images/yellowBin.png'
        super().__init__((255, 255, 0), expectedTrash, photo)


class BlueTrashCan(TrashCan):
    def __init__(self, expectedTrash=None, photo=None):
        if expectedTrash is None:
            expectedTrash = "paper"
        if photo is None:
            photo = 'assets/images/blueBin.png'
        super().__init__((0, 0, 255), expectedTrash, photo)


class BrownTrashCan(TrashCan):
    def __init__(self, expectedTrash=None, photo=None):
        if expectedTrash is None:
            expectedTrash = "BIO"
        if photo is None:
            photo = 'assets/images/brownBin.png'
        super().__init__((165, 42, 42), expectedTrash, photo)


class RedTrashCan(TrashCan):
    def __init__(self, expectedTrash=None, photo=None):
        if expectedTrash is None:
            expectedTrash = "mixed"
        if photo is None:
            photo = 'assets/images/redBin.png'
        super().__init__((255, 0, 0), expectedTrash, photo)


class GreenTrashCan(TrashCan):
    def __init__(self, expectedTrash=None, photo=None):
        if expectedTrash is None:
            expectedTrash = "glass"
        if photo is None:
            photo = 'assets/images/greenBin.png'
        super().__init__((0, 255, 0), expectedTrash, photo)



