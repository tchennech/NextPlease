import math,random, pygame
import abc
from setting import Setting
class Snake:
    def __init__(self,screen):
        self.screen = screen
        self.num = 8
        self.degree = 0
        self.bodyX = []
        self.bodyY = []
        self.r = 10
        self.power = 2
        self.invincibleTime = 40 # 无敌时间
        self.life = 1
        color = [Setting.yellowCir, Setting.redCir, Setting.blueCir, Setting.greenCir]
        temp = random.randint(0, 3)
        HeadColor = [Setting.yellowCirHead, Setting.redCirHead, Setting.blueCirHead, Setting.greenCirHead]
        self.color = color[temp]
        self.HeadColor = HeadColor[temp]

    def createBody(self):
        for i in range(1, self.num):
            self.bodyX.append(self.bodyX[i - 1] + int(2 * self.r * math.cos(random.randint(0, 45))))
            self.bodyY.append(self.bodyY[i - 1] + int(2 * self.r * math.sin(random.randint(0, 45))))
            #print(self.bodyX[i - 1], self.bodyY[i - 1])

    @abc.abstractmethod
    def moveaction(self,set):
        pass

    #获取蛇头位置
    def getSnakeHead(self):
        return self.bodyX[0],self.bodyY[0]


    @abc.abstractmethod
    def paint(self):
        pass

    @abc.abstractmethod
    def hitBorder(self,set):
        pass

    # 判断是否碰撞
    def isHit(self, x, y):
        distance = pow((self.bodyX[0] - x), 2) + pow((self.bodyY[0] - y), 2)
        if distance < pow(self.r, 2):
            return True
        return False

    # 碰撞后的反应
    def hitReact(self, thing):
        if thing == 'hitOtherSnake':
            self.dead()
        pass

    # 碰撞到其他蛇
    def hitOtherSnake(self, other):
        # 无敌时间削减
        if self.invincibleTime > 0 or other.invincibleTime > 0:
            return False

        for i in range(other.num):
            tempX = other.bodyX[i]
            tempY = other.bodyY[i]
            if self.isHit(tempX, tempY):
                self.life-=1
                self.dead()
                if self.life == 0:
                    return True
        return False

    # 无敌时间削减
    def decreInvincibleTime(self):
        if self.invincibleTime!=0:
            self.invincibleTime-=1

    # 无敌闪烁模式
    def wudi_paint(self):
        if self.invincibleTime > 0:
            color = [Setting.yellowCir, Setting.redCir, Setting.blueCir, Setting.greenCir]
            HeadColor = [Setting.yellowCirHead, Setting.redCirHead, Setting.blueCirHead, Setting.greenCirHead]
            for i in range(self.num):
                colortemp = random.randint(0, 3)
                self.color = color[colortemp]
                self.HeadColor = HeadColor[colortemp]
                if i == 0:
                    snakeheadrotate = pygame.transform.rotate(self.HeadColor, 360 - self.degree)
                    self.screen.blit(snakeheadrotate, (self.bodyX[i], self.bodyY[i]))
                else:
                    self.screen.blit(self.color, (self.bodyX[i], self.bodyY[i]))


    # 自身死亡后效果
    def dead(self):
        if self.life == 0:
            print('i was dead')


    def hasShield(self):
        self.invincibleTime += 20