import pygame


class App:
    def __init__(self, res, fps):
        self.res = res
        self.fps = fps
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while True:
            self.update()
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            self.clock.tick(self.fps)
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')