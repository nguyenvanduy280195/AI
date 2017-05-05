import pygame

import GUI_Player as player
import GUI_DISTIONARY as dist
import GUI_SpriteSheet
import Utilities as util


class Mummy(player.Player):
    def __init__(self, col, row):
        super(Mummy, self).__init__(col,row)

        self.change_x = 0
        self.change_y = 0

        self.direction = ''

        self.level = None

        sprite_sheet = GUI_SpriteSheet.SpriteSheet(dist.IMAGEDIST['mummy'])

        self.walking_frame_up = util.getSpriteSheet(sprite_sheet, 0, 60, 60)
        self.walking_frame_right = util.getSpriteSheet(sprite_sheet, 60, 60, 60)
        self.walking_frame_down = util.getSpriteSheet(sprite_sheet, 120, 60, 60)
        self.walking_frame_left = util.getSpriteSheet(sprite_sheet, 180, 60, 60)

        self.image = self.walking_frame_up[0]
        self.rect = self.image.get_rect()

        self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE
        self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE
