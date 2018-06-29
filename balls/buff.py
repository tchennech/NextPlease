import abc
import random
from setting import Setting

'''特殊物品类：盾，生命的父类'''

set = Setting()


class Buff(object):
    '''初始化'''
    def __init__(self, screen, image, radius):
        self.screen = screen
        self.x = random.randint(-480, 800)
        self.y = random.randint(-480, 800)
        self.image = image
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.screen = screen
        self.radius = radius
        self.pos = [random.randint(-set.BGWIDTH + self.radius, 2 * set.BGWIDTH - self.radius),\
        random.randint(-set.BGHEIGHT + self.radius, 2 * set.BGHEIGHT - self.radius)]

    '''
    @abc.abstractmethod
    def outofBounds(self):
        pass

    @abc.abstractmethod
    def step(self):
        pass
    '''

    '''画出'''
    def blitme(self, x, y):
        self.x -= x
        self.y -= y
        self.screen.blit(self.image, (self.x, self.y))

    '''判断碰撞'''
    @abc.abstractmethod
    def isEaten(self):
        '''
        判断小球是否被蛇吃掉
        '''
        # 蛇的位置
        iseaten = False
        if self.x > set.backgroundWidth//2-30 and self.x < set.backgroundWidth//2+30:
            if self.y > set.backgroundHeight//2-30 and self.y < set.backgroundHeight//2+30:
                iseaten = True

        # 返回判断结果
        # 判断小球与蛇的脑袋是否相撞
        return iseaten