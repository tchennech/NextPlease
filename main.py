import pygame, random, sys
from pygame.locals import *
from setting import *
from Snake import Snake
from enermy import OtherSnake
# 全局变量
enermylist = []
#设置
set = Setting()
#屏幕
screen = pygame.display.set_mode((set.backgroundWidth,set.backgroundHeight),0,32)
#初始化蛇
snake = Snake(screen)
#设置状态
state = 0
starts = 0
infinity = 1
limit = 2
stops = 3
stopTemp = -1
finish = 4
#按钮字
leftWord, rightWord = '无尽模式', '限时模式'

#控制界面按钮
left, right = True, True
#偏移
leftX = set.backgroundWidth//2-20-set.imgWidth
rightX = set.backgroundWidth//2+30
height = set.backgroundHeight-90

#分数
score = 0

# 函数

#初始化
def initGame():
    pygame.init()
    pygame.display.set_caption("贪吃蛇大作战")
    # 键盘重复监听
    pygame.key.set_repeat(20, 5)
    # 音效 初始化
    pygame.mixer.init()
    # 初始化 敌人
    for i in range(5):
        enermylist.append(OtherSnake(screen))

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

def finishs():
    screen.blit(set.gameover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 30)
    stopStr = ft.render(str(score), True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth - 105, 60))
def stop():
    screen.blit(set.cover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 35)
    stopStr = ft.render("再次点击继续", True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth // 2 - 105, set.backgroundHeight - 80))
#初始界面
def start():
    screen.blit(set.cover, (0, 0))
    if left:
        screen.blit(set.leftImg, (leftX, height))
    else:
        screen.blit(set.pressImg, (leftX, height))
    if right:
        screen.blit(set.rightImg, (rightX, height))
    else:
        screen.blit(set.pressImg, (rightX, height))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 25)
    leftStr = ft.render(leftWord, True, (0, 0, 0))
    rightStr = ft.render(rightWord, True, (0, 0, 0))
    screen.blit(leftStr, (set.backgroundWidth//2-set.imgWidth+30, set.backgroundHeight-80))
    screen.blit(rightStr, (set.backgroundWidth//2+80, set.backgroundHeight-80))

#事件处理
def action():
    mouseX, mouseY = pygame.mouse.get_pos()
    global state, left, right, stopTemp
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #键盘事件
        if event.type == KEYDOWN:
            keyListen(event)
        #模式选择
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = pygame.mouse.get_pressed()[0]
            if state == starts:
                if left:
                    if mouseY > height and mouseY < height + 47:
                        if mouseX < leftX + 200 and mouseX > leftX:
                            state = infinity
                        if mouseX > rightX and mouseX < rightX + 200:
                            state = limit
            elif state == finish:
                state = starts
            elif state == stops:
                state = stopTemp
            else:
                stopTemp = state
                state = stops
    if state == starts:
        left, right = True, True
        #改变按钮
        if mouseY > height and mouseY < height+47:
            if mouseX < leftX+200 and mouseX > leftX:
                left = False
            if mouseX > rightX and mouseX < rightX+200:
                right = False



#主函数
def main():
    initGame()
    while True:
        if state == starts:
            start()
        elif state == stops:
            stop()
        elif state == finish:
            finishs()
        elif state != stops:
            # 碰撞函数
            collision()
            # 各物体对象坐标变化
            dynamic()
            paint()
            #延时
            #pygame.time.delay(15)
            # 限制帧数
            clock.tick(60)
            # 刷新
        action()
        pygame.display.update()

if __name__ == '__main__':
    main()
