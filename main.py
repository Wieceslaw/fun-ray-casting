import pygame
from settings import *
from lines import *

class App:
    def __init__(self, res, fps) -> None:
        self.res = res
        self.fps = fps
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()

    def update(self):
        keys()

    def draw(self): 
        self.screen.fill(BLACK)
        drawer(self.screen)
        pygame.display.flip()


    def run(self):
        while True:
            self.update()
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            self.clock.tick(self.fps)
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')



if __name__ == '__main__':
    app = App(
        SIZE,
        FPS
    )
    app.run()