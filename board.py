import random
import asyncio
import pygame
from models.trash_truck import TrashTruck
from coordinates import Coordinates, Directions
from models.house import House
from gui.grid_one import get_road_type

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
        self.all_roads = []
        self.houses = []
        self.weather = "clear"
        self.season = "summer"
        self.temp = 20
        self.trash_truck = TrashTruck(size=TRUCK_SIZE, coordinates=STARTING_COORDINATES, weather=self.weather,
                                      temp=self.temp, season=self.season)

    async def change_weather(self):
        while True:
            await asyncio.sleep(2)
            weather_options = ["clear", "rain", "snow"]
            season_options = ["winter", "autumn", "spring", "summer"]
            self.weather = random.choice(weather_options)
            self.season = random.choice(season_options)
            self.temp = random.randint(-10, 30)
            self.trash_truck.weather = self.weather
            self.trash_truck.temp = self.temp
            self.trash_truck.season = self.season


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

        for i in range(32):
            for j in range(32):
                colour = (0, 0, 0)
                road = get_road_type(i * 25, j * 25)
                match road:
                    case 0:
                        colour = (64, 64, 64)
                    case 1:
                        colour = (128, 128, 128)
                    case 2:
                        colour = (139, 69, 19)
                cell_rect = pygame.Rect(i * 25 + 1, j * 25 + 1, 24, 24)
                pygame.draw.rect(self.WINDOW, colour, cell_rect)

    def draw_objects(self):
        if len(self.houses) == 0:
            self.generate_houses()
        for house in self.houses:
            house.draw(self.WINDOW)
        self.trash_truck.draw(self.WINDOW)
        incinerator = pygame.image.load("assets/images/incinerator.png")
        incinerator = pygame.transform.scale(incinerator, (100, 100))
        self.WINDOW.blit(incinerator, (42, 35))

        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Weather: {self.weather}", True, (255, 255, 255))
        self.WINDOW.blit(text, (10, 10))
        text = font.render(f"Temp: {self.temp}", True, (255, 255, 255))
        self.WINDOW.blit(text, (200, 10))
        text = font.render(f"Season: {self.season}", True, (255, 255, 255))
        self.WINDOW.blit(text, (400, 10))
        pygame.display.update()

    def generate_houses(self):
        coordinates = [(5, 12), (8, 12), (12, 9), (15, 10), (16, 25), (17, 27), (14, 16), (24, 3), (25, 5), (26, 10),
                       (5, 26), (6, 7)]
        for cor in coordinates:
            x = cor[0] * 25
            y = cor[1] * 25
            self.houses.append(House(Coordinates(int(x), int(y))))

    async def main(self):
        asyncio.create_task(self.change_weather())

        run = True
        while run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        await self.trash_truck.follow_path(self.houses, self.draw_window)

            keys = pygame.key.get_pressed()
            await self.trash_truck.move(keys, self.houses)
            self.draw_window()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    board = Board()
    asyncio.run(board.main())
