import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from game import Game
from minimax import minimax
from copy import deepcopy
from constants import *

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner and Chasers Game")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def printArray(arr):
    for row in arr:
        for item in row:
            print("{}".format(item), end = " ")
        print("")
    print("\n")


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(window)
    # round = int(input("Enter the number of turns: "))
    # black_cell_number = int(input("Enter the number of black cells on the board: "))
    # black_cell_number = game.board.black_cells
    
    while run and game.round < 20:
        clock.tick(60)
        
        print("after {}'s play:\n".format(game.turn.name))
        if game.turn.name == "R":
            value, new_board = minimax(game.get_board(), 1, game.turn, game)
            game.ai_move(new_board)
            
        
        printArray(game.board.board)
        print("after {}'s play:\n".format(game.turn.name))    
        if game.turn.name == "C1":
            value, new_board = minimax(game.get_board(), 1, game.turn, game)
            game.ai_move(new_board)
            
            
        printArray(game.board.board)
        
        print("after {}'s play:\n".format(game.turn.name))
        if game.turn.name == "C2":
            value, new_board = minimax(game.get_board(), 1, game.turn, game)
            game.ai_move(new_board)
            
        printArray(game.board.board)
        """
        game.ai_move()
        """
        if game.winner() != None:
            print(game.winner())
            run = False
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            
            """
                    
        game.round += 1
        game.update()
        
        
    pygame.quit()


if __name__ == "__main__":
    main()
    