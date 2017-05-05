import DISTIONARY as dist
import pygame

class Label():
    def __init__(self, text, fontsize, x, y):
        #super(Label, self).__init__()
        self.__font__ = pygame.font.Font(None, fontsize)
        self.__image__ = self.__font__.render(str(text), True, dist.COLOR['black'])
        self.__rect__ = self.__image__.get_rect()
        self.__rect__.x = x
        self.__rect__.y = y

    def draw(self, screen): screen.blit(self.__image__, self.__rect__)

    def update(self, value): self.__image__ = self.__font__.render(str(value), True, dist.COLOR['black'])
