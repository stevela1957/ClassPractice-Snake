import pygame as pg
from settings import *


class Alien(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.green = pg.image.load('graphics/green.png').convert_alpha()
        self.yellow = pg.image.load('graphics/yellow.png').convert_alpha()
        self.red = pg.image.load('graphics/red.png').convert_alpha()
        self.image = self.red
        self.rect = self.image.get_rect(bottomleft=pos)

    def update(self):
        pass