import pygame as pg
import sys
from settings import *
import random

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.font.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Slither")
        self.font = pg.font.Font(None, 30)

        self.headX = WIDTH // 2
        self.headY = HEIGHT // 2
        self.snakeMotionX = 0
        self.snakeMotionY = 0
        self.snakeVel = 3
        self.blockSize = 10
        self.appleImg = pg.transform.scale(pg.image.load('graphics/apple.png').convert_alpha(),
                                          (self.blockSize, self.blockSize))
        self.appleRect = self.appleImg.get_rect()
        self.appleRect.x = random.randrange(0, WIDTH - self.blockSize)
        self.appleRect.y = random.randrange(0, HEIGHT - self.blockSize)
        self.score = 0
        self.hiScore = 0
        self.snakeList = []
        self.snakeList.append([self.headX, self.headY])
        self.snakeLength = 15

        self.running = True

    def snake(self, snkLst, blkSz):
        for XnY in snkLst:
            pg.draw.rect(self.screen, GREEN, (XnY[0], XnY[1], self.blockSize, self.blockSize))

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                    running = False
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.snakeMotionX = -self.snakeVel
                        self.snakeMotionY = 0
                    if event.key == pg.K_RIGHT:
                        self.snakeMotionX = self.snakeVel
                        self.snakeMotionY = 0
                    if event.key == pg.K_UP:
                        self.snakeMotionX = 0
                        self.snakeMotionY = -self.snakeVel
                    if event.key == pg.K_DOWN:
                        self.snakeMotionX = 0
                        self.snakeMotionY = self.snakeVel
            self.headX += self.snakeMotionX
            self.headY += self.snakeMotionY
            self.screen.fill(GRAY)
            self.snake(self.snakeList, self.blockSize)
            pg.draw.rect(self.screen, GREEN, (self.headX, self.headY, self.blockSize, self.blockSize))
            self.screen.blit(self.appleImg,self.appleRect)
            if (self.headX + self.blockSize >= self.appleRect.x and self.headX <= self.appleRect.x + self.blockSize):
                if (self.headY + self.blockSize >= self.appleRect.y and self.headY <= self.appleRect.y + self.blockSize):
                    self.snakeList.append([self.headX, self.headY])
                    if len(self.snakeList) > self.snakeLength:
                        del self.snakeList[0]
                    self.appleRect.x = random.randrange(0, WIDTH - self.blockSize)
                    self.appleRect.y = random.randrange(0, HEIGHT - self.blockSize)
                    self.score += 1
            self.scoreboard = self.font.render(f"Score:{self.score}", False, AQUA)
            self.screen.blit(self.scoreboard, (10, 20))
            pg.display.update()
            self.clock.tick(FPS)

            if self.headX <=0 or self.headX >= WIDTH - self.blockSize or self.headY <=0 or self.headY >= HEIGHT - self.blockSize:
                self.running = False

if __name__ == '__main__':
    game = Game()
    game.run()
    pg.quit()
