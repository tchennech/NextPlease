import pygame


class Setting:
    def __init__(self):
        self.background = []
        self.backgroundPages = 9
        self.backgroundPos = [(-300,-300),(-300, 0), (-300, 300), (0,-300), (0, 0), (0, 300), (300, -300), (300, 0)
                              ,(300,300)]
        for i in range(1,self.backgroundPages+1):
            self.background.append('img/grids'+str(i)+'.jpg')
        #self.BGWIDTH = pygame.image.load(self.background[0]).get_rect()[2]
        #self.BGHEIGHT = pygame.image.load(self.background[0]).get_rect()[3]
        self.BGWIDTH = 400
        self.BGHEIGHT = 400
        self.originX = 200
        self.originY = 200


set = Setting()
screen = pygame.display.set_mode((set.BGWIDTH, set.BGHEIGHT))
clock = pygame.time.Clock()