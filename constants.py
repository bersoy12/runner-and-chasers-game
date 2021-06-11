import pygame

COLS, ROWS = int(input("input number of columns: ")), int(input("input number of rows: "))
WIDTH, HEIGHT = COLS*100, ROWS*100
SQUARE_SIZE = WIDTH // COLS
MOVE_DISTANCE = SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


CHASER = 1
RUNNER = 0

R_IMAGE = pygame.image.load("images\jogging.png")
C1_IMAGE = pygame.image.load("images\\thunder.png")
C2_IMAGE = pygame.image.load("images\\tornado.png")
