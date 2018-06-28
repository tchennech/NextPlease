from ball import Ball
import pygame
import random

class BasicBall(Ball):
    '''
    基本小球，没有特殊属性，被吃后蛇长度以及分数增加1
    '''
    def __init__(self, screen, radius):
        self.screen = screen
        self.pos = [random.randint(0, 600), random.randint(0, 800)]
        self.radius = radius 
        super(basicball, self).__init__(screen, self.radius)
        # 被吃后增加权重
        self.weight = 1
        

    def blitme(self):
        '''
        绘制自己，最基本的小球，圆形，随机颜色，填充
        '''
        R = random.randint(50, 150)
        G = random.randint(50, 150)
        B = random.randint(50, 150)
        pygame.draw.circle(self.screen, (R, G, B), \
        (self.pos[0], self.pos[1]), self.radius, 0)

    def byEat(self):
        '''
        小球被吃后，蛇身体增加值以及分数增加值
        Return:
               返回分数以及小球身体增加的值
        '''
        return self.weight
