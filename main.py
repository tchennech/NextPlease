import pygame, random, sys
from pygame.locals import *
from setting import *
from mySnake import MySnake
from enermy import OtherSnake
from attribute import Attribute
from balls.basicball import BasicBall
from balls.shield import Shield
from balls.heart import Heart
import math

# 全局变量
enermylist = []
# 设置
set = Setting()
# 屏幕
screen = pygame.display.set_mode((set.backgroundWidth, set.backgroundHeight), 0, 32)
# 初始化蛇
snake = MySnake(screen, set)
# 分数栏
attr = Attribute(screen)
# 设置状态
state = 0
starts = 0
infinity = 1
limit = 2
stops = 3
stopTemp = -1
finish = 4

# 按钮字
leftWord, rightWord = '无尽模式', '限时模式'

# 控制界面按钮
left, right = True, True

# 偏移
leftX = set.backgroundWidth // 2 - 20 - set.imgWidth
rightX = set.backgroundWidth // 2 + 30
height = set.backgroundHeight - 90

# 食物
normal = []
special = []

# 分数
score = 0

# 时间
timeIndex = 60

#生命
life = 1

#盾牌
shield = 0

#爱心
heart = 0

# 函数

# 初始化各个参数，  添加图片到内存中
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


def CountClock():
    global timeIndex, state
    timeIndex -= 0.1
    if timeIndex == 0:
        state = finish
        timeIndex = 60


# 键盘监听
def keyListen(event):
    snake.turn(event)


# 碰撞函数
def collision():
    global set, snake, state, finish
    # 判断蛇是否碰到边界
    if snake.hitBorder(set):
        state = finish

    # 碰撞食物与道具
    isEaten()


    global enermylist
    # 无敌时间削减
    snake.decreInvincibleTime()
    for i in enermylist:
        i.decreInvincibleTime()

    # 与敌方的碰撞
    allSnake = []
    allSnake.append(snake)
    allSnake.extend(enermylist)
    killList = []
    for i in range(len(allSnake)):
        for j in range(len(allSnake)):
            if i == j:
                continue
            if allSnake[i].hitOtherSnake(allSnake[j]):
                killList.append(allSnake[i])
    # 根据列表清除场上的蛇
    for i in killList:
        if i == snake:
            state = finish
        else:
            enermylist.remove(i)

    del allSnake
    del killList
        # 增添蛇

    while len(enermylist) < 5 :
        enermylist.append(OtherSnake(screen))



# 初始化食物
def initFood():
    for i in range(20):
        normal.append(BasicBall(screen))
    for i in range(5):
        special.append(Shield(screen, set.shieldImg, 5))
    for i in range(3):
        special.append(Heart(screen, set.heartImg, 5))


# 绘制食物
def foodPaint():
    for i in normal:
        i.blitme(set.rx, set.ry)
    for i in special:
        i.blitme(set.rx, set.ry)


# 绘制函数
def paint():
    bgPaint()
    borderPaint()
    snake.paint()
    attr.paintattribute()
    foodPaint()
    if state == limit:
        timePaint()
    for i in enermylist:
        i.paint()


def timePaint():
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 25)
    timeStr = ft.render('倒计时：%d s' % math.ceil(timeIndex), True, (75, 200, 200))
    screen.blit(timeStr, (30, 20))


# 绘制背景
def bgPaint():
    global set
    for x, y in set.backgroundPos:
        screen.blit(pygame.transform.scale(Setting.backgroundStore[0], (set.BGWIDTH, set.BGHEIGHT)), (x, y))


def borderPaint():
    global set
    for x, y in set.borderPos:
        screen.blit(pygame.transform.scale(Setting.borderImg, (set.BGWIDTH, set.BGHEIGHT)), (x, y))


# 各物体对象坐标变化
def dynamic():
    global set, state
    set.rx, set.ry = snake.moveaction()
    backgroundmove()

    # 无敌变色
    snake.wudi_paint()
    for i in enermylist:
        i.moveaction(set)
        i.wudi_paint()

# 背景(含边界黑幕)移动
def backgroundmove():
    global set
    for i in range(set.backgroundPages):
        set.backgroundPos[i][0] -= set.rx
        set.backgroundPos[i][1] -= set.ry
    for i in range(len(set.borderPos)):
        set.borderPos[i][0] -= set.rx
        set.borderPos[i][1] -= set.ry


def finishs():
    screen.blit(set.gameover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 30)
    stopStr = ft.render(str(score), True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth - 105, 60))


# 游戏结束后参数重置
def argsInit():
    global state, starts, snake, set, enermylist,score,life,shield
    life = 1
    shield = 0
    score = 0
    state = starts
    set.setInit()
    snake = MySnake(screen, set)
    enermylist.clear()
    for i in range(5):
        enermylist.append(OtherSnake(screen))


def stop():
    screen.blit(set.cover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 35)
    stopStr = ft.render("再次点击继续", True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth // 2 - 105, set.backgroundHeight - 80))


def isEaten():
    global score,attr,life,shield,snake
    for i in normal:
        if i.isEaten():
            normal.remove(i)
            score += 1
            snake.add()
            snake.num += 1
            attr.changestatue(score,life,shield)
    for i in special:
        if i.isEaten():
            if isinstance(i, Shield):
                snake.hasShield()
            elif isinstance(i, Heart):
                life += 1

            special.remove(i)



# 初始界面
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
    screen.blit(leftStr, (set.backgroundWidth // 2 - set.imgWidth + 30, set.backgroundHeight - 80))
    screen.blit(rightStr, (set.backgroundWidth // 2 + 80, set.backgroundHeight - 80))


# 事件处理
def action():
    mouseX, mouseY = pygame.mouse.get_pos()
    global state, left, right, stopTemp
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 键盘事件
        if event.type == KEYDOWN:
            keyListen(event)
        # 模式选择
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = pygame.mouse.get_pressed()[0]
            if state == starts:
                if left:
                    if mouseY > height and mouseY < height + 47:
                        if mouseX < leftX + 200 and mouseX > leftX:
                            state = infinity
                            initFood()
                        if mouseX > rightX and mouseX < rightX + 200:
                            state = limit
                            initFood()
            elif state == finish:
                argsInit()
                state = starts
            elif state == stops:
                state = stopTemp
            else:
                stopTemp = state
                state = stops
    if state == starts:
        left, right = True, True
        # 改变按钮
        if mouseY > height and mouseY < height + 47:
            if mouseX < leftX + 200 and mouseX > leftX:
                left = False
            if mouseX > rightX and mouseX < rightX + 200:
                right = False


# 主函数
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
            if state == limit:
                CountClock()
            # 碰撞函数
            collision()
            # 各物体对象坐标变化
            dynamic()

            paint()
            # 延时
            # pygame.time.delay(15)
            # 限制帧数
            clock.tick(60)
            # 刷新
        action()
        pygame.display.update()


if __name__ == '__main__':
    main()
