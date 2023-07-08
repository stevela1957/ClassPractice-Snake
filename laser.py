import pygame as pg
from settings import *


class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((4, 10))
        self.rect = self.image.get_rect(bottomleft=pos)
        self.image.fill(WHITE)

    def update(self):
        self.rect.y -= 7
        if self.rect.y <= -40:
            self.kill()