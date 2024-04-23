import pygame
from main.coordinates import Coordinates
from incinerator import Incinerator


class Landfill:
    def __init__(self, image_path: str, size: (int, int), coordinates: Coordinates):
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.size = size
        self.rotation = 0
        self.is_gate_open = False
        self.incinerator = Incinerator(self, self.coordinates)
        self.dumps = []

    def openGate(self):
        if self.is_gate_open:
            print("Gate is already open")
            return
        else :
            print("Opening the gate...")
            self.is_gate_open = True
            print("Opened the gate")

    def closeGate (self):
        if self.is_gate_open:
            print("Closing the gate...")
            self.is_gate_open = False
            print("Closed the gate")
        else:
            print("Gate is already closed")

    def check_has_free_place(self, trash_type):
        return True
