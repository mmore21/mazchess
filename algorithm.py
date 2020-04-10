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

# initial call
# alphabeta(origin, depth, float('-inf'), float('inf'), True)