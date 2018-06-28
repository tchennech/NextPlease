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
        self.backgroundPos = [[-self.BGWIDTH,-self.BGHEIGHT],[-self.BGWIDTH, 0], [-self.BGWIDTH, self.BGHEIGHT],
                              [0,-self.BGHEIGHT], [0, 0], [0, self.BGHEIGHT],
                              [self.BGWIDTH, -self.BGHEIGHT], [self.BGWIDTH, 0],[self.BGWIDTH,self.BGHEIGHT]]
        for i in range(1,self.backgroundPages+1):
            self.background.append('img/grids'+str(i)+'.jpg')
        #self.BGWIDTH = pygame.image.load(self.background[0]).get_rect()[2]
        #self.BGHEIGHT = pygame.image.load(self.background[0]).get_rect()[3]



set = Setting()
screen = pygame.display.set_mode((set.BGWIDTH, set.BGHEIGHT))
clock = pygame.time.Clock()