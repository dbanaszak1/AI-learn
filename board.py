import random
import pygame
from trash_truck import TrashTruck
from house import House


STARTING_COORDINATES = (0, 0)
PATH_TO_TRASH_TRUCK_IMAGE = "assets/images/trash_truck.png"
PATH_TO_HOUSE_IMAGE = "assets/images/house.png"
TRUCK_SIZE = (25, 25)
COLOR_FILL = (100, 100, 100)
LINE_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 800, 800
BLOCK_SIZE = int(WIDTH / TRUCK_SIZE[0])
FPS = 60


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("AI Project")
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.trash_truck = TrashTruck(PATH_TO_TRASH_TRUCK_IMAGE, TRUCK_SIZE, STARTING_COORDINATES)
        self.houses = []

        for _ in range(random.randint(int(BLOCK_SIZE / 2), BLOCK_SIZE)):
            x = random.randint(0, BLOCK_SIZE) * TRUCK_SIZE[0]
            y = random.randint(0, BLOCK_SIZE) * TRUCK_SIZE[0]
            if (x == 0 and y == 0) or (x == 25 and y == 0) or (x == 0 and y == 25):
                continue
            self.houses.append(House(x, y))

    def draw_window(self):
        self.WINDOW.fill(COLOR_FILL)
        self.trash_truck.draw(self.WINDOW)

        for i in range(0, WIDTH, TRUCK_SIZE[0]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (i, 0), (i, HEIGHT))
        for j in range(0, HEIGHT, TRUCK_SIZE[1]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (0, j), (WIDTH, j))

        for house in self.houses:
            house.draw(self.WINDOW)

        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            self.trash_truck.move(keys, self.houses)
            self.draw_window()

        pygame.quit()
