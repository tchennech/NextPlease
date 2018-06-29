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
    def isHit(self,set):
        pass
