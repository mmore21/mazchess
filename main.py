import chess
import algorithm # Temporary until Agent class complete
import agent

# Create a new game
ai = agent.Agent()
board = chess.Board()
playing = True

while playing:

    print(board)
    
    for move in list(board.legal_moves):
        move_str = move.uci().lower()
        file_index = chess.FILE_NAMES.index(move_str[0])
        rank_index = chess.RANK_NAMES.index(move_str[1])
        piece = board.piece_at(chess.square(file_index=file_index, rank_index=rank_index))
        #print(move_str, file_index, rank_index, piece)
    print(board.legal_moves)
    print(board.turn)

    # Get player move
    human_move = input("Enter move:")

    # Exit the game
    if human_move == 'exit':
        break

    try:
        board.push_san(human_move)
    except ValueError:
        print("Invalid Move")
        continue

