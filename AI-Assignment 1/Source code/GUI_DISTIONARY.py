import pygame

FILEDIST = {0: 'res/maps/0.txt',
            1: 'res/maps/1.txt',
            2: 'res/maps/2.txt',
            3: 'res/maps/3.txt',
            4: 'res/maps/4.txt',
            5: 'res/maps/5.txt',
            6: 'res/maps/6.txt',
            7: 'res/maps/7.txt',
            8: 'res/maps/8.txt',
            9: 'res/maps/9.txt'}

IMAGEDIST = {
    'arrow': pygame.image.load('res/images/arrows6.gif'),
    'background': pygame.image.load('res/images/background.jpg'),
    'goal': pygame.image.load('res/images/stairs6.gif'),
    'mummy': pygame.image.load('res/images/mummy6.gif'),
    'player': pygame.image.load('res/images/explorer6.gif'),
    'wall': pygame.image.load('res/images/walls6.gif'),
    'btnBFS': pygame.image.load('res/images/btnBFS.png'),
    'btnDFS': pygame.image.load('res/images/btnDFS.png'),
    'btnSHC': pygame.image.load('res/images/btnSHC.png'),
    'btnRun': pygame.image.load('res/images/btnRun.png'),
    'btnQuit': pygame.image.load('res/images/btnQuit.png'),
    'btnPrev': pygame.image.load('res/images/btnPrev.png'),
    'btnNext': pygame.image.load('res/images/btnNext.png')}


COLORDIST = {'black': (0, 0, 0)}

STEP = 1
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 360
BOARD_HEIGHT = 360

TILE_WIDTH_SIZE = 216
TILE_HEIGHT_SIZE = 80
TILE_SPACE = 60

FPS = 240