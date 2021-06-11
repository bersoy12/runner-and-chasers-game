import pygame
from constants import *
from agent import *


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
                pygame.draw.rect(window, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
                
            
    def collision(self, row, col, agent):
        print("{} hit {}".format(agent.name, self.get_agent(row, col).name))
        

    def move(self, agent, row, col):
        if self.board[row][col] != 0 and (row, col) != (agent.row, agent.col) and self.board[row][col] != agent:
            self.collision(row, col, agent)
            
        self.board[agent.row][agent.col], self.board[row][col] = self.board[row][col], self.board[agent.row][agent.col]
        agent.move(row, col)

    def get_agent(self, row, col):
        return self.board[row][col]

    def create_board(self):
        r_r = int(input("input row of RUNNER: "))
        c_r = int(input("input column of RUNNER: "))
        r_c1 = int(input("input row of CHASER1: "))
        c_c1 = int(input("input column of CHASER1: "))
        r_c2 = int(input("input row of CHASER2: "))
        c_c2 = int(input("input column of CHASER2: "))
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == r_r and col == c_r:
                    R = Runner(row, col, RED, "R")
                    self.board[row].append(R)
                    self.agent_list.append(R)
                elif row == r_c1 and col == c_c1:
                    C1 = Chaser(row, col, BLUE, "C1")
                    self.board[row].append(C1)
                    self.agent_list.append(C1)
                elif row == r_c2 and col == c_c2:
                    C2 = Chaser(row, col, BLUE, "C2")
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
        return sum(abs(e1 - e2) for e1, e2 in zip(a, b))

    def evaluate(self):
        r = [self.agent_list[0].row, self.agent_list[0].col]
        c1 = [self.agent_list[1].row, self.agent_list[1].col]
        c2 = [self.agent_list[2].row, self.agent_list[2].col]

        d1 = self.manhattan_distance(r, c1)
        d2 = self.manhattan_distance(r, c2)
        
        if d1 > d2:
            return d1, d2
        else:
            return d2, d1     

    def get_all_agents(self):
        self.positions = {}
        for row in self.board:
            for agent in row:
                if agent != 0:
                    self.positions.update({agent: (agent.row, agent.col)})

        return self.positions

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row + 1

        if -1 < left < COLS:
            moves.update({"left": (piece.row, left)})
        if -1 < right < COLS:
            moves.update({"right": (piece.row, right)})
        if -1 < up < ROWS:
            moves.update({"up": (up, piece.col)})
        if -1 < down < ROWS:
            moves.update({"down": (down, piece.col)})

        moves.update({"stay": (piece.row, piece.col)})
        return moves
