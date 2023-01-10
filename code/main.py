import pygame
import sys
from debug import debug
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ground Game')

        self.game_screen = pygame.display.set_mode((WIDTH, HIGHT))

        self.running = True
        self.clock = pygame.time.Clock()

        self.level = Level()

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

    def render(self):
        self.game_screen.fill('black')
        self.level.draw(pygame.mouse.get_pos())
        #debug('Test')


if __name__ == '__main__':
    app = Game()
    app.run()
    sys.exit()