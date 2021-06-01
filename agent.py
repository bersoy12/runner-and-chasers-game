import pygame
from constants import *

class Runner:
    def __init__(self, row, col, pic, name):
        self.type = "runner"
        self.row = row
        self.col = col
        self.pic = pic
        self.name = name

        self.x = 0
        self.y = 0
        self.calc_pos()


    def move(self, row ,col):
        self.row = row
        self.col = col
        self.calc_pos()
        
        

    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col) + SQUARE_SIZE // 2 - 32
        self.y = (SQUARE_SIZE*self.row) + SQUARE_SIZE // 2 - 32
    

    def draw(self,window):
        window.blit(self.pic,(self.x,self.y))


class Chaser:
    def __init__(self, row, col, pic, name):
        self.type = "chaser"
        self.row = row
        self.col = col
        self.pic = pic
        self.name = name

        self.x = 0
        self.y = 0
        self.calc_pos()


    def move(self, row ,col):
        self.row = row
        self.col = col
        self.calc_pos()
        

    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col) + SQUARE_SIZE // 2 - 32
        self.y = (SQUARE_SIZE*self.row) + SQUARE_SIZE // 2 - 32
    

    def draw(self,window):
        window.blit(self.pic,(self.x,self.y))