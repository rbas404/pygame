import pygame
from globals import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = image 
        self.rect = self.image.get_rect(topleft = position)
    #def update(self):