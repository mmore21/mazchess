import algorithm

class Agent:
    def __init__(self, depth):
        self.depth = depth

    def get_move(self, legal_moves):
        return algorithm.calculate_best_move(legal_moves, self.depth)