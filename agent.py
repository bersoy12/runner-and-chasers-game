import pygame
from constants import *


class Runner:
    def __init__(self, row, col, color, name):
        self.row = row
        self.col = col
        self.name = name
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col) + (SQUARE_SIZE//2) - 15
        self.y = (SQUARE_SIZE*self.row) + (SQUARE_SIZE//2) - 15

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 15,15))
        pygame.display.flip()


class Chaser:
    def __init__(self, row, col, color, name):
        self.row = row
        self.col = col
        self.name = name
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col) + (SQUARE_SIZE//2) - 15
        self.y = (SQUARE_SIZE*self.row) + (SQUARE_SIZE//2) - 15

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 15,15))
        pygame.display.flip()
