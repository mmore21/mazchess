import chess

board = chess.Board()

playing = True
while (playing):
    print(board)
    human_move = input("Enter move:")

    if human_move == 'exit':
        break

    board.push_san(human_move)