from agent import Runner, Chaser
import pygame
from constants import *
from board import Board
import random as rnd


class Game:
    def __init__(self, window):
        self._init()
        self.window = window
        self.moves_list = {}
        self.round = 0


    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = self.board.agent_list[0]
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        agent = self.board.get_agent(row, col)

        if agent != 0 and agent == self.turn:
            self.selected = agent
            self.valid_moves = self.board.get_valid_moves(agent)
            return True

        return False


    def collision(self, row, col):
        agent = self.board.get_agent(row, col)

    def _move(self, row, col):
        agent = self.board.get_agent(row, col)
        if self.selected and agent == 0 and (row, col) in self.valid_moves.values():
            self.board.move(self.selected, row, col)
            self.change_turn()
        elif self.selected and agent != 0 and (row, col) in self.valid_moves.values():
            self.collision(row, col)
            return self.winner()
        else:
            return False
        return True            
    
    
    def draw_valid_moves(self, moves):
        for r, c in moves.values():
            row, col = r, c
            pygame.draw.circle(self.window, BLACK, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 5)
        
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == self.board.agent_list[0]:
            self.turn = self.board.agent_list[1]
        elif self.turn == self.board.agent_list[1]:
            self.turn = self.board.agent_list[2]
        else:
            self.turn = self.board.agent_list[0]
            self.round += 1


    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        moves = self.board.get_valid_moves(self.turn)
        row, col = rnd.choice(list(moves.values()))
        self.board.move(self.turn, row, col)
        self.change_turn()