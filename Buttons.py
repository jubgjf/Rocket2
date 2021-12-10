import pygame


class StartGameButton(pygame.sprite.Sprite):
    """ 开始游戏按钮 """

    def __init__(self, width, height):
        super(StartGameButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/GreetScreen/StartGameButton.png').convert_alpha(
            )
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 - 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 1 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 10
        elif choose != 1 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 10


class OptionButton(pygame.sprite.Sprite):
    """ 设置按钮 """

    def __init__(self, width, height):
        super(OptionButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/GreetScreen/OptionButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 2 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 10
        elif choose != 2 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 10


class HelpButton(pygame.sprite.Sprite):
    """ 帮助按钮 """

    def __init__(self, width, height):
        super(HelpButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/GreetScreen/HelpButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 + 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 3 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 10
        elif choose != 3 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 10


class QuitGameButton(pygame.sprite.Sprite):
    """ 退出游戏按钮 """

    def __init__(self, width, height):
        super(QuitGameButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/GreetScreen/QuitGameButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 + 200

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 4 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 10
        elif choose != 4 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 10


class PauseBackground(pygame.sprite.Sprite):
    """ 暂停背景 """

    def __init__(self, height):
        super(PauseBackground, self).__init__()
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/PauseBackground.png').convert_alpha()
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示背景 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def MoveIn(self):
        if self.rect.centerx < 100:
            self.rect.centerx += 10


class PauseResumeButton(pygame.sprite.Sprite):
    """ 结束暂停按钮 """

    def __init__(self, height):
        super(PauseResumeButton, self).__init__()
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Pause/PauseResumeButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 50))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = self.height / 2 - 200

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def MoveIn(self):
        if self.rect.centerx < 100:
            self.rect.centerx += 5

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 1 and self.rect.centerx <= 130:
            self.rect.centerx += 1
        elif choose != 1 and self.rect.centerx > 100:
            self.rect.centerx -= 1


class PauseOptionButton(pygame.sprite.Sprite):
    """ 暂停时设置按钮 """

    def __init__(self, height):
        super(PauseOptionButton, self).__init__()
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Pause/PauseOptionButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 50))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = self.height / 2 - 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def MoveIn(self):
        if self.rect.centerx < 100:
            self.rect.centerx += 5

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 2 and self.rect.centerx <= 130:
            self.rect.centerx += 1
        elif choose != 2 and self.rect.centerx > 100:
            self.rect.centerx -= 1


class PauseGoMenuButton(pygame.sprite.Sprite):
    """ 返回起始界面按钮 """

    def __init__(self, height):
        super(PauseGoMenuButton, self).__init__()
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Pause/PauseGoMenuButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 50))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def MoveIn(self):
        if self.rect.centerx < 100:
            self.rect.centerx += 5

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 3 and self.rect.centerx <= 130:
            self.rect.centerx += 1
        elif choose != 3 and self.rect.centerx > 100:
            self.rect.centerx -= 1


class PauseQuitButton(pygame.sprite.Sprite):
    """ 结束游戏按钮 """

    def __init__(self, height):
        super(PauseQuitButton, self).__init__()
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Pause/PauseQuitButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (150, 50))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = self.height / 2 + 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def MoveIn(self):
        if self.rect.centerx < 100:
            self.rect.centerx += 5

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 4 and self.rect.centerx <= 130:
            self.rect.centerx += 1
        elif choose != 4 and self.rect.centerx > 100:
            self.rect.centerx -= 1


class OptionBackground(pygame.sprite.Sprite):
    """ 设置界面背景 """

    def __init__(self, width, height):
        super(OptionBackground, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/OptionBackground.png').convert_alpha()
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示背景 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)


class OptionChangeMusicButton(pygame.sprite.Sprite):
    """ 更换音乐按钮 """

    def __init__(self, width, height):
        super(OptionChangeMusicButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Option/ChangeMusicButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 - 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 1 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 2
        elif choose != 1 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 2


class OptionChangeAirCraftButton(pygame.sprite.Sprite):
    """ 更换飞船按钮 """

    def __init__(self, width, height):
        super(OptionChangeAirCraftButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Option/ChangeAircraftButton.png').convert_alpha(
            )
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 2 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 2
        elif choose != 2 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 2


class OptionChangeModeButton(pygame.sprite.Sprite):
    """ 更换游戏模式按钮 """

    def __init__(self, width, height):
        super(OptionChangeModeButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Option/ChangeModeButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 + 100

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 3 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 2
        elif choose != 3 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 2


class OptionChangeScreenSizeButton(pygame.sprite.Sprite):
    """ 更换屏幕尺寸按钮 """

    def __init__(self, width, height):
        super(OptionChangeScreenSizeButton, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Option/ChangeScreenSizeButton.png'
        ).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width - 300
        self.rect.centery = self.height / 2 + 200

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)

    def TempChoose(self, choose):
        """ 暂时选择 """
        if choose == 4 and self.rect.centerx >= self.width - 350:
            self.rect.centerx -= 2
        elif choose != 4 and self.rect.centerx < self.width - 300:
            self.rect.centerx += 2


class ShowMusicAlbum(pygame.sprite.Sprite):
    """ 显示封面 """

    def __init__(self, width, height):
        super(ShowMusicAlbum, self).__init__()
        self.width = width
        self.height = height
        """ 加载图片 """
        self.ImageList = []
        self.ImageList.append(
            pygame.image.load('Music/9h00.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/Distress_Signa.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/Exchange.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/MN84_Theme.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/Shoulder_of_Orion.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/Sung-Thunder_Love.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/SYNTHWAVE_DEMO_02.jpg').convert_alpha())
        self.ImageList.append(
            pygame.image.load('Music/Spoiler_Original_Mix.jpg').convert_alpha())

    def draw(self, screen, number):
        """ 绘制封面 """
        self.screen = screen
        self.number = number
        """ 加载图片 """
        self.image = self.ImageList[self.number]
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2 - 200
        self.rect.centery = self.height / 2
        """ 显示 """
        self.screen.blit(self.image, self.rect)


class ScreenSize():
    """ 屏幕尺寸选择按钮 """

    def __init__(self):
        """ 加载图片 """
        self.AllImage = []
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/Width.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/600.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/800.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1000.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1200.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1400.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1600.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/Height.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/600.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/800.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1000.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/1200.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/IsFull.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/FullScreen.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/NotFullScreen.png'))
        self.AllImage.append(
            pygame.image.load('pictures/Buttons/ScreenSize/ChooseSize.png'))
        """ 按钮矩形 """
        self.AllRect = []
        for i in range(0, 16):
            self.AllRect.append(self.AllImage[i].get_rect())
        """ 设置位置 """
        for i in range(0, 7):
            self.AllRect[i].centerx = 150
            self.AllRect[i].centery = 100 * i + 100
        for i in range(7, 12):
            self.AllRect[i].centerx = 400
            self.AllRect[i].centery = 100 * i - 600
        for i in range(12, 15):
            self.AllRect[i].centerx = 650
            self.AllRect[i].centery = 100 * i - 1100

    def draw(self, screen, width, height):
        """ 绘制按钮 """
        self.screen = screen
        self.width = width
        self.height = height

        for i in range(0, 15):
            self.screen.blit(self.AllImage[i], self.AllRect[i])

    def TempChoose(self, screen, CenterList):
        self.screen = screen
        if CenterList[0] > 0:
            self.AllRect[15].centerx = CenterList[0]
            self.AllRect[15].centery = CenterList[1]
            self.screen.blit(self.AllImage[15], self.AllRect[15])
        else:
            pass


class AgainButton():
    """ 重新开始按钮 """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Buttons/Again/AgainButton.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (200, 75))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)
