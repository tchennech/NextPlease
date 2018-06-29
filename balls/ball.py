import abc
import random

class Ball(object):
    '''
    这是游戏内被贪吃蛇吃的球的基类
    '''
    BASIC = 1
    DOUBLEWFUC = 2
    BUFFER = 3

    def __init__(self, screen, radius):
        '''
        初始化基类球 
        Args:
            screen: pygame.display.set_mode()对象，表示整个屏幕
        
        pos: 是一个包含两个int值的list 例如[1,2]，表示球在屏幕位置，随机生成
        radius: 是
        '''
        self.screen = screen
        self.radius = radius
        self.pos = [random.randint(-set.BGWIDTH + self.radius, 2 * set.BGWIDTH - self.radius),\
        random.randint(-set.BGHEIGHT + self.radius, 2 * set.BGHEIGHT - self.radius)]
    
    @abc.abstractmethod
    def blitme(self):
        '''
        在屏幕中绘制自己图像
        '''
        pass

    @abc.abstractmethod
    def byEat(self):
        '''
        被吃之后的效果
        '''
        pass

    def isEated(self, snake):
        '''
        判断小球是否被蛇吃掉
        '''
        # 蛇的位置
        sx = snake.bodyX[0]
        sy = snake.bodyY[0]
        # 蛇脑袋的半径
        sr = snake.r

        # 小球的位置
        bx = self.pos[0]
        by = self.pos[1]
        br = self.radius

        # 返回判断结果
        # 判断小球与蛇的脑袋是否相撞
        return (bx-sx)*(bx-sx) + (by-sy)*(by-sy) < (br+sr)*(br+sr)
