import pygame
from trashcan import TrashCan

HOUSE_SIZE = (50, 50)

class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.trash_cans = [TrashCan((255, 255, 0), 5), TrashCan((0, 255, 0), 3)]

    def draw(self, surface):
        house_image = pygame.image.load("assets/images/house.png") 
        house_image = pygame.transform.scale(house_image, HOUSE_SIZE)
        surface.blit(house_image, (self.x, self.y))