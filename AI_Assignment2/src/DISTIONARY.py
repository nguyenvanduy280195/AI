import pygame

# GUI
imagedist = {
    '1q': pygame.image.load('res/images/1q.png'),
    '2q': pygame.image.load('res/images/2q.png'),
    '3q': pygame.image.load('res/images/3q.png'),
    '4q': pygame.image.load('res/images/4q.png'),
    '5q': pygame.image.load('res/images/5q.png'),
    '6q': pygame.image.load('res/images/6q.png'),
    '7q': pygame.image.load('res/images/nq.png'),
    'Q': pygame.image.load('res/images/Q.png'),
    'N': pygame.image.load('res/images/N.png'),
    'flag': pygame.image.load('res/images/flag.png'),
    'screen_game': pygame.image.load('res/images/screen_game.png'),
    'screen_menu': pygame.image.load('res/images/screen_menu.png'),
    'btnBatDau': pygame.image.load('res/images/btnBatDau.png'),
    'btnCapMinimax1': pygame.image.load('res/images/btnCapMinimax1.png'),
    'btnCapMinimax2': pygame.image.load('res/images/btnCapMinimax2.png'),
    'btnCapMinimax3': pygame.image.load('res/images/btnCapMinimax3.png'),
    'btnHuongDan': pygame.image.load('res/images/btnHuongDan.png'),
    'btnMenu': pygame.image.load('res/images/btnMenu.png'),
    'btnThoat': pygame.image.load('res/images/btnThoat.png'),
    'arrow_left': pygame.image.load('res/images/arrow_left.png'),
    'arrow_right': pygame.image.load('res/images/arrow_right.png'),
}

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BTN_WIDTH = 130
BTN_HEIGHT = 30
BTN_SIZE = (BTN_WIDTH, BTN_HEIGHT)
BTN_GAP_SPACE = 20

SQUARE_WIDTH = 60
SQUARE_HEIGHT = 60
SQUARE_SIZE = (SQUARE_WIDTH, SQUARE_HEIGHT)

COLOR = {
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

FONTSIZE = 40
FONTSIZE1 = 20

FPS = 60

# ALGORITHM
TREE_LEVEL = 5

BOARD_NONE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BOARD_DEFAULT_0 = [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0]  # ai_turn 0 <-
BOARD_DEFAULT_1 = [0, 6, 6, 6, 6, 1, 0, 6, 6, 6, 6, 0]  # player_ 2 <-
BOARD_DEFAULT_2 = [2, 1, 8, 0, 0, 0, 0, 9, 0, 8, 8, 2]  # ai_turn 0 <-
BOARD_DEFAULT_3 = [0, 2, 9, 1, 1, 1, 1, 10, 1, 0, 9, 0]  # player_ 0 <-
BOARD_DEFAULT_4 = [1, 0, 0, 0, 0, 3, 1, 11, 2, 1, 10, 1]  # ai_turn 0 ->
BOARD_DEFAULT_5 = [0, 2, 9, 1, 1, 1, 1, 10, 1, 0, 9, 0]  # player_ 0 <-
BOARD_DEFAULT_6 = [1, 2, 1, 1, 1, 1, 2, 0, 0, 2, 11, 2]
BOARD_DEFAULT_7 = [0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 12, 3]
BOARD_DEFAULT = [BOARD_DEFAULT_0, BOARD_DEFAULT_1, BOARD_DEFAULT_2,
                 BOARD_DEFAULT_3, BOARD_DEFAULT_4, BOARD_DEFAULT_5,
                 BOARD_DEFAULT_6, BOARD_DEFAULT_7]
BOARD_SIZE = 12

# test
PLAYER_SCORE_0 = 0
PLAYER_SCORE_1 = 0
PLAYER_SCORE_2 = 21
PLAYER_SCORE_3 = 21
PLAYER_SCORE_4 = 26
PLAYER_SCORE_5 = 26
PLAYER_SCORE_6 = 29
PLAYER_SCORE_7 = 29
PLAYER_SCORE = [PLAYER_SCORE_0, PLAYER_SCORE_1, PLAYER_SCORE_2,
                PLAYER_SCORE_3, PLAYER_SCORE_4, PLAYER_SCORE_5,
                PLAYER_SCORE_6, PLAYER_SCORE_7]

AI_SCORE_0 = 0
AI_SCORE_1 = 11
AI_SCORE_2 = 11
AI_SCORE_3 = 14
AI_SCORE_4 = 14
AI_SCORE_5 = 17
AI_SCORE_6 = 17
AI_SCORE_7 = 22
AI_SCORE = [AI_SCORE_0, AI_SCORE_1, AI_SCORE_2, AI_SCORE_3, AI_SCORE_4, AI_SCORE_5, AI_SCORE_6, AI_SCORE_7]

HAS_QUAN_1_0 = True
HAS_QUAN_1_1 = True
HAS_QUAN_1_2 = False
HAS_QUAN_1_3 = False
HAS_QUAN_1_4 = False
HAS_QUAN_1_5 = False
HAS_QUAN_1_6 = False
HAS_QUAN_1_7 = False
HAS_QUAN_1 = [HAS_QUAN_1_0, HAS_QUAN_1_1, HAS_QUAN_1_2, HAS_QUAN_1_3, HAS_QUAN_1_4, HAS_QUAN_1_5, HAS_QUAN_1_6,
              HAS_QUAN_1_7]

HAS_QUAN_2_0 = True
HAS_QUAN_2_1 = False
HAS_QUAN_2_2 = False
HAS_QUAN_2_3 = False
HAS_QUAN_2_4 = False
HAS_QUAN_2_5 = False
HAS_QUAN_2_6 = False
HAS_QUAN_2_7 = False
HAS_QUAN_2 = [HAS_QUAN_2_0, HAS_QUAN_2_1, HAS_QUAN_2_2, HAS_QUAN_2_3, HAS_QUAN_2_4, HAS_QUAN_2_5, HAS_QUAN_2_6,
              HAS_QUAN_2_7]

QUAN_1_INDEX = 5
QUAN_2_INDEX = 11
QUAN_SCORE = 10

DAN_SCORE = 1

NaN = float('nan')
INF = float('inf')
