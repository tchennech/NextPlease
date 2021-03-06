import abc
import random
from setting import *

class Ball(object):
    '''
    这是游戏内被贪吃蛇吃的球的基类
    '''
    BASIC = 1
    DOUBLEWFUC = 2
    BUFFER = 3

    def __init__(self, screen, radius, x, y):
        '''
        初始化基类球 
        Args:
            screen: pygame.display.set_mode()对象，表示整个屏幕
        
        pos: 是一个包含两个int值的list 例如[1,2]，表示球在屏幕位置，随机生成
        radius: 是
        '''
        self.screen = screen
        self.radius = radius
        self.pos = [random.randint(x[0], x[1]),\
        random.randint(y[0], y[1])]
    
    @abc.abstractmethod
    def blitme(self):
        '''
        在屏幕中绘制自己图像
        '''


    @abc.abstractmethod
    def byEaten(self):
        '''
        被吃之后的效果
        '''
        pass

    def isEaten(self):
        '''
        判断小球是否被蛇吃掉
        '''
        iseaten = False
        if self.pos[0] > Setting.backgroundWidth//2-30 and self.pos[0] < Setting.backgroundWidth//2+30:
            if self.pos[1] > Setting.backgroundHeight//2-30 and self.pos[1] < Setting.backgroundHeight//2+30:
                iseaten = True

        # 返回判断结果
        # 判断小球与蛇的脑袋是否相撞
        return iseaten
