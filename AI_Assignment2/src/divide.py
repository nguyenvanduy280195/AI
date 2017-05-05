import DISTIONARY as dist
import utilities as util

def divide(chessqs, chessQs, iChessq, is_left):
    """
    rai~ quan
    :param chessqs:
    :param chessQs:
    :param iChessq:
    :param is_left:
    :return:
    """
    if iChessq is dist.QUAN_1_INDEX or iChessq is dist.QUAN_2_INDEX:
        return None

    if chessqs[util.scaleIdx(iChessq)].nquan == 0:
        return None
    # init return
    step = 1 if is_left else -1
    jChessq = iChessq
    deltaScore = 0
    hasQuan1 = chessQs[0].hasQuan
    hasQuan2 = chessQs[1].hasQuan

    while True:
        hand = step * chessqs[jChessq].nquan
        chessqs[jChessq].nquan = 0
        # init loop - for
        begin = jChessq + step
        end = begin + hand
        for i in range(begin, end, step):
            chessqs[util.scaleIdx(i)].nquan += dist.DAN_SCORE
        # neu o tiep theo la quan thi khong duoc rai tiep
        end = util.scaleIdx(end)
        if end is dist.QUAN_1_INDEX or end is dist.QUAN_2_INDEX:
            break

        # an quan -> ket thuc luot
        if chessqs[end].nquan is 0:
            run = end
            nextRun = util.scaleIdx(run + step)
            # an quan lien tiep (combo)
            while chessqs[run].nquan is 0 and chessqs[nextRun].nquan is not 0:
                deltaScore += chessqs[nextRun].nquan
                # an quan tai dau quan 1
                if nextRun is dist.QUAN_1_INDEX and chessQs[0].hasQuan:
                    deltaScore += dist.QUAN_SCORE
                    hasQuan1 = False

                # an quan tai dau quan 2
                if nextRun is dist.QUAN_2_INDEX and chessQs[1].hasQuan:
                    deltaScore += dist.QUAN_SCORE
                    hasQuan2 = False

                chessqs[nextRun].nquan = 0
                run = util.scaleIdx(run + step + step)
            break  # -> ket thuc an quan -> ket thuc luot
        jChessq = end
    return deltaScore, hasQuan1, hasQuan2


def canDivide(chessq, ai_turn):
    """
    kiem tra nguoi choi co kha nang rai~ quan khong
    :param chessq:
    :param ai_turn:
    :return:
    """
    begin = 6 * (not int(ai_turn))
    end = begin + 5

    squares_control = chessq[begin: end]

    if squares_control.count(0) == 5:
        return False
    return True


def comePeople(chessq, score, ai_turn):
    """
    xuat quan khi khong the rai quan
    :param chessq:
    :param score:
    :param ai_turn:
    :return:
    """

    idx_squares_control = [x + 6 * (not int(ai_turn)) for x in range(0, 5, 1)]
    for i in idx_squares_control:
        chessq[i].nquan += 1

    return score - 5


def clearBoard(board):
    ai = board[0:5]
    player = board[6:11]
    aiDeltaScore = reduce(lambda x, y: x + y, ai)
    playerDeltaScore = reduce(lambda x, y: x + y, player)

    return aiDeltaScore, playerDeltaScore
