import algorithm_state as s
import random as rand

class Random():
    def __init__(self, board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn):
        # board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent

        ai_turn = ai_turn
        level = 0
        parent = None

        self.tree = s.State(board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent, None, None)

    def random(self):
        idxSquaresControl = list(i for i in range(5) if self.tree.board[i] != 0)
        idx = rand.choice(idxSquaresControl)
        is_left = bool(rand.randrange(2))
        state = self.tree.turn(idx,is_left, True)
        return state
