import pygame, random, sys
from pygame.locals import *
from setting import *
from Snake import Snake
# 全局变量
snake = Snake(screen)


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
    snake.paint_Hero()


# 绘制背景
def bgPaint():
    i = 0
    for x, y in set.backgroundPos:
        tempImg = pygame.image.load(set.background[i])
        print(x,y)
        screen.blit(pygame.transform.scale(tempImg,(set.BGWIDTH,set.BGHEIGHT)), (x,y))
        i+=1

# 各物体对象坐标变化
def dynamic():
    global set
    set.rx, set.ry= snake.moveaction()
    backgroundmove()


# 背景移动
def backgroundmove():
    global set
    for i in range(set.backgroundPages):
        set.backgroundPos[i][0]-= set.rx
        set.backgroundPos[i][1]-= set.ry



if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Snake')
    # 键盘重复监听
    pygame.key.set_repeat(2, 10)
    # 音效 初始化
    pygame.mixer.init()

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
        pygame.time.delay(20)
        # 限制帧数
        clock.tick(30)
        # 刷新
        pygame.display.update()

