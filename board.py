import random
import pygame
from models.trash_truck import TrashTruck
from coordinates import Coordinates, Directions
from models.house import House
from gui.board_one import draw_road_one
from gui.board_two import draw_road_two

STARTING_COORDINATES = Coordinates()
STARTING_COORDINATES.x = 50
STARTING_COORDINATES.y = 125
STARTING_COORDINATES.direction = Directions.DOWN
TRUCK_SIZE = (25, 25)
COLOR_FILL = (100, 100, 100)
LINE_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 800, 800
BLOCK_SIZE = 25
FPS = 60

class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("AI Project")
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.trash_truck = TrashTruck(size=TRUCK_SIZE, coordinates=STARTING_COORDINATES)
        self.all_roads = []
        self.houses = []

    def draw_window(self):
        self.clock.tick(self.FPS)
        self.WINDOW.fill(COLOR_FILL)
        self.draw_roads()
        self.draw_objects()

    def draw_roads(self):
        for i in range(0, WIDTH, TRUCK_SIZE[0]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (i, 0), (i, HEIGHT))
        for j in range(0, HEIGHT, TRUCK_SIZE[1]):
            pygame.draw.line(self.WINDOW, LINE_COLOR, (0, j), (WIDTH, j))

    def draw_objects(self):
        if len(self.houses) == 0:
            self.generate_houses()
        for house in self.houses:
            house.draw(self.WINDOW)
        self.trash_truck.draw(self.WINDOW)
        incinerator = pygame.image.load("assets/images/incinerator.png")
        incinerator = pygame.transform.scale(incinerator, (100, 100))
        self.WINDOW.blit(incinerator, (42, 35))
        pygame.display.update()

    def generate_houses(self):
        for _ in range(random.randint(1, 5)):
            x = random.randint(0, BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, BLOCK_SIZE) * BLOCK_SIZE
            if x <= 50 and y <= 50 or tuple((x, y)) in self.all_roads:
                continue
            self.houses.append(House(Coordinates(int(x), int(y))))

    async def main(self):

        run = True
        while run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        await self.trash_truck.follow_path(self.houses, self.draw_window, (350, 350), self.all_roads)
                        await self.trash_truck.follow_path(self.houses, self.draw_window, (225, 700), self.all_roads)
                        await self.trash_truck.follow_path(self.houses, self.draw_window, (750, 150), self.all_roads)
                        await self.trash_truck.follow_path(self.houses, self.draw_window, (650, 575), self.all_roads)
                        await self.trash_truck.follow_path(self.houses, self.draw_window, (50, 125), self.all_roads)

            keys = pygame.key.get_pressed()
            await self.trash_truck.move(keys, self.houses)
            self.draw_window()
            pygame.display.update()

        pygame.quit()
