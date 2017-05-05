import Utilities


class Tree:
    def __init__(self, board, parent):
        self.board = board
        self.parent = parent
        self.playerIsKilled = False
        self.mummy_move = []
        self.goLeft = None
        self.goRight = None
        self.goUp = None
        self.goDown = None
        self.noMove = None
        pass

    def isLeaf(self):
        return self.goLeft is None and \
               self.goRight is None and \
               self.goUp is None and \
               self.goDown is None and \
               self.noMove is None

    def getGoal(self):
        n = len(self.board)
        for i in range(n):
            if self.board[0][i] is 'g':
                return 0, i
            if self.board[n - 1][i] is 'g':
                return (n - 1), i
            if self.board[i][0] is 'g':
                return i, 0
            if self.board[n - 1][0] is 'g':
                return n - 1, 0

        return -1, -1

    def getPlayer(self):
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i][j] is 'p':
                    return i, j
        return -1, -1

    def getMummy(self):
        """
        find mummy in map
        :return: index of mummy in map
        """
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i][j] is 'm':
                    return i, j
        return -1, -1

    def playersMove(self, direction):

        r, c = self.getPlayer()
        # left
        if direction == 'left':
            if self.board[r][c - 1] == '-':
                left = self.board[:]
                rLeft = Utilities.swapIn1Arr(left[r], c, c - 2)
                left[r] = rLeft
                return left, True

        # right
        elif direction == 'right':
            if self.board[r][c + 1] == '-':
                right = self.board[:]
                rRight = Utilities.swapIn1Arr(right[r], c, c + 2)
                right[r] = rRight
                return right, True
        # up
        elif direction == 'up':
            if self.board[r - 1][c] == '-':
                up = self.board[:]
                rUp, rUp2 = Utilities.swapIn2Arr(up[r], up[r - 2], c)
                up[r] = rUp
                up[r - 2] = rUp2
                return up, True
        # down
        elif direction == 'down':
            if self.board[r + 1][c] == '-':
                down = self.board[:]
                rDown, rDown2 = Utilities.swapIn2Arr(down[r], down[r + 2], c)
                down[r] = rDown
                down[r + 2] = rDown2
                return down, True
        elif direction == 'nomove':
            noMove = self.board[:]
            return noMove, True
        return self.board[:], False

    def mummyMove(self, direction):
        r, c = self.getMummy()
        # left
        if direction == 'left':
            if self.board[r][c - 2] == 'p' and self.board[r][c - 1] == '-':
                self.playerIsKilled = True
                return None, False
            if self.board[r][c - 1] == '-':
                left = self.board[:]
                rLeft = Utilities.swapIn1Arr(left[r], c, c - 2)
                left[r] = rLeft
                return left, True
        # right
        elif direction == 'right':
            if self.board[r][c + 2] == 'p' and self.board[r][c + 1] == '-':
                self.playerIsKilled = True
                return None, False

            if self.board[r][c + 1] == '-':
                right = self.board[:]
                rRight = Utilities.swapIn1Arr(right[r], c, c + 2)
                right[r] = rRight
                return right, True
        # up
        elif direction == 'up':
            if self.board[r - 2][c] == 'p' and self.board[r - 1][c] == '-':
                self.playerIsKilled = True
                return None, False

            if self.board[r - 1][c] == '-':
                up = self.board[:]
                rUp, rUp2 = Utilities.swapIn2Arr(up[r], up[r - 2], c)
                up[r] = rUp
                up[r - 2] = rUp2
                return up, True
        # down
        elif direction == 'down':
            if self.board[r + 2][c] == 'p' and self.board[r + 1][c] == '-':
                self.playerIsKilled = True
                return None, False

            if self.board[r + 1][c] == '-':
                down = self.board[:]
                rDown, rDown2 = Utilities.swapIn2Arr(down[r], down[r + 2], c)
                down[r] = rDown
                down[r + 2] = rDown2
                return down, True

        return self.board[:], False

    def player2Goal(self):
        rp, cp = self.getPlayer()
        rg, cg = self.getGoal()

        if (rp + 1 is rg or rp is rg + 1) and cp is cg:
            return True
        if (cp + 1 is cg or cp is cg + 1) and rp is rg:
            return True
        return False

    def mummyMoveX(self, cm, cp):
        if cp > cm:
            return self.mummyMove('right')
        elif cp < cm:
            return self.mummyMove('left')
        return self.board[:], False

    def mummyMoveY(self, rm, rp):
        if rp > rm:
            return self.mummyMove('down')
        elif rp < rm:
            return self.mummyMove('up')
        return self.board[:], False

    def mummyMove1(self, rm, cm, rp, cp):
        if self.playerIsKilled:
            return None

        if cp is not cm:
            b, f = self.mummyMoveX(cm, cp)
            if f:
                if cp > cm:
                    self.mummy_move.append('r')
                elif cp < cm:
                    self.mummy_move.append('l')
                return b
            else:
                b, f = self.mummyMoveY(rm, rp)
                if f:
                    if rp > rm:
                        self.mummy_move.append('d')
                    elif rp < rm:
                        self.mummy_move.append('u')
                    return b
                else:
                    return None
        else:
            b, f = self.mummyMoveY(rm, rp)
            if f:
                if rp > rm:
                    self.mummy_move.append('d')
                elif rp < rm:
                    self.mummy_move.append('u')
                return b
            else:
                return None
        pass

    def mummyMove2(self):
        rm, cm = self.getMummy()
        rp, cp = self.getPlayer()
        b1 = self.mummyMove1(rm, cm, rp, cp)
        if self.playerIsKilled:
            return
        if b1 is not None:
            self.board = b1

            rm, cm = self.getMummy()
            rp, cp = self.getPlayer()
            b2 = self.mummyMove1(rm, cm, rp, cp)

            if b2 is not None:
                self.board = b2
            else:
                self.mummy_move.append('n')
        else:
            self.mummy_move.append('n')
            self.mummy_move.append('n')

    def generateStateTree(self):
        self.goLeft = generateState(self, 'left')
        self.goRight = generateState(self, 'right')
        self.goUp = generateState(self, 'up')
        self.goDown = generateState(self, 'down')
        self.noMove = generateState(self, 'nomove')

    def printBoard(self):
        for b in self.board:
            print b
        pass

    pass


def isDuplicateState(node, parent):
    '''
    kiem tra trang thai cua no co trung voi cha cua no khong
    :return:
    '''
    if parent == None:
        return False

    child_player = node.getPlayer()
    child_mummy = node.getMummy()
    parent_player = parent.getPlayer()
    parent_mummy = parent.getMummy()

    if child_player == parent_player and child_mummy == parent_mummy:
        return True

    return isDuplicateState(node, parent.parent)


def generateState(parent, direction):
    child = Tree(parent.board, parent)
    # Player's moving
    board, logic = child.playersMove(direction)

    if not logic:
        return None
    else:
        child.board = board
    # Mummy's moving
    child.mummyMove2()
    if child.playerIsKilled:
        return None
    return child
