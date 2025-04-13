import pygame
from globals import *

class Scene:
    def __init__(self, app) -> None:
        self.app = app

    def update(self):
        pass

    def draw(self):
        self.app.screen.fill("red")