import pygame, random, math
from pygame.locals import *
from snake import Snake


class MySnake(Snake, set):
    step = 1

    # 延时时间
    delaytime = 0

    def __init__(self, screen, set):
        super().__init__(screen)
        self.set = set
        self.bodyX.append(set.originX)
        self.bodyY.append(set.originY)
        self.createBody()

    def get_body(self):
        return self.bodyX, self.bodyY

    # 加速功能，代填补
    def accelerate(self):
        self.delaytime += 10
        pass

    # 转向功能
    def turn(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.degree -= 10

            if event.key == K_RIGHT or event.key == K_d:
                self.degree += 10

            if event.key == K_SPACE:
                self.accelerate()

    # 移动
    def moveaction(self):
        rx = int(self.power * self.r * math.cos(math.radians(self.degree)))
        ry = int(self.power * self.r * math.sin(math.radians(self.degree)))
        for i in range(1, self.num):
            self.bodyX[self.num - i] = self.bodyX[self.num - i - 1] - rx
            self.bodyY[self.num - i] = self.bodyY[self.num - i - 1] - ry
        return rx, ry

    # 绘制
    def paint(self):
        # self.moveaction()
        pygame.time.delay(self.delaytime)
        for i in range(self.num):
            self.screen.blit(self.set.yellowCir, (self.bodyX[i], self.bodyY[i]))


