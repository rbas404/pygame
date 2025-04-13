import pygame
import math
import random
import os
import sys
from globals import *
from scene import *
from player import Player
from texturedata import atlas_texture_data, solo_texture_data

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()           
        self.running = True

        self.scene = Scene(self)
        self.player = Player([self.scene.sprites])

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
    textures[name] = pygame.Surface.subsurface(atlas_image, pygame.Rect(data['position'][0], data['position'][1], data['size'], data['size']))
    game = game()
    game.run()



