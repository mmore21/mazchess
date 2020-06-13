import chess
import algorithm # Temporary until Agent class complete
import agent

def get_move_info(legal_moves):
    for move in list(legal_moves):
        move_str = move.uci().lower()
        file_index = chess.FILE_NAMES.index(move_str[0])
        rank_index = chess.RANK_NAMES.index(move_str[1])
        piece = board.piece_at(chess.square(file_index=file_index, rank_index=rank_index))
        print(move_str, file_index, rank_index, piece)
    print(legal_moves)

# Create a new game
ai = agent.Agent(depth=1)
board = chess.Board()
playing = True

while playing:
    # Display board
    print(board)
    print(board.turn)

    #get_move_info(board.legal_moves)

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

    # Display board
    print(board)
    print(board.turn)

    # Get AI move
    ai_move = ai.get_move(list(board.legal_moves))
    print(ai_move, type(ai_move))

    try:
        board.push_san(ai_move)
    except ValueError:
        print("Error: AI Predicted Invalid Move")