import pygame
from settings import *
from lines import *
from app import App

class RayCastApp(App):
    def update(self):
        keys()

    def draw(self):
        self.screen.fill(BG_COLOR)
        drawer(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    app = RayCastApp(
        SIZE,
        FPS
    )
    app.run()