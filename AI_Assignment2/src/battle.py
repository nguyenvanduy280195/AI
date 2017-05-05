import algorithm_minimax as am
import DISTIONARY as dist

import chessboard
import chess
import arrow
import divide



class Battle():
    def __init__(self):
        # chessboard
        self.chessboard = chessboard.Chessboard()
        # chess
        self.chessqs = chess.createChessqs()
        self.chessQs = chess.createChessQs()
        # arrow
        self.arrowLeft = None
        self.arrowRight = None
        #
        self.idxed = -1

    def draw(self, screen):
        """

        :param screen:
        :return:
        """
        # chessboard
        self.chessboard.draw(screen)
        # chess
        for i in self.chessqs: i.draw(screen)
        for i in self.chessQs: i.draw(screen)
        # draw arrow
        if self.arrowLeft: self.arrowLeft.draw(screen)
        if self.arrowRight: self.arrowRight.draw(screen)

    def update(self):
        """

        :return:
        """
        self.chessboard.update()
        for i in self.chessqs: i.update()
        for i in self.chessQs: i.update()


    def event(self, e):
        """

        :return:
        """

        if self.arrowLeft:
            if self.arrowLeft.rect.collidepoint(e.pos):
                del self.arrowLeft
                del self.arrowRight
                self.arrowLeft = None
                self.arrowRight = None
                # player_turn
                self.chessboard.scorePlayer += self.turn(aiTurn=False, isLeft=True)
                # ai_turn
                self.idxed, isLeft = self.runAlgorithm()
                print 'idxed, isLeft =', self.idxed, isLeft
                self.chessboard.scoreAI += self.turn(aiTurn=True, isLeft=isLeft)

        if self.arrowRight:
            if self.arrowRight.rect.collidepoint(e.pos):
                del self.arrowLeft
                del self.arrowRight
                self.arrowLeft = None
                self.arrowRight = None
                # player_turn
                self.turn(aiTurn=False, isLeft=False)
                # ai_turn
                self.idxed, isLeft = self.runAlgorithm()

                self.turn(aiTurn=True, isLeft=isLeft)

        begin = len(self.chessqs) / 2  # 12 / 2 = 6
        end = begin * 2 - 1  # 6 * 2 - 1 = 11
        for i in range(begin, end, 1):
            if i == dist.QUAN_1_INDEX or i == dist.QUAN_2_INDEX:
                continue
            if self.chessqs[i].rect.collidepoint(e.pos):
                self.idxed = i

                x1 = 250 + i * dist.SQUARE_WIDTH - dist.SQUARE_WIDTH / 3
                x2 = 250 - dist.SQUARE_WIDTH / 3 + (4 - i % 6) * dist.SQUARE_WIDTH
                x = x1 if i < 6 else x2
                y = 180 + i / 6 * dist.SQUARE_HEIGHT + dist.SQUARE_HEIGHT / 3
                self.arrowLeft = arrow.Arrow(x, y, is_left=True)
                self.arrowRight = arrow.Arrow(x + 1.45 * dist.SQUARE_WIDTH, y, is_left=False)

        return self.chessboard.event(e)

    def chessqs2Array(self): return map(lambda x: x.nquan, self.chessqs)

    def turn(self, aiTurn, isLeft):
        if aiTurn:
            if not divide.canDivide(self.chessqs, aiTurn):
                self.chessboard.scoreAI = divide.comePeople(self.chessqs, self.chessboard.scoreAI, aiTurn)

        else:
            if not divide.canDivide(self.chessqs, aiTurn):
                self.chessboard.scorePlayer = divide.comePeople(self.chessqs, self.chessboard.scorePlayer, aiTurn)

        deltaScore, hasQuan1, hasQuan2  = divide.divide(self.chessqs, self.chessQs, self.idxed, isLeft)
        self.chessQs[0].hasQuan = hasQuan1
        self.chessQs[1].hasQuan = hasQuan2

        return deltaScore

    def runAlgorithm(self):
        """

        :return: tuple<int, bool>
        """
        board = self.chessqs2Array()
        has_quan_1 = self.chessQs[0]
        has_quan_2 = self.chessQs[1]
        player_score = self.chessboard.scorePlayer
        ai_score = self.chessboard.scoreAI

        minimax = am.Minimax(board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn=True)
        sol = minimax.minimax()
        return sol[1].idx, sol[1].is_left

    def printChessqs(self):
        for i in self.chessqs:
            print '%2d' % (i.nquan),
        print
