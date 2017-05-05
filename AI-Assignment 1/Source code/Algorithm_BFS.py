import Algorithm_BFS_Queue as bfsQueue
import Algorithm_TreeState as ts

class BFS(object):
    def __init__(self, board):
        self.tree = ts.Tree(board, None)

    def traversalStateTree(self):
        queue = bfsQueue.Queue()
        queue.enqueue(self.tree)
        count = 0
        while not queue.isEmpty():
            tree = queue.dequeue()
            count += 1

            if ts.isDuplicateState(tree,tree.parent):
                continue

            #Players is killed by mummy
            if tree.playerIsKilled:
                continue

            #If node is leaf, node will generate TreeState
            if tree.isLeaf():
                tree.generateStateTree()

            #Goal
            if tree.player2Goal():
                return tree, count

            if tree.noMove is not None:
                queue.enqueue(tree.noMove)
            if tree.goDown is not None:
                queue.enqueue(tree.goDown)
            if tree.goUp is not None:
                queue.enqueue(tree.goUp)
            if tree.goRight is not None:
                queue.enqueue(tree.goRight)
            if tree.goLeft is not None:
                queue.enqueue(tree.goLeft)
            pass

        return None, count

    pass