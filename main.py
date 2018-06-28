import pygame, random, sys
from pygame.locals import *
from setting import *
from Snake import Snake
from enermy import OtherSnake
# 全局变量
snake = Snake(screen)
enermylist = []

# 函数

#键盘监听
def keyListen(event):
    snake.turn(event)

# 碰撞函数
def collision():
    pass

# 绘制函数
def paint():
    bgPaint()
    borderPaint()
    snake.paint_Hero()
    for i in enermylist:
        i.paint()

# 绘制背景
def bgPaint():
    global set
    i = 0
    for x, y in set.backgroundPos:
        tempImg = pygame.image.load(set.background[i])
        screen.blit(pygame.transform.scale(tempImg,(set.BGWIDTH,set.BGHEIGHT)), (x,y))
        i+=1

def borderPaint():
    global set
    for x, y in set.borderPos:
        tempImg = pygame.image.load('img/border.jpg')
        screen.blit(pygame.transform.scale(tempImg, (set.BGWIDTH, set.BGHEIGHT)), (x, y))

# 各物体对象坐标变化
def dynamic():
    global set
    set.rx, set.ry= snake.moveaction()
    backgroundmove()
    for i in enermylist:
        i.moveaction()


# 背景(含边界黑幕)移动
def backgroundmove():
    global set
    for i in range(set.backgroundPages):
        set.backgroundPos[i][0]-= set.rx
        set.backgroundPos[i][1]-= set.ry
    for i in range(len(set.borderPos)):
        set.borderPos[i][0]-=set.rx
        set.borderPos[i][1]-=set.ry



if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Snake')
    # 键盘重复监听
    pygame.key.set_repeat(2, 10)
    # 音效 初始化
    pygame.mixer.init()

    # 初始化 敌人
    for i in range(5):
        enermylist.append(OtherSnake(screen))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                keyListen(event)


        # 碰撞函数
        collision()
        # 各物体对象坐标变化
        dynamic()
        # 绘制函数
        paint()
        # 延迟，  待替换
        #pygame.time.delay(15)
        # 限制帧数
        clock.tick(60)
        # 刷新
        pygame.display.update()

