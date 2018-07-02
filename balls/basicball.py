from balls.ball import Ball
import pygame
import random
from setting import Setting

set = Setting()

class BasicBall(Ball):
    '''
    基本小球，没有特殊属性，被吃后蛇长度以及分数增加1
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.radius = 10
        super(BasicBall, self).__init__(screen, self.radius, x, y)
        # 被吃后增加权重
        self.weight = 1
        self.R = random.randint(50, 150)
        self.G = random.randint(50, 150)
        self.B = random.randint(50, 150)
        

    def blitme(self, x, y):
        '''
        绘制自己，最基本的小球，圆形，随机颜色，填充
        '''
        self.pos[0] -= x
        self.pos[1] -= y
        pygame.draw.circle(self.screen, (self.R, self.G, self.B), \
        (self.pos[0], self.pos[1]), self.radius, 0)

    def byEaten(self):
        '''
        小球被吃后，效果的代表值
        Return:
               返回效果值
        '''
        return Ball.BASIC