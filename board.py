import pygame
from constants import *
from agent import Runner, Chaser


class Board:
    def __init__(self):
        self.board = []
        self.agent_list = []
        self.create_board()
        self.positions = {}
        self.black_cells = 0

    def draw_squares(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(window, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)


    def move(self, agent, row, col):
        if self.board[row][col] != 0 and (row, col) != (agent.row, agent.col) and self.board[row][col] != agent:
            print("{} hit {}******************".format(agent.name, self.get_agent(row, col).name))
            
        print("{}: {}{} {}{}".format(agent.name, chr(97+agent.col), agent.row, chr(97+col), row))
        self.board[agent.row][agent.col], self.board[row][col] = self.board[row][col], self.board[agent.row][agent.col]
        agent.move(row, col)

    
    def get_agent(self, row, col):
        return self.board[row][col]


    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0 and col == 0:
                    R = Runner(row, col, R_IMAGE, "R")
                    self.board[row].append(R)
                    self.agent_list.append(R)
                elif row == 7 and col == COLS-2:
                    C1 = Chaser(row, col, C1_IMAGE, "C1")
                    self.board[row].append(C1)
                    self.agent_list.append(C1)
                elif row == 7 and col == COLS-1:
                    C2 = Chaser(row, col, C2_IMAGE, "C2")
                    self.board[row].append(C2)
                    self.agent_list.append(C2)
                else:
                    self.board[row].append(0)
                

    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                agent = self.board[row][col]
                if agent != 0:
                    agent.draw(window)


    def winner(self):
        return None


    def manhattan_distance(self, a, b):
        # calculates manhattan distance between agents
	    return sum(abs(e1-e2) for e1, e2 in zip(a,b))   
 

    def evaluate(self):
        Xs1 = [self.agent_list[0].row, self.agent_list[1].row]
        Ys1 = [self.agent_list[0].col, self.agent_list[1].col]
        
        d1 = self.manhattan_distance(self, Xs1, Ys1)
        
        Xs2 = [self.agent_list[0].row, self.agent_list[2].row]
        Ys2 = [self.agent_list[0].col, self.agent_list[2].col]
        
        d2 = self.manhattan_distance(self, Xs2, Ys2)
        
        max_d = d1 > d2 and d1 or d2
        
        return max_d
        

    def get_all_agents(self):
        self.positions = {}
        for row in self.board:
            for agent in row:
                if agent != 0:
                    self.positions.update({agent.name: (agent.row, agent.col)})
        
        return self.positions


    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row + 1

        if left > -1 and left < COLS:
            moves.update({"left":(piece.row, left)})
        if right > -1 and right < COLS:
            moves.update({"right":(piece.row, right)})
        if up > -1 and up < ROWS:
            moves.update({"up":(up, piece.col)})
        if down > -1 and down < ROWS:
            moves.update({"down":(down, piece.col)})
            
        moves.update({"stay":(piece.row, piece.col)})
        return moves
    
    
"""

    def get_positions(self):
        self.positions = {}
        for i in range(len(self.agent_list)):
            self.positions.update({self.agent_list[i]:(self.agent_list[i].row, self.agent_list[i].col)})

        return self.positions
        
"""
