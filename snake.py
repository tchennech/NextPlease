import math,random
import abc
class Snake:
    def __init__(self,screen):
        self.screen = screen
        self.num = 8
        self.degree = 0
        self.bodyX = []
        self.bodyY = []
        self.r = 10
        self.power = 2
        self.invincibleTime = 20 # 无敌时间
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
                self.dead()
                return True
        return False

    # 无敌时间削减
    def decreInvincibleTime(self):
        if self.invincibleTime!=0:
            self.invincibleTime-=1

    # 自身死亡后效果
    def dead(self):
        print('i was dead')
