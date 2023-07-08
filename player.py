import pygame as pg
from pygame.locals import *
from settings import *
from laser import Laser

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=pos)
        self.velocity = 3
        self.laser = pg.sprite.Group()
        self.laserSnd = pg.mixer.Sound('audio/laser.wav')
        self.laserIdle = True
        self.timer = 0

    def move(self):
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.left -= self.velocity
            if self.rect.left <= 0:
                self.rect.left = 0
        if keys[K_RIGHT]:
            self.rect.right += self.velocity
            if self.rect.right >= WIDTH:
                self.rect.right = WIDTH
        if keys[K_SPACE]:
            if self.laserIdle:
                self.laserIdle = False
                self.laser.add(Laser((self.rect.centerx, self.rect.top)))
                self.laserSnd.play()
                self.timer = pg.time.get_ticks()

    def laserCooldown(self):
        if pg.time.get_ticks() - self.timer >= 500:
            self.laserIdle = True

    def update(self):
        self.move()
        self.laserCooldown()
        self.laser.update()