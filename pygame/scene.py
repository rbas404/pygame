import pygame
from globals import *
from sprite import Entity
from player import Player
from texturedata import atlas_texture_data, solo_texture_data

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.gen_solo_textures = self.gen_solo_textures()
        self.atlas_textures = self.gen_atlas_textures('assets/images/tiles/DemoSprite.png')

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites], image=self.atlas_textures['grass_1'], position=(0, 0))
        Entity([self.sprites], position=(100, 100), image=self.gen_solo_textures['player_static'])

        self.player = Player([self.sprites])

        self.gen_world()

    def gen_solo_textures(self): 
        textures = {}

        for name, data in solo_texture_data.items():
            textures[name] = pygame.transform.scale(pygame.image.load(data['file_path']).convert_alpha(), data['size'])

        return textures

    def gen_atlas_textures(self, filepath):
        textures = {}
        try:
            # Zorg ervoor dat het bestandspad correct is
            atlas_image = pygame.image.load(filepath).convert_alpha()
        except FileNotFoundError:
            raise FileNotFoundError(f"Het bestand '{filepath}' bestaat niet. Controleer het pad.")

        # Itereer door atlas_texture_data en maak subsurfaces
        for name, data in atlas_texture_data.items():
            textures[name] = pygame.Surface.subsurface(
                atlas_image,
                pygame.Rect(data['position'][0], data['position'][1], data['size'], data['size'])
            )
        return textures

    def gen_world(self):  
        pass

    def update(self):
        self.sprites.update()
    def draw(self):
        self.app.screen.fill("red")
        self.sprites.draw(self.app.screen)