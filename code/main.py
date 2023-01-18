import pygame
import sys
from debug import debug
from settings import *
from level import Level
from interface import Interface


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ground Game')

        self.game_screen = pygame.display.set_mode((WIDTH, HIGHT))

        self.running = True
        self.clock = pygame.time.Clock()

        self.interface = Interface()
        self.level = Level(self.interface)

    def run(self):
        while self.running:
            self.event_process()
            self.render()

            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()

    def event_process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.interface.click(pygame.mouse.get_pos())
                #self.interface.update()

    def render(self):
        self.game_screen.fill('black')
        self.interface.update()
        self.level.draw(pygame.mouse.get_pos())
        #debug('Test')


if __name__ == '__main__':
    app = Game()
    app.run()
    sys.exit()