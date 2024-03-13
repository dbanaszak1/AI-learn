import pygame
import datetime

# TODO: proper inheritance

class TrashCan:
    def __init__(self, color, expectedTrash, photo):
        self.color = color
        self.expectedTrash = expectedTrash
        self.temperature
        self.isEmpty
        self.time
        self.photo = photo
        self.trashphoto

    def emptyTrashCan(self):
        self.isEmpty = True

    def fillTrashcan(self, temp, trashPhoto):
        self.isEmpty = False
        self.temperature = temp
        self.time = datetime.datetime.now()

class YellowTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((255, 255, 0), "plastic", 'assets/images/yellowBin.png')

class BlueTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((0, 0, 255), "paper", 'assets/images/blueBin.png')

class GreenTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((0, 255, 0), "glass", 'assets/images/greenBin.png')

class BrownTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((165, 42, 42), "BIO", 'assets/images/brownBin.png')

class RedTrashCan(TrashCan):
    def __init__(self, expectedTrash, photo):
        super().__init__((255, 0, 0), "mixed", 'assets/images/redBin.png')