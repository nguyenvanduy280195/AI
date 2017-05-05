import pygame
import sys
import time
import Utilities as util

import GUI_Map as map
import GUI_DISTIONARY as dist

import Algorithm_BFS as bfs
import Algorithm_DFS as dfs
import Algorithm_DFS_Stack as stack

class MainGame:
    def __init__(self):
        self.level = 0
        self.levels = []
        self.screen = pygame.display.set_mode((dist.SCREEN_WIDTH, dist.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.algo_mode = 'Depth first search'
        self.count = 0
        self.directions_player = stack.Stack()
        self.directions_mummy = stack.Stack()
        self.game_running = True
        self.turnMovePlayer = 0
        #init pygame
        pygame.init()
        pygame.display.set_caption('Mummy Maze')
        # init level
        for i in range(0, 10, 1):
            self.levels.append(map.Map(dist.FILEDIST[i]))
            self.levels[i].makeMap()

    def run(self):
        player_count = 0
        mummy_count = 0
        while self.game_running:
            self.dt = self.clock.tick(dist.FPS)
            self.events()
            self.update()
            self.draw()
            #move

            if not self.directions_player.isEmpty() and self.turnMovePlayer == 0:
                step = self.directions_player.pop()
                self.levels[self.level].player.start(step)

                if player_count == 59:
                    player_count = 0
                    self.turnMovePlayer = 1
                else:
                    self.directions_player.push(step)
                    player_count += 1

            if not self.directions_mummy.isEmpty() and self.turnMovePlayer != 0:
                step = self.directions_mummy.pop()
                self.levels[self.level].mummy.start(step)

                if mummy_count == 59:
                    if self.turnMovePlayer == 2:
                        self.turnMovePlayer = 0
                    else:
                        self.turnMovePlayer = 2
                    mummy_count = 0
                else:
                    self.directions_mummy.push(step)
                    mummy_count += 1
                pass
            pygame.display.update()
        quit()

    def update(self):
        self.levels[self.level].player.update()
        self.levels[self.level].mummy.update()
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if self.levels[self.level].btnbfs.rect.collidepoint(pos):
                    self.algo_mode = 'Breadth first search'
                elif self.levels[self.level].btndfs.rect.collidepoint(pos):
                    self.algo_mode = 'Depth first search'
                elif self.levels[self.level].btnshc.rect.collidepoint(pos):
                    self.algo_mode = 'Simple Hill Climbing'
                elif self.levels[self.level].btnrun.rect.collidepoint(pos):

                    if self.algo_mode == 'Breadth first search':
                        b = bfs.BFS(self.levels[self.level].data)
                        start_time = time.time()
                        traversal_bfs, step = b.traversalStateTree()
                        self.levels[self.level].time = time.time() - start_time
                        self.levels[self.level].step = step
                        self.directions_player.push(None, util.findStep(traversal_bfs))
                        self.directions_mummy.push(None, util.findStep2(traversal_bfs))
                        pass

                    elif self.algo_mode == 'Depth first search':
                        d = dfs.DFS(self.levels[self.level].data)
                        start_time = time.time()
                        traversal_dfs, step = d.traversalStateTree()
                        self.levels[self.level].time = time.time() - start_time
                        self.levels[self.level].step = step
                        self.directions_player.push(None,util.findStep(traversal_dfs))
                        self.directions_mummy.push(None, util.findStep2(traversal_dfs))
                        pass
                    pass
                elif self.levels[self.level].btnprev.rect.collidepoint(pos):
                    if self.level > 0:
                        self.level -= 1
                elif self.levels[self.level].btnnext.rect.collidepoint(pos):
                    if self.level < 9:
                        self.level += 1
                elif self.levels[self.level].btnquit.rect.collidepoint(pos):
                    self.game_running = False

        pass

    def draw(self):
        # background
        self.levels[self.level].background.draw(self.screen)
        # goal
        self.levels[self.level].goal.draw(self.screen)
        # player
        self.levels[self.level].player.draw(self.screen)
        # mummy
        self.levels[self.level].mummy.draw(self.screen)
        # walls
        for level in self.levels[self.level].walls:
            level.draw(self.screen)

        # buttons
        self.levels[self.level].btnbfs.draw(self.screen)
        self.levels[self.level].btndfs.draw(self.screen)
        self.levels[self.level].btnshc.draw(self.screen)
        self.levels[self.level].btnrun.draw(self.screen)
        self.levels[self.level].btnquit.draw(self.screen)
        self.levels[self.level].btnprev.draw(self.screen)
        self.levels[self.level].btnnext.draw(self.screen)

        # Text: Level
        text = 'Level: ' + str(self.level)
        fontsize = 40
        color = (255, 255, 255)
        topleft = (10, 10)
        writeOnBackground(self.screen, text, fontsize, color, topleft)
        # Text: Step
        text = 'Step: ' + str(self.levels[self.level].step)
        fontsize = 20
        color = (255, 255, 255)
        topleft = (10, 50)
        writeOnBackground(self.screen, text, fontsize, color, topleft)

        # Text: Time
        text = 'Time: ' + str(self.levels[self.level].time)
        fontsize = 20
        color = (255, 255, 255)
        topleft = (10, 70)
        writeOnBackground(self.screen, text, fontsize, color, topleft)

        # Text: Algorithm
        text = self.algo_mode
        fontsize = 20
        color = (255, 255, 255)
        topleft = (10, 90)
        writeOnBackground(self.screen, text, fontsize, color, topleft)

        self.levels[self.level].player.stop()
        self.levels[self.level].mummy.stop()
        pass


def writeOnBackground(screen, text, fontsize, color, topleft):
    font = pygame.font.Font(None, fontsize, )
    t = font.render(text, True, color)
    rect = t.get_rect()
    rect.topleft = topleft
    screen.blit(t, rect)


def quit():
    pygame.quit()
    sys.exit()


main = MainGame()
main.run()
