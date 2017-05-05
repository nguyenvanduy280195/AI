import sys
import pygame

import menu
import battle

import DISTIONARY as dist


# nguoi choi chon nhung~ lua chon dc show ra o 'menu'
# 'menu' se thiet lap nhung value
# goi 'chessboard'

class MainGame:
    def __init__(self):
        # init pygame
        pygame.init()
        pygame.display.set_caption('O An Quan')
        # sys
        self.screen = pygame.display.set_mode(dist.SCREEN_SIZE)
        self.screen.fill(dist.COLOR['white'])
        self.clock = pygame.time.Clock()
        self.gameRunning = True
        self.screenIsMenu = True
        # game
        self.menu = menu.Menu()
        self.battle = battle.Battle()

    def run(self):
        while self.gameRunning:
            self.clock.tick(dist.FPS)
            self.events()
            self.updates()
            self.draws()

            pygame.display.update()
        self.quitGame()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if self.screenIsMenu:
                    self.screenIsMenu, self.gameRunning = self.menu.events(pos)
                else:
                    self.screenIsMenu, self.gameRunning = self.battle.event(event)
                    pass

    def updates(self):
        if not self.screenIsMenu:
            self.battle.update()
            pass

    def draws(self):
        if self.screenIsMenu:
            self.menu.draw(self.screen)
        else:
            self.battle.draw(self.screen)


        pass

    def quitGame(self):
        pygame.quit()
        sys.exit()

main = MainGame()
main.run()

#TODO (priority 9) delete flag
#TODO (priority 8) step by step
#TODO (priority 7) edit chess q
#TODO (priority 7) edit button Menu