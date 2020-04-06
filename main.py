import chess

board = chess.Board()

playing = True
while (playing):
    human_move = input()
    
    print(board)
    playing = False