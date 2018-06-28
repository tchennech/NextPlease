import pygame,random,math
from pygame.locals import  *
class Snake:
    num = 5
    r = 10
    degree = 0
    step = 1
    # 蛇身+头 横纵坐标
    headX = random.randint(20, 760)
    headY = random.randint(20, 760)
    bodyX = []
    bodyY = []
    bodyX.append(headX)
    bodyY.append(headY)


    def __init__(self,screen):
        self.screen =screen

        for i in range(1,self.num ):
            self.bodyX.append(self.bodyX[i-1] + int(2 * self.r * math.cos(random.randint(0, 45))))
            self.bodyY.append(self.bodyY[i-1] + int(2 * self.r * math.sin(random.randint(0, 45))))
            print(self.bodyX[i-1], self.bodyY[i-1])

    def get_body(self):
        return self.bodyX,self.bodyY

    # 加速功能，代填补
    def accelerate(self):
        pass

    # 转向功能
    def turn(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.degree -= 15

            if event.key == K_RIGHT or event.key == K_d:
                self.degree += 15

            if event.key == K_SPACE:
                self.accelerate()

    # 获取蛇头坐标
    def getSnakeHead(self):
        return self.bodyX[0], self.bodyY[0]

    # 移动
    def moveaction(self):
        for i in range(1,self.num):
            self.bodyX[self.num-i]=self.bodyX[self.num-i-1]
            self.bodyY[self.num-i]=self.bodyY[self.num-i-1]
        self.bodyX[0] = int(self.bodyX[0] + 2 * self.r*math.cos(math.radians(self.degree)))
        self.bodyY[0] = int(self.bodyY[0] + 2 * self.r * math.sin(math.radians(self.degree)))

    # 绘制
    def paint_Hero(self):
        self.moveaction()
        for i in range(self.num):
            pygame.draw.circle(self.screen, (255, 255, 0), (self.bodyX[i], self.bodyY[i]), 5, 0)



    