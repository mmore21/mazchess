import chess
import algorithm 
import agent

def evaluate():
    """Evaluates the current status of the board by computing a score.

    Calculates a total score which is the combination of two scores: the material 
    score and the mobility score. The material score is calculated for each piece
    with a specific weight relative to its importance. The mobility score is
    the number of legal moves for the current turn multiplied by an arbitrary
    threshold. These are then combined and mulitiplied by -1 or 1 depending on
    which player currently holds the turn.

    Returns:
        The score of the current player's board status. Positive scores are for
        white and negative scores are for black.
    """

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

    # This material scoring system does not include the king piece
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

def get_optimal_move():
    max_score = None 
    best_move = None
    
    for move in board.legal_moves:
        board.push(move)
        score = -negamax(depth - 1)
        board.pop()
        if max_score is None or score > max_score:
            best_move = move
            max_score = score

    return (best_move, max_score)


def negamax_root(depth):
    best_move, max_score = get_optimal_move()
           
    print(max_score)

    return best_move

def negamax(depth):
    if depth == 0:
        score = evaluate()
        return score

    max_score = get_optimal_move()[1]

    print(max_score)

    return max_score

if __name__ == "__main__":
    # Create a new game
    ai = agent.Agent(depth=1)
    board = chess.Board()
    playing = True

    it = 0

    while playing:
        # Display board
        print(board)
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
            print(board.legal_moves)
            continue

        # Check endgame
        if board.is_game_over():
            print("Checkmate. White Wins.")
            break

        # Display board
        print(board)
        print(board.turn)

        # Get AI move
        ai_move = negamax_root(depth=3)
        print(ai_move, type(ai_move))

        try:
            board.push(ai_move)
        except ValueError:
            print("Error: AI Predicted Invalid Move")

        # Check endgame
        if board.is_game_over():
            print("Checkmate. Black Wins.")
            break
