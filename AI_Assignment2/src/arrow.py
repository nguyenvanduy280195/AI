import DISTIONARY as dist

class Arrow:
    def __init__(self, x, y, is_left):
        self.__image__= dist.imagedist['arrow_left'] if is_left else dist.imagedist['arrow_right']
        self.__rect__ = self.__image__.get_rect()
        self.__rect__.x = x
        self.__rect__.y = y

    def draw(self, screen): screen.blit(self.__image__, self.__rect__)

    @property
    def rect(self): return self.__rect__

    @rect.setter
    def rect(self, value): self.__rect__ = value


