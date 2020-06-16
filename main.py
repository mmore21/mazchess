import chess
import agent

def evaluate():
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    # Note: These values do not include the king
    material_score = 9*(wq - bq) + 5*(wr - br) + 3*(wb - bb + wn - bn) + 1*(wp - bp)

    num_white_pieces = wp + wn + wb + wr + wq
    num_black_pieces = bp + bn + bb + br + bq
    mobility_score = board.legal_moves.count() * .01

    if board.turn == True:
        who2move = 1
    else:
        who2move = -1

    score = (material_score + mobility_score) * who2move

    return score

def negamax_root(depth):
    max = -99999
    best_move = None

    for move in board.legal_moves:
        board.push(move)
        score = -negamax(depth - 1)
        board.pop()
        if score > max:
            best_move = move
            max = score
            
    print(max)
    return best_move

def negamax(depth):
    if depth == 0:
        score = evaluate()
        return score

    max = -99999

    for move in board.legal_moves:
        board.push(move)
        score = -negamax(depth - 1)
        board.pop()
        if score > max:
            max = score
            
    return max

# Create a new game
ai = agent.Agent(depth=3)
board = chess.Board()
playing = True

print("################\nDEMO CLI VERSION\n################\n")

it = 0

while playing:
    # Display board
    print(board)

    # Get human move
    print(board.legal_moves)
    human_move = input("Enter move:")

    # Exit the game
    if human_move == 'exit':
        break

    try:
        board.push_san(human_move)
    except ValueError:
        print("Invalid Move")
        print(board.legal_moves)
        continue

    # Check endgame
    if board.is_game_over():
        print("Checkmate. White Wins.")
        break

    # Display board
    print(board)

    # Get AI move
    ai_move = negamax_root(3)
    if board.piece_type_at(ai_move.from_square) == chess.PAWN and chess.square_rank(ai_move.to_square) == 0:
        print("Promotion")
        ai_move.promotion = chess.QUEEN
    print(ai_move)

    try:
        board.push(ai_move)
    except ValueError:
        print("Error: AI Predicted Invalid Move")

    # Check endgame
    if board.is_game_over():
        print("Checkmate. Black Wins.")
        break