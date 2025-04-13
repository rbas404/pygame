import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), position = (SCREENWIDTH   // 2, SCREENHEIGHT // 2)):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = 3

    def input(self):  # Correcte inspringing
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self):
        self.input()