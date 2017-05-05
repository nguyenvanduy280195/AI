import DISTIONARY as dist


def scaleIdx(idx):
    """
    chuan hoa -> [0 - 11]
    :param idx:
    :return:
    """
    if idx > 11:
        return scaleIdx(idx - dist.BOARD_SIZE)
    elif idx < 0:
        return scaleIdx(idx + dist.BOARD_SIZE)
    else:
        return idx


def reverseBoard(board):
    #                 *                 *                     *                 *
    #  0  1  2  3  4  5  6  7  8  9  0  1      0  1  2  3  4  5  6  7  8  9  0  1
    # [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0] -> [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0]
    # [0, 6, 6, 6, 6, 1, 0, 0, 6, 6, 6, 1] -> [0, 0, 6, 6, 6, 1, 0, 6, 6, 6, 6, 1]
    # [3, 0, 0, 0, 0, 5, 4, 3, 9, 2, 9, 3] -> [4, 3, 9, 2, 9, 3, 3, 0, 0, 0, 0, 5]
    a = board[:dist.BOARD_SIZE / 2]
    b = board[dist.BOARD_SIZE / 2:]
    return b + a

def endgame(board):
    if board[dist.QUAN_1_INDEX] == 0 and board[dist.QUAN_2_INDEX] == 0:
        return True
    return False

