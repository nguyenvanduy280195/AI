import pygame
import GUI_SpriteSheet as ss
import GUI_DISTIONARY as dist


class Maze():
    def __init__(self, wall, backdrop):
        self.wall = wall
        self.backgdrop = backdrop
        pass

    pass


class Goal(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        spritesheet = ss.SpriteSheet(dist.IMAGEDIST['goal'])

        # top
        frame = spritesheet.getImage(4, 0, 52, 66)
        self.frames.append(frame)
        # right
        frame = spritesheet.getImage(60, 0, 52, 66)
        self.frames.append(frame)
        # bottom
        frame = spritesheet.getImage(116, 0, 52, 35)
        self.frames.append(frame)
        # left
        frame = spritesheet.getImage(172, 0, 52, 66)
        self.frames.append(frame)

        self.x = col
        self.y = row

        self.image = self.frames[self.goalIdx()]

        self.rect = self.image.get_rect()

        if row == 0:
            self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE
            self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE - dist.TILE_SPACE - 6
        elif col == 0:
            self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE - dist.TILE_SPACE + 6
            self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE - 10
        else:
            self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE# - dist.TILE_SPACE
            self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE

        pass

    def goalIdx(self):
        if self.x == 0:
            return 3
        elif self.x == 12:
            return 1
        elif self.y == 0:
            return 0
        else:
            return 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Wall(pygame.sprite.Sprite):
    def __init__(self, idx, col, row):
        super(Wall, self).__init__()
        self.frames = []

        spritesheet = ss.SpriteSheet(dist.IMAGEDIST['wall'])

        # 0 left
        frame = spritesheet.getImage(0, 0, 12, 75)
        self.frames.append(frame)
        # 1 top
        frame = spritesheet.getImage(12, 0, 72, 18)
        self.frames.append(frame)
        # 2 right
        frame = spritesheet.getImage(84, 0, 96, 75)
        self.frames.append(frame)

        # show image
        self.image = self.frames[idx]
        self.rect = self.image.get_rect()

        # index of wall in board
        self.rect.x = col / 2 * dist.TILE_SPACE + dist.TILE_WIDTH_SIZE - 6
        self.rect.y = row / 2 * dist.TILE_SPACE + dist.TILE_HEIGHT_SIZE - 15

    pass

    def draw(self, screen): screen.blit(self.image, self.rect)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.sprite = dist.IMAGEDIST['background']
        pass

    def draw(self, screen): screen.blit(self.sprite, (0, 0))

    pass
