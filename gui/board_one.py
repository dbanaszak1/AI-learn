import pygame

BLOCK_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)


def draw_road_one(WINDOW, STARTING_COORDINATES, BLOCK_SIZE):
    for i in range(STARTING_COORDINATES.y - 25, BLOCK_SIZE * 20, BLOCK_SIZE):
        pygame.draw.rect(WINDOW, BLOCK_COLOR, pygame.Rect(STARTING_COORDINATES.x, i, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(WINDOW, BLOCK_COLOR, pygame.Rect(STARTING_COORDINATES.x + 19, i, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.line(WINDOW, LINE_COLOR, (STARTING_COORDINATES.x + 25, i), (STARTING_COORDINATES.x + 25, i + 10), 1)
