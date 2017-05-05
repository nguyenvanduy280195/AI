import Algorithm_DFS_Stack
import Algorithm_TreeState as ts

class DFS(object):
    def __init__(self, board):
        self.tree = ts.Tree(board, None)

    def traversalStateTree(self):
        stack = Algorithm_DFS_Stack.Stack()
        stack.push(self.tree)
        count = 0
        while not stack.isEmpty():
            node = stack.pop()
            count += 1
            #bi trung -> skip
            if ts.isDuplicateState(node, node.parent):
                continue

            #player bi mummy giet -> skip
            if node.playerIsKilled:
                continue

            #node la node la sinh cay
            if node.isLeaf():
                node.generateStateTree()

            if node.player2Goal():
                return node, count

            if node.noMove is not None:
                stack.push(node.noMove)
            if node.goDown is not None:
                stack.push(node.goDown)
            if node.goUp is not None:
                stack.push(node.goUp)
            if node.goRight is not None:
                stack.push(node.goRight)
            if node.goLeft is not None:
                stack.push(node.goLeft)
            pass

        return None, count

    pass
