import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, top_left):
        super(Button, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left

    def draw(self, screen): screen.blit(self.image, self.rect)