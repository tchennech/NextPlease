import pygame


class Setting:
    backgroundStore = []
    borderImg = pygame.image.load('img/border.jpg')
    # 封面
    cover = pygame.image.load("img/cover.jpg")
    backgroundWidth = cover.get_rect()[2]
    backgroundHeight = cover.get_rect()[3]
    pressImg = pygame.image.load('img/press.png')
    leftImg = pygame.image.load('img/yellow.png')
    rightImg = pygame.image.load('img/red.png')
    imgWidth = pressImg.get_rect()[2]
    # 游戏结束
    gameover = pygame.image.load('img/gameover.jpg')

    redCir = pygame.image.load("img/circle00.png")
    blueCir = pygame.image.load("img/circle01.png")
    yellowCir = pygame.image.load("img/circle02.png")
    greenCir = pygame.image.load("img/circle03.png")
    shieldImg = "img/shield.png"
    heartImg = "img/heart.png"

    # 蛇的脑袋
    redCirHead = pygame.image.load("img/head00.png")
    blueCirHead = pygame.image.load("img/head01.png")
    yellowCirHead = pygame.image.load("img/head02.png")
    greenCirHead = pygame.image.load("img/head03.png")

    # 分数栏
    titleImage = pygame.image.load('img/title.png')

    # 参数重置
    def setInit(self):
        self.__init__()

    def __init__(self):
        self.backgroundPages = 9
        # 窗口大小
        #self.BGWIDTH = self.cover.get_rect()[2]
        #self.BGHEIGHT = self.cover.get_rect()[3]
        self.BGWIDTH = self.cover.get_rect()[2]
        self.BGHEIGHT= self.cover.get_rect()[3]
        # 蛇头原始坐标
        self.originX = self.cover.get_rect()[2]//2
        self.originY = self.cover.get_rect()[3]//2
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

        Setting.backgroundStore.append(pygame.image.load('img/background.png'))
        #for i in range(1, self.backgroundPages + 1):
         #   Setting.backgroundStore.append(pygame.image.load('img/grids' + str(i) + '.jpg'))

set = Setting()
clock = pygame.time.Clock()
