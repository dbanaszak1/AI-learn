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
        self.isEmpty = True
        self.time = datetime.datetime.now()

    def emptyTrashCan(self):
        self.isEmpty = True

    def fillTrashcan(self, temp, trashPhoto):
        self.isEmpty = False
        self.temperature = temp


class YellowTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((255, 255, 0), "plastic", 'assets/images/trash-can-yellow.png')


class BlueTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((0, 0, 255), "paper", 'assets/images/trash-can-blue.png')


class GreenTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((0, 255, 0), "glass", 'assets/images/trash-can-green.png')


class BrownTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((165, 42, 42), "BIO", 'assets/images/trash-can-brown.png')


class RedTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((255, 0, 0), "mixed", 'assets/images/trash-can-red.png')


class RedTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((255, 0, 0), "mixed", 'assets/images/trash-can-black.png')
