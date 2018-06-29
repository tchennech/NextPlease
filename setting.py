import pygame


class Setting:
    def __init__(self):
        self.background = []
        self.backgroundPages = 9
        # 窗口大小
        self.BGWIDTH = 500
        self.BGHEIGHT = 500
        # 蛇头原始坐标
        self.originX = 200
        self.originY = 200
        self.rx = 0
        self.ry = 0
        self.backgroundPos = [[-self.BGWIDTH, -self.BGHEIGHT], [-self.BGWIDTH, 0], [-self.BGWIDTH, self.BGHEIGHT],
                              [0, -self.BGHEIGHT], [0, 0], [0, self.BGHEIGHT],
                              [self.BGWIDTH, -self.BGHEIGHT], [self.BGWIDTH, 0], [self.BGWIDTH, self.BGHEIGHT]]

        self.borderPos = [
            [-self.BGWIDTH * 2, -self.BGHEIGHT * 2], [-self.BGWIDTH * 2, -self.BGWIDTH], [-self.BGWIDTH * 2, 0],
            [-self.BGWIDTH * 2, self.BGHEIGHT], [-self.BGWIDTH * 2, self.BGHEIGHT * 2],
            [-self.BGWIDTH, -self.BGWIDTH*2], [-self.BGWIDTH, self.BGWIDTH*2],
            [0, -self.BGWIDTH * 2], [0, self.BGWIDTH * 2],
            [self.BGWIDTH, -self.BGWIDTH*2], [self.BGWIDTH, self.BGWIDTH*2],
            [self.BGWIDTH * 2, -self.BGHEIGHT * 2], [self.BGWIDTH * 2, -self.BGWIDTH], [self.BGWIDTH * 2, 0],
            [self.BGWIDTH * 2, self.BGHEIGHT], [self.BGWIDTH * 2, self.BGHEIGHT * 2]]

        for i in range(1, self.backgroundPages + 1):
            self.background.append('img/grids' + str(i) + '.jpg')

        #封面
        self.cover = pygame.image.load("img/cover.jpg")
        self.backgroundWidth = self.cover.get_rect()[2]
        self.backgroundHeight = self.cover.get_rect()[3]
        self.pressImg = pygame.image.load('img/press.png')
        self.leftImg = pygame.image.load('img/yellow.png')
        self.rightImg = pygame.image.load('img/red.png')
        self.imgWidth = self.pressImg.get_rect()[2]
        #游戏结束
        self.gameover = pygame.image.load('img/gameover.jpg')

        self.redCir = pygame.image.load("img/circle00.png")

        self.shieldImg = "img/shield.png"

        self.yellowCir = pygame.image.load("img/circle02.png")


clock = pygame.time.Clock()
