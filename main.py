import pygame

win_width = 700
win_height = 500
bg_color = pygame.Color(255, 255, 255)
text_color = pygame.Color(0, 0, 0)


class MainGame():
    window = None
    my_tank = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小以及显示
        MainGame.window = pygame.display.set_mode([win_width, win_height])
        # 初始化我方坦克
        MainGame.my_tank = Tank(200, 300)
        # 设计标题
        pygame.display.set_caption('war of tank')
        while True:
            # 设置填充色
            MainGame.window.fill(bg_color)
            # 获取事件
            self.getEvent()
            # 调用坦克显示的方法
            MainGame.my_tank.displayTank()
            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print('exit')
        exit()

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        # 遍历事件
        for event in eventList:
            # 判断按下的键是关闭，还是方向
            # 如果按下的是退出
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                # 判断按下的是上下左右
                if event.key == pygame.K_LEFT:
                    MainGame.my_tank.direction = 'L'
                    MainGame.my_tank.move()
                    print('left')
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.move()
                    print('right')
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.move()
                    print('up')
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.move()
                    print('down')


class Tank():
    # 距离上，左
    def __init__(self, top, left):
        # 保存加载的图片
        self.images = {'U': pygame.image.load('img/tank-up.png'),
                       'D': pygame.image.load('img/tank-down.png'),
                       'L': pygame.image.load('img/tank-left.png'),
                       'R': pygame.image.load('img/tank-right.png')}
        # 方向
        self.direction = 'U'
        # 根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        # 速度 决定移动的快慢
        self.speed = 10

    # 移动
    def move(self):
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            self.rect.left -= self.speed
        elif self.direction == 'U':
            self.rect.top -= self.speed
        elif self.direction == 'D':
            self.rect.top += self.speed
        elif self.direction == 'R':
            self.rect.left += self.speed

    # 射击
    def shoot(self):
        pass

    # 展示坦克
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass


# 子弹类
class Bullet():
    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 展示子弹
    def displayBullet(self):
        pass


# 墙壁
class Wall():
    def __init__(self):
        pass

    # 展示墙壁
    def displayWall(self):
        pass


# 爆炸
class Explode():
    def __init__(self):
        pass

    # 爆炸效果
    def displayExplode(self):
        pass


# 音效
class Music():
    def __init__(self):
        pass

    # 展示音效
    def displayMusic(self):
        pass


if __name__ == '__main__':
    MainGame().startGame()

