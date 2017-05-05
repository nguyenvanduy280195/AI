import label
import DISTIONARY as dist


class ChessQ():
    def __init__(self, x, y):
        self.hasQuan = True

        self.image = dist.imagedist['Q']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.hasQuan:
            self.image = dist.imagedist['Q']
        else:
            self.image = dist.imagedist['N']

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Chessq():
    def __init__(self, nquan, x, y):
        self.nquan = nquan

        self.frames = map(lambda i: dist.imagedist['%sq' % (i)], range(1, 8, 1))

        if self.nquan == 0:
            self.image = dist.imagedist['N']
        else:
            idx = self.nquan - 1
            idx_frame = 6 if idx >= 7 else idx
            self.image = self.frames[idx_frame]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # label value
        self.label = label.Label(self.nquan, dist.FONTSIZE1, x + dist.SQUARE_WIDTH - 10,
                                     y + dist.SQUARE_HEIGHT - 10)

    def update(self):
        if self.nquan == 0:
            self.image = dist.imagedist['N']
        else:
            idx = self.nquan - 1
            idx_frame = 6 if idx >= 7 else idx
            self.image = self.frames[idx_frame]
        self.label.update(self.nquan)

    def draw(self, screen):
        self.label.draw(screen)
        screen.blit(self.image, self.rect)


def createChessqs():
    '''
     /|00|01|02|03|04|\
    11|--|--|--|--|--|05
     \|10|09|08|07|06|/
    :return: list<chessq>
    '''

    x = lambda i, j: 250 + i * dist.SQUARE_WIDTH - j * dist.SQUARE_WIDTH
    y = lambda i: 180 + i * dist.SQUARE_HEIGHT
    # 00->04
    chessqs1 = map(lambda i: Chessq(5, x(i, 0), y(0)), range(5))
    # 05
    chessqs2 = [Chessq(0, x(5, 0), y(0))]
    # 06-10
    chessqs3 = map(lambda i: Chessq(5, x(i, 1), y(1)), range(5, 0, -1))
    # 11
    chessqs4 = [Chessq(0, x(-1, 0), y(1))]
    return chessqs1 + chessqs2 + chessqs3 + chessqs4


def createChessQs():
    '''

    :return: list<chessQ>
    '''
    x = lambda i: 250 + i * dist.SQUARE_WIDTH
    y = lambda i: 180 + i * dist.SQUARE_HEIGHT
    return map(lambda i: ChessQ(x(6 * i - 1), y(i)), range(1,-1,-1))
