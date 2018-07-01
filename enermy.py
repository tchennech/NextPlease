import pygame,random,math
from snake import Snake
from setting import Setting
set = Setting()
class OtherSnake(Snake):
    x = random.randint(22,640)
    y = random.randint(22,640)
    step = 1
    #headX = random.randint(20, 760)
    #headY = random.randint(20, 760)

    def __init__(self, screen):
        self.screen = screen
        super().__init__(screen)
        self.num = 20
        self.bodyX.append(200)
        self.bodyY.append(200)
        self.moveX = 2 * self.r * math.cos(math.radians(random.randint(-180, 180)))
        self.moveY = 2 * self.r * math.sin(math.radians(random.randint(-180, 180)))
        self.createBody()
        #color = [set.yellowCir, set.redCir, set.blueCir, set.greenCir]
        #self.color = color[random.randint(0,3)]


    def get_body(self):
        return self.bodyX, self.bodyY


    # 加速
    def accelerate(self):
        pass

    # 移动
    def moveaction(self, set):
        for i in range(0,self.num):
            self.bodyY[i] = self.bodyY[i] - set.ry
            self.bodyX[i] = self.bodyX[i] - set.rx
        for i in range(1, self.num):
            self.bodyX[self.num - i] = self.bodyX[self.num - i - 1]
            self.bodyY[self.num - i] = self.bodyY[self.num - i - 1]
        #random_x = 2 * self.r * math.cos(math.radians(random.randint(-180, 180)))
        #random_y = 2 * self.r * math.sin(math.radians(random.randint(-180, 180)))
        #print(set.directX,set.directY)

        #print('snake%d %d'%(self.bodyX[0],self.bodyY[0]))
        #print(set.backgroundPos[set.backgroundPages-1][0]+set.BGWIDTH, set.backgroundPos[set.backgroundPages - 1][1] + set.BGHEIGHT)

        if self.bodyX[0] + self.moveX < set.backgroundPos[0][0] and self.moveX < 0:
            self.moveX = - self.moveX
        if self.bodyX[0] + self.moveX > set.backgroundPos[set.backgroundPages - 1][0] + set.BGWIDTH and self.moveX >0:
            self.moveX = - self.moveX
        if self.bodyY[0] + self.moveY  < set.backgroundPos[0][1] and self.moveY < 0:
            self.moveY = -self.moveY
        if self.bodyY[0] + self.moveY> set.backgroundPos[set.backgroundPages - 1][1] + set.BGHEIGHT and self.moveY > 0:
            self.moveY = -self.moveY
        #if self.bodyX[0] + OtherSnake.moveX > 3*set.BGWIDTH or self.bodyX[0] + OtherSnake.moveX < 0:
        #    random_x =- random_x
            #OtherSnake.moveX *= -1
        #if self.bodyY[0] + OtherSnake.moveY > 3*set.BGHEIGHT or self.bodyY[0] + OtherSnake.moveY < 0:
        #    random_y =- random_y
        #if self.bodyX[0] < 0 or self.bodyX[0] > 200:

        #if self.bodyY[0] < 0 or self.bodyY[0] > 200:
            #OtherSnake.moveY *= -1
        #print(random_x, random_y)
        self.bodyX[0] = self.bodyX[0]  + int(self.moveX)
        self.bodyY[0] = self.bodyY[0]  + int(self.moveY)

    # 绘制
    def paint(self):
        for i in range(self.num):
            j = random.randint(0,3)
            self.screen.blit(self.color, (self.bodyX[i], self.bodyY[i]))
            #print(self.bodyX[i],self.bodyY[i])


