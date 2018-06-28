import pygame


class Setting:
    def __init__(self):
        self.background = []
        self.backgroundPages = 9
        for i in range(1,self.backgroundPages+1):
            self.background.append('img/grid'+str(i)+'.jpg')
        self.BGWIDTH = pygame.image.load(self.background[0]).get_rect()[2]
        self.BGHEIGHT = pygame.image.load(self.background[0]).get_rect()[3]


set = Setting()
screen = pygame.display.set_mode((set.BGWIDTH, set.BGHEIGHT))
clock = pygame.time.Clock()