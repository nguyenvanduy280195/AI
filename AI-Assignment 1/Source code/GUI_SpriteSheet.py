import pygame
import GUI_DISTIONARY as dist

class SpriteSheet(object):
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet
        pass

    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.spritesheet, (0,0), (x,y,width, height))
        image.set_colorkey(dist.COLORDIST['black'])
        return image