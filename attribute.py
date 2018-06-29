import pygame
from setting import Setting

set = Setting()

class Attribute:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.life = 1
        self.shield = False

    # score: 变化后的分数
    # life: +1 加一条生命  -1 减一条生命  shield: true 有盾  false 无盾
    def changestatue(self, score, life, shield):
        self.score = score
        self.life += life
        self.shield = shield

    def paintattribute(self):
        # set.titleImage.convert_alpha(100)
        self.screen.blit(set.titleImage, (set.backgroundWidth - set.titleImage.get_rect()[2] - 30, 10))
        self.screen.blit(set.titleImage, \
                         (set.backgroundWidth - set.titleImage.get_rect()[2] - 30, \
                          set.titleImage.get_rect()[3]+20))
        self.screen.blit(set.titleImage, \
                         (set.backgroundWidth - set.titleImage.get_rect()[2] - 30, \
                          set.titleImage.get_rect()[3]*2 + 20))
        self.screen.blit(set.titleImage, \
                         (set.backgroundWidth - set.titleImage.get_rect()[2] - 30, \
                          set.titleImage.get_rect()[3]*3 + 20))

        pygame.font.init()
        ft = pygame.font.Font('font/butter.ttf', 25)
        # 标题
        titleStr = ft.render("我 的 属 性", True, (124, 150, 112))
        self.screen.blit(titleStr, (set.backgroundWidth - set.titleImage.get_rect()[2] - 15,17))
        # 分数
        scoreStr = ft.render("分 数： %d"%self.score, True, (124, 150, 112))
        self.screen.blit(scoreStr, (set.backgroundWidth - set.titleImage.get_rect()[2] - 15, 75))
        # 生命
        lifeStr = ft.render("生 命： %d" % self.life, True, (124, 150, 112))
        self.screen.blit(lifeStr, (set.backgroundWidth - set.titleImage.get_rect()[2] - 15, 115))
        # BUFF
        s = ""
        if self.shield:
            s += "盾牌"
        else:
            s += "无"
        shieldStr = ft.render("BUFF： %s" % s, True, (124, 150, 112))
        self.screen.blit(shieldStr, (set.backgroundWidth - set.titleImage.get_rect()[2] - 15, 155))


