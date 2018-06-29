import pygame,random,math
from setting import Setting

set = Setting()
class OtherSnake:
    x = random.randint(22,640)
    y = random.randint(22,640)
    num = 20
    r = 10
    degree = 0
    step = 1
    headX = random.randint(20, 760)
    headY = random.randint(20, 760)
    bodyX = []
    bodyY = []
    bodyX.append(headX)
    bodyY.append(headY)

    def __init__(self, screen):
        self.screen = screen

        for i in range(1, self.num):
            self.bodyX.append(self.bodyX[i - 1] + int(2 * self.r * math.cos(random.randint(0, 45))))
            self.bodyY.append(self.bodyY[i - 1] + int(2 * self.r * math.sin(random.randint(0, 45))))
            print(self.bodyX[i - 1], self.bodyY[i - 1])


    def get_body(self):
        return self.bodyX, self.bodyY


    # 加速
    def accelerate(self):
        pass


    # 移动
    def moveaction(self):
        for i in range(1, self.num):
            self.bodyX[self.num - i] = self.bodyX[self.num - i - 1]
            self.bodyY[self.num - i] = self.bodyY[self.num - i - 1]
        random_x = 2 * self.r * math.cos(math.radians(random.randint(-180, 180)))
        random_y = 2 * self.r * math.sin(math.radians(random.randint(-180, 180)))
        #if self.bodyX[0] + random_x > 3*set.BGWIDTH or self.bodyX[0] + random_x < 0:
        #    random_x =- random_x
        #elif self.bodyY[0] + random_y > 3*set.BGHEIGHT or self.bodyY[0] + random_y < 0:
        #    random_y =- random_y
        if self.bodyX[0] < set.backgroundPos[0][0] or self.bodyX[0] > set.backgroundPos[set.backgroundPages-1][0] + set.BGWIDTH:
            random_x *= -1
        if self.bodyY[0] < set.backgroundPos[0][1] or self.bodyY[0] > set.backgroundPos[set.backgroundPages-1][1] + set.BGHEIGHT:
            random_y *= -1

        self.bodyX[0]+=int(random_x)
        self.bodyY[0]+=int(random_y)

    # 绘制
    def paint(self):
        for i in range(self.num):
            pygame.draw.circle(self.screen, (255, 0, 0), (self.bodyX[i], self.bodyY[i]), 5, 0)