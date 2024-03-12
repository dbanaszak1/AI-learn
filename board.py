import random
import pygame

from house import House

STARTING_POSITION = (0, 0)
PATH_TO_TRASH_TRUCK_IMAGE = "assets/images/trash_truck.png"
PATH_TO_HOUSE_IMAGE = "assets/images/house.png"
TRUCK_SIZE = (50, 50)
HOUSE_SIZE = (80, 80)
COLOR_FILL = (100, 100, 100)
LINE_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 800, 800
FPS = 60

class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("AI Project")
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.TRASH_TRUCK_IMAGE = pygame.image.load(PATH_TO_TRASH_TRUCK_IMAGE)
        self.TRASH_TRUCK = pygame.transform.scale(self.TRASH_TRUCK_IMAGE, TRUCK_SIZE)
        self.houses = []

        # Randomly generate houses
        num_houses = random.randint(5, 15)
        for _ in range(num_houses):
            x = random.randint(0, 15) * 50
            y = random.randint(0, 15) * 50
            self.houses.append(House(x, y))

    def draw_window(self):
        self.WINDOW.fill(COLOR_FILL)

        for i in range(0, WIDTH, TRUCK_SIZE[0]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (i, 0), (i, HEIGHT))
        for j in range(0, HEIGHT, TRUCK_SIZE[1]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (0, j), (WIDTH, j))

        for house in self.houses:
            house.draw(self.WINDOW)

        self.WINDOW.blit(self.TRASH_TRUCK, STARTING_POSITION)

        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_window()

        pygame.quit()