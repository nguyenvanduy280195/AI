import pygame
import time
import GUI_DISTIONARY as dist
import GUI_SpriteSheet
import Utilities as util


class Player(pygame.sprite.Sprite):
    def __init__(self, col, row):
        super(Player, self).__init__()

        self.move_x = 0
        self.move_y = 0

        self.direction = ''

        sprite_sheet = GUI_SpriteSheet.SpriteSheet(dist.IMAGEDIST['player'])

        self.walking_frame_up = util.getSpriteSheet(sprite_sheet, 0, 60, 60)
        self.walking_frame_right = util.getSpriteSheet(sprite_sheet, 60, 60, 60)
        self.walking_frame_down = util.getSpriteSheet(sprite_sheet, 120, 60, 60)
        self.walking_frame_left = util.getSpriteSheet(sprite_sheet, 180, 60, 60)

        self.image = self.walking_frame_down[0]

        self.rect = self.image.get_rect()

        self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE
        self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE
        pass

    #
    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        position = self.rect.x + self.rect.y

        if self.direction == 'l':
            frame = (position // 5) % len(self.walking_frame_left)
            self.image = self.walking_frame_left[frame]
        if self.direction == 'r':
            frame = (position // 5) % len(self.walking_frame_right)
            self.image = self.walking_frame_right[frame]
        if self.direction == 'u':
            frame = (position // 5) % len(self.walking_frame_up)
            self.image = self.walking_frame_up[frame]
        if self.direction == 'd':
            frame = (position // 5) % len(self.walking_frame_down)
            self.image = self.walking_frame_down[frame]

    def draw(self, screen): screen.blit(self.image, self.rect)

    # Player press down	-> call start()
    def start(self, direction):
        self.direction = direction
        if direction == 'l':
            self.move_x = -dist.STEP
        elif direction == 'r':
            self.move_x = dist.STEP
        elif direction == 'u':
            self.move_y = -dist.STEP
        elif direction == 'd':
            self.move_y = dist.STEP
        pass

    # Player press up	-> call stop()
    def stop(self):
        self.move_x = 0
        self.move_y = 0
        pass

