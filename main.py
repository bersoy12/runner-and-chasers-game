import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from game import Game
from minimax import minimax

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner and Chasers Game")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(window)
    # round = int(input("Enter the number of turns: "))
    # black_cell_number = int(input("Enter the number of black cells on the board: "))
    # black_cell_number = game.board.black_cells
    
    while run and game.round < 20:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game.turn.name == "R":
                game.ai_move(game.board)
                """
                value, new_board = minimax(game.get_board(), 2, game.turn, game)
                game.ai_move(new_board)
                """
            else:
                # value, new_board = minimax(game.get_board(), 2, game.turn, game)
                game.ai_move(game.board)
                """
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                """
         
        game.update()
        
        
    pygame.quit()


if __name__ == "__main__":
    main()
    