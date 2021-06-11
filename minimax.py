from copy import deepcopy
import pygame

WHITE = (255, 255, 255)
RED = (255,0,0)

def minimax(board, depth, player, game):
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board
    
    if player.color == RED:
        maxEval = float('-inf')
        best_move = None
        
        for move in get_all_moves(game.board, player, game):
            evaluation = minimax(move, depth-1, player, game)[0][0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    
    else:
        minEval = float('inf')
        best_move = None
        
        for move in get_all_moves(game.board, player, game):
            evaluation = minimax(move, depth-1, player, game)[0][1]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(piece, move, board, game):
    board.move(piece, move[0], move[1])
    return board


def get_all_moves(board, agent, game):   
    moves = []      # boardların listesi
    
    for piece in board.get_all_agents():        # 1. runnerı alacak, 2. chaser1 i alacak, sonra chaser2 yi alacak
        valid_moves = board.get_valid_moves(agent)
        moves_array = [valid_moves[key] for key in valid_moves.keys()]  # [(1,0), (2,3), (1,4)] gibi bir liste
        for i in range(len(moves_array)):
            # moves_arrayin içindeki her kordinatı simulate_move ediyoruz
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board) # geçici bir board yarattık
            temp_agent = temp_board.get_agent(agent.row, agent.col)
            new_board = simulate_move(temp_agent, moves_array[i], temp_board, game)
            moves.append(new_board)
            
    return moves



def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.window)
    pygame.draw.circle(game.window, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves)
    pygame.display.update()
    pygame.time.delay(10)
