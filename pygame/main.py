import pygame
import math
import random
import os
import sys
from globals import *
from scene import *


class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()           
        self.running = True

        self.scene = Scene(self)

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.scene.update()
        
        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.scene.draw()
        
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = game()
    game.run()



