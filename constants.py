import pygame

WIDTH, HEIGHT = 1300, 800
COLS, ROWS  = 13, 8
SQUARE_SIZE = WIDTH // COLS
MOVE_DISTANCE = SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

R_IMAGE = pygame.image.load("images\jogging.png")
C1_IMAGE = pygame.image.load("images\\thunder.png")
C2_IMAGE = pygame.image.load("images\\tornado.png")