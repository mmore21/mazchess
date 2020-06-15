import chess

class Agent:
    def __init__(self, depth):
        self.depth = depth
        self.board = chess.Board()

    def add_move(self, beg_pos, end_pos):
        raw_human_move = beg_pos + end_pos
        print(raw_human_move)
        human_move = chess.Move.from_uci(raw_human_move)
        self.board.push(human_move)

        if self.board.is_game_over():
            print("Checkmate (White).")
            self.board = chess.Board()

        ai_move = self.negamax_root(3)
        print(ai_move)
        self.board.push(ai_move)

        if self.board.is_game_over():
            print("Checkmate (Black).")
            self.board = chess.Board()

        return ai_move


    def evaluate(self):
        wp = len(self.board.pieces(chess.PAWN, chess.WHITE))
        bp = len(self.board.pieces(chess.PAWN, chess.BLACK))
        wn = len(self.board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(self.board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(self.board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(self.board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(self.board.pieces(chess.ROOK, chess.WHITE))
        br = len(self.board.pieces(chess.ROOK, chess.BLACK))
        wq = len(self.board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(self.board.pieces(chess.QUEEN, chess.BLACK))

        # Note: These values do not include the king
        material_score = 9*(wq - bq) + 5*(wr - br) + 3*(wb - bb + wn - bn) + 1*(wp - bp)

        num_white_pieces = wp + wn + wb + wr + wq
        num_black_pieces = bp + bn + bb + br + bq
        mobility_score = self.board.legal_moves.count() * .01

        if self.board.turn == True:
            who2move = 1
        else:
            who2move = -1

        score = (material_score + mobility_score) * who2move

        return score

    def negamax_root(self, depth):
        max = -99999
        best_move = None


        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.negamax(depth - 1)
            self.board.pop()
            if score > max:
                best_move = move
                max = score
                
        print(max)
        return best_move

    def negamax(self, depth):
        if depth == 0:
            score = self.evaluate()
            return score

        max = -99999

        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.negamax(depth - 1)
            self.board.pop()
            if score > max:
                max = score
                
        return max