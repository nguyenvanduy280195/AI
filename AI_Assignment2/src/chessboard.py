import DISTIONARY as dist

import button
import label


class Chessboard:
    def __init__(self):
        # background
        self.background = dist.imagedist['screen_game']
        self.rect = self.background.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # score
        self.scorePlayer = 0
        self.scoreAI = 0

        x = 15
        y = 0.5 * dist.SCREEN_HEIGHT
        delta = dist.BTN_HEIGHT + dist.BTN_GAP_SPACE
        # button
        self.btnMenu = button.Button(dist.imagedist['btnMenu'], x, y)
        self.btnHuongDan = button.Button(dist.imagedist['btnHuongDan'], x, y + delta)
        self.btnThoat = button.Button(dist.imagedist['btnThoat'], x, y + 2 * delta)
        # label
        self.lblPlayer = label.Label('PLAYER', dist.FONTSIZE, 200, 330)
        self.lblScorePlayer = label.Label('SCORE', dist.FONTSIZE, 450, 400)
        self.lblValueScorePlayer = label.Label(str(self.scorePlayer), dist.FONTSIZE, 560, 400)

        self.lblAI = label.Label('COMPUTER', dist.FONTSIZE, 200, 120)
        self.lblScoreAI = label.Label('SCORE', dist.FONTSIZE, 450, 50)
        self.lblValueScoreAI = label.Label(str(self.scorePlayer), dist.FONTSIZE, 560, 50)



    def update(self):
        self.lblValueScorePlayer.update(self.scorePlayer)
        self.lblValueScoreAI.update(self.scoreAI)

    def draw(self, screen):
        # draw a background
        screen.blit(self.background, self.rect)
        # draw buttons
        self.btnMenu.draw(screen)
        self.btnHuongDan.draw(screen)
        self.btnThoat.draw(screen)
        # draw label
        self.lblPlayer.draw(screen)
        self.lblScorePlayer.draw(screen)
        self.lblValueScorePlayer.draw(screen)
        self.lblAI.draw(screen)
        self.lblScoreAI.draw(screen)
        self.lblValueScoreAI.draw(screen)

    def event(self, e):
        if self.btnMenu.rect.collidepoint(e.pos):
            return True, True
        if self.btnHuongDan.rect.collidepoint(e.pos):
            return False, False
        if self.btnThoat.rect.collidepoint(e.pos):
            return False, False
        return False, True
