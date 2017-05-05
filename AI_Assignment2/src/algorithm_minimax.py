import algorithm_state as s
import DISTIONARY as dist
import algorithm_queue as q



class Minimax:
    def __init__(self, board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn):
        # board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent

        ai_turn = ai_turn
        level = 0
        parent = None

        self.tree = s.State(board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent, None, None)

    def minimax(self):
        queue = q.Queue()
        queue.enqueue(self.tree)
        while not queue.isEmpty():
            run = queue.dequeue()

            if run.level < dist.TREE_LEVEL:
                turn = run.ai_turn if run.level == 0 else not run.ai_turn
                run.generateStates(turn)

            for state in run.states:
                queue.enqueue(state)


        for s in self.tree.states:
            s.evalue = s.maxState()

        self.tree.evalue = self.tree.maxState()

        sol = []
        run = self.tree
        sol.append(run)


        for state in run.states:
            if run.evalue == state.evalue:
                run = state
                sol.append(state)
                continue

        return sol

    def printTree(self):
        queue = q.Queue()
        queue.enqueue(self.tree)
        while not queue.isEmpty():
            run = queue.dequeue()

            print '__________________________________________________'
            # print 'board', run.board
            # print 'has_quan_1', run.has_quan_1
            # print 'has_quan_2', run.has_quan_2
            # print 'player_score', run.player_score
            # print 'ai_score', run.ai_score
            print 'ai_turn', run.ai_turn
            # print 'idx', run.idx
            # print 'is_left', run.is_left
            print 'level', run.level

            for state in run.states:
                queue.enqueue(state)
        pass