from balls.buff import Buff
import pygame, random


class Heart(Buff):
    def __init__(self, screen, image, radius):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.width = self.image.get_rect()[2]
        self.x = random.randint(0, 500 - self.width)
        self.y = -random.randint(0, 500)
        self.radius = radius
        # self.xStep = 1
        super(Heart, self).__init__(screen, self.image, self.radius)