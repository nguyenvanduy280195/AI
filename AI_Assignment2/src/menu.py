import pygame

import DISTIONARY as dist
import button


class Menu():
    def __init__(self):
        # super(Menu, self).__init__()
        self.batDau = False
        self.x = 0
        self.y = 0
        self.image = dist.imagedist['screen_menu']
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        x = dist.SCREEN_WIDTH / 2 - dist.BTN_WIDTH / 2
        y = dist.SCREEN_HEIGHT / 2
        delta = dist.BTN_HEIGHT + dist.BTN_GAP_SPACE

        self.btnBatDau = button.Button(dist.imagedist['btnBatDau'], x, y)
        # de cuoi cung` se lam
        self.btnHuongDan = button.Button(dist.imagedist['btnHuongDan'], x, y + delta)
        self.btnThoat = button.Button(dist.imagedist['btnThoat'], x, y + 2 * delta)

        self.btnCapDo = map(
            lambda i: button.Button(dist.imagedist['btnCapMinimax%s' % (i)], x, y + (i - 1) * delta), range(1, 4, 1))

    def events(self, pos):
        '''

        :param pos:
        :return: screenIsMenu, gameRunning
            True, True
            False, True
            False, False
        '''
        if not self.batDau:
            if self.btnBatDau.rect.collidepoint(pos):
                # clear 3 button: batdau, huong dan, thoat
                # show 3 button: cap 1 2 3
                self.batDau = True
            if self.btnHuongDan.rect.collidepoint(pos):
                return False, False
            if self.btnThoat.rect.collidepoint(pos):
                return False, False

        else:
            for i in self.btnCapDo:
                if i.rect.collidepoint(pos):
                    # TODO param of algorithm
                    print 'click'
                    return False, True
        return True, True

    def draw(self, screen):
        if not self.batDau:
            self.btnBatDau.draw(screen)
            self.btnHuongDan.draw(screen)
            self.btnThoat.draw(screen)
        else:
            for i in self.btnCapDo: i.draw(screen)
        screen.blit(self.image, self.rect)
