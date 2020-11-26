piece_values = {'p': 10, 'n': 30, 'b': 30, 'r': 50, 'q': 90, 'k': 900}

def calculate_best_move(legal_moves, depth):
    return legal_moves[-1].uci()

def get_piece_value(piece, turn):
    if turn == True:
        return piece_values[piece.lower()]
    else:
        return -piece_values[piece.lower()]

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.terminal:
        return node.val
    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

def evaluate(material_weight, num_white_pieces, num_black_pieces, player_color):
    score = material_weight * (num_white_pieces - num_black_pieces) * player_color
    return score

def negamax(legal_moves, depth):
    if depth == 0:
        return evaluate()

    max = float('-inf')

    for move in legal_moves:
        score = -negamax(legal_moves, depth - 1)
        if score > max:
            max = score
    
    return max

if __name__ == "__main__":
    # Initial call
    # alphabeta(origin, depth, float('-inf'), float('inf'), True)

