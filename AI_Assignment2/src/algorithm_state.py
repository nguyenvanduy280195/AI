import math

import DISTIONARY as dist
import utilities as util


class State:
    def __init__(self, board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent, is_left, idx):
        self.board = board

        self.has_quan_1 = has_quan_1
        self.has_quan_2 = has_quan_2

        self.player_score = player_score
        self.ai_score = ai_score

        self.ai_turn = ai_turn

        self.level = level
        self.evalue = dist.NaN

        self.parent = parent
        self.states = []

        self.is_left = is_left
        self.idx = idx

    def isLeaf(self):
        if self.states == []:
            return True
        return False

    def generateStates(self, ai_turn):
        # Should check self.states == [] ?
        for i in range(0, 10, 1):
            state = self.turn(i / 2, not bool(i % 2), ai_turn)
            # if exist x: x <- self.states and x is None:
            #   skip == continue for
            if state is None:
                continue

            if state.level == dist.TREE_LEVEL:
                state.evalue = state.evalution()

            self.states.append(state)

    def turn(self, idx, is_left, ai_turn):
        # khong the rai~ qua^n -> xuat qua^n
        if not canDivide(self.board, self.ai_turn):
            score = self.ai_score if self.ai_turn else self.player_score
            a_new_board, a_new_score = comePeople(self.board, score, self.ai_turn)

            self.board = a_new_board

            if self.ai_turn:
                self.ai_score = a_new_score
            else:
                self.player_score = a_new_score

        # rai~ quan
        # ai_turn = True -> not ai_turn = False
        # idx + int(not ai_turn)*6 = idx
        # ai_turn = False -> not ai_turn = True
        # idx + int(not ai_turn)*6 = idx + 6
        square_idx = idx + int(not ai_turn) * 6
        result = divide(self.board, square_idx, is_left, self.has_quan_1, self.has_quan_2)

        if result is None:
            # idx khong hop le
            #   idx == QUAN_INDEX
            #   board[idx] == 0
            return result

        b_new, d_score, quan_1, quan_2 = result
        board = b_new
        has_quan_1 = quan_1
        has_quan_2 = quan_2

        player_score = self.player_score + int(not ai_turn) * d_score
        ai_score = self.ai_score + int(ai_turn) * d_score

        if util.endgame(b_new):
            a, p = clearBoard(b_new)
            ai_score += a
            player_score += p
            b_new = dist.BOARD_NONE

        parent = self
        level = self.level + 1

        return State(board, has_quan_1, has_quan_2, player_score, ai_score, ai_turn, level, parent, is_left, idx)

    def evalution(self):
        """
        delta_ai = ai(i) - ai(i - 1)
        delta_player = player(i) - player(i - 1)

        :return: sigma (delta_ai - delta_player)
        """
        if self.parent == None:
            return self.ai_score - self.player_score
        return self.ai_score - self.player_score + self.parent.evalution()

    def maxState(self):
        if not math.isnan(self.evalue):
            return self.evalue
        max = -dist.INF
        for state in self.states:
            if math.isnan(state.evalue):
                state.evalue = state.minState()

            if state.evalue > max:
                max = state.evalue

        return max

    def minState(self):
        if not math.isnan(self.evalue):
            return self.evalue
        min = dist.INF
        for state in self.states:
            if math.isnan(state.evalue):
                state.evalue = state.minState()

            if state.evalue < min:
                min = state.evalue

        return min


def divide(board, idx, is_left, has_quan_1, has_quan_2):
    """
    rai~ quan
    :param board:
    :param idx: [0, 11]
    :param is_left:
    :return: None if idx == INDEX_QUAN or board[idx] == 0 else not None
    """
    if idx is dist.QUAN_1_INDEX or idx is dist.QUAN_2_INDEX:
        return None

    if board[util.scaleIdx(idx)] == 0:
        return None
    # init a_new_board
    a_new_board = board[:]
    score = 0
    jdx = idx
    step = -1 if is_left else 1
    quan_1 = has_quan_1
    quan_2 = has_quan_2

    while True:
        hand = step * a_new_board[jdx]
        a_new_board[jdx] = 0
        # init loop - for
        begin = jdx + step
        end = begin + hand
        for i in range(begin, end, step):
            idx_new = util.scaleIdx(i)
            a_new_board[idx_new] += dist.DAN_SCORE

        # neu o tiep theo la o quan thi khong duoc rai tiep -> ket thuc luot
        if util.scaleIdx(end) is dist.QUAN_1_INDEX or util.scaleIdx(end) is dist.QUAN_2_INDEX:
            break

        # an qua^n -> ket thuc luot
        if a_new_board[util.scaleIdx(end)] is 0:
            run = util.scaleIdx(end)
            # an qua^n lien tiep (combo)
            while a_new_board[run] is 0 and a_new_board[util.scaleIdx(run + step)] is not 0:
                score += a_new_board[util.scaleIdx(run + step)]
                # an qua^n tai da^u quan 1
                if (util.scaleIdx(run + step) == dist.QUAN_1_INDEX and quan_1):
                    score += dist.QUAN_SCORE
                    quan_1 = False

                # an qua^n tai da^u quan 2
                if (util.scaleIdx(run + step) == dist.QUAN_2_INDEX and quan_2):
                    score += dist.QUAN_SCORE
                    quan_2 = False

                a_new_board[util.scaleIdx(run + step)] = 0
                run = util.scaleIdx(run + step + step)
            break  # -> ket thuc luot

        jdx = util.scaleIdx(end)

    return a_new_board, score, quan_1, quan_2


def canDivide(board, ai_turn):
    """
    kiem tra nguoi choi co kha nang rai~ quan khong

    :param board: list[12]
    :param ai_turn: bool
    :return:
        True    : co kha nang rai~ quan
        False   : khong co kha nang rai~ quan
    """

    # if ai_turn:
    #   [x + 6 * (not int(ai_turn)) for x in range(0, 5, 1)] = [0, 1, 2, 3, 4]
    # else:
    #   [x + 6 * (not int(ai_turn)) for x in range(0, 5, 1)] = [6, 7, 8, 9, 10]

    # idx_squares_control = [x + 6 * (not int(ai_turn)) for x in range(0, 5, 1)]

    # length_idx_squares_control = len(idx_squares_control)

    # begin = idx_squares_control[0]
    # end = idx_squares_control[length_idx_squares_control - 1] + 1

    begin = 6 * (not int(ai_turn))
    end = begin + 5

    squares_control = board[begin: end]

    if squares_control.count(0) == 5:
        return False
    return True



def comePeople(board, score, ai_turn):
    # type: (list, int, bool) -> list, int
    """
    xuat quan khi khong the rai quan

    :param board:
    :param score:
    :param ai_turn:
    :return:
    """

    idx_squares_control = [x + 6 * (not int(ai_turn)) for x in range(0, 5, 1)]
    for i in idx_squares_control:
        board[i]+=1

    return board, score - 5

def clearBoard(board):
    ai = board[0:5]
    player = board[6:11]
    aiDeltaScore = reduce(lambda x, y: x + y, ai)
    playerDeltaScore = reduce(lambda x, y: x + y, player)

    return aiDeltaScore, playerDeltaScore
