import pygame
import GUI_Button as button
import GUI_Maze as maze
import GUI_Player as player
import GUI_Mummy as mummy
import GUI_DISTIONARY as dist


class Map:
    def __init__(self, filename):
        tileSize = 16
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width = self.tileWidth * tileSize
        self.height = self.tileHeight * tileSize
        self.lv = int(filename[9])
        self.step = 0
        self.time = 0

        self.player = None
        self.mummy =  None
        self.walls = pygame.sprite.Group()
        self.goal = None
        self.background = None

    def makeMap(self):
        self.background = maze.Background()

        for row, tiles in enumerate(self.data):
            for col, tile in enumerate(tiles):
                if tile == 'x' and row != 0 and col != 0 and row != 12 and col != 12:
                    if row % 2 == 0 and col % 2 != 0:
                        self.walls.add(maze.Wall(1, col, row))
                    if row % 2 != 0 and col % 2 == 0:
                        self.walls.add(maze.Wall(0, col, row))
                if tile == 'm':
                    self.mummy = mummy.Mummy(col, row)
                if tile == 'p':
                    self.player = player.Player(col, row)
                if tile == 'g':
                    self.goal = maze.Goal(col, row)

        self.btnbfs = button.Button(dist.IMAGEDIST['btnBFS'], (10, 132))
        self.btndfs = button.Button(dist.IMAGEDIST['btnDFS'], (11, 176))
        self.btnshc = button.Button(dist.IMAGEDIST['btnSHC'], (9, 225))
        self.btnrun = button.Button(dist.IMAGEDIST['btnRun'], (11, 270))
        self.btnprev = button.Button(dist.IMAGEDIST['btnPrev'], (10, 315))
        self.btnnext = button.Button(dist.IMAGEDIST['btnNext'], (80, 315))


        self.btnquit = button.Button(dist.IMAGEDIST['btnQuit'], (10, 430))


        pass
