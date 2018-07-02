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
from balls.bigball import BigBall
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
timeIndex = 30


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


# 进行倒计时
def CountClock():
    global timeIndex, state
    timeIndex -= 0.05
    if math.ceil(timeIndex)==0:
        state = finish


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
    #设置边界
    x = [set.backgroundPos[0][0] + 50, set.backgroundPos[6][0]+set.BGWIDTH-50]
    y = [set.backgroundPos[0][1] + 50, set.backgroundPos[2][1]+set.BGHEIGHT-50]

    #普通食物
    for i in range(20-len(normal)):
        normal.append(BasicBall(screen, x, y))

    #特殊道具
    for i in range(8-len(special)):
        randomNum = random.randint(0,2)
        if randomNum == 0:
            special.append(Shield(screen, set.shieldImg, 5, x, y))
        elif randomNum == 1:
            special.append(Heart(screen, set.heartImg, 5, x, y))
        else:
            special.append(BigBall(screen, x, y))

# 绘制食物
def foodPaint():
    for i in normal:
        i.blitme(set.rx, set.ry)
    for i in special:
        i.blitme(set.rx, set.ry)


# 绘制函数
def paint():
    global attr
    bgPaint()
    borderPaint()
    snake.paint()
    attr.life = snake.life
    attr.paintattribute()
    foodPaint()
    if state == limit:
        timePaint()
    for i in enermylist:
        i.paint()

# 绘制计时器
def timePaint():
    pygame.font.init()
    fontSize = 20
    colorAttr = (50, 65, 80)
    if timeIndex < 10:
        colorAttr = (250, 0, 0)
        fontSize = 35

    ft_word = pygame.font.Font('font/fonts.ttf', 20)
    ft_time = pygame.font.Font('font/fonts.ttf', fontSize)

    timeStr = ft_word.render('%d'% math.ceil(timeIndex), True, colorAttr)
    imgIndex = int(timeIndex/8)
    ClockImg = pygame.image.load(set.ClockImg[imgIndex])
    screen.blit(ft_time.render('倒计时：', True, (50, 65, 80)), (30, 20))
    screen.blit(ClockImg, (42, 35))
    screen.blit(timeStr, (42, 80))



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

#结束状态
def finishs():
    screen.blit(set.gameover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 30)
    stopStr = ft.render(str(score), True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth - 105, 65))


# 游戏结束后参数重置
def argsInit():
    global state, starts, snake, set, enermylist, score, shield, attr, normal, special, timeIndex
    shield = 0
    score = 0
    state = starts
    timeIndex = 30
    set.setInit()
    attr = Attribute(screen)
    normal = []
    special = []
    snake = MySnake(screen, set)
    enermylist.clear()
    for i in range(5):
        enermylist.append(OtherSnake(screen))

#暂停状态
def stop():
    screen.blit(set.cover, (0, 0))
    pygame.font.init()
    ft = pygame.font.Font('font/fonts.ttf', 35)
    stopStr = ft.render("再次点击继续", True, (0, 0, 0))
    screen.blit(stopStr, (set.backgroundWidth // 2 - 105, set.backgroundHeight - 80))

#食物或道具被吃
def isEaten():
    global score,attr,shield,snake
    for i in normal:
        if i.isEaten():
            normal.remove(i)
            score += 1
            snake.add()
            snake.num += 1
            attr.changestatue(score, snake.life,shield)
    for i in special:
        if i.isEaten():
            if isinstance(i, Shield):
                snake.hasShield()
            elif isinstance(i, Heart):
                attr.life += 1
                snake.life += 1
            elif isinstance(i, BigBall):
                score += 10
                for j in range(10):
                    snake.add()
                snake.num += 10
                attr.changestatue(score, snake.life, shield)


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
            initFood()
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
