import pygame


class TimeBar(pygame.sprite.Sprite):
    """ 激光缓冲进度 """

    def __init__(self, screen, ScreenHeight, TimeBarHeight, FireFrequency,
                 MaxFireFrequency):
        super(TimeBar, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        self.ScreenHeight = ScreenHeight
        self.TimeBarHeight = TimeBarHeight
        """ 矩形 """
        if FireFrequency <= MaxFireFrequency:
            self.color = (255, 255, 0)  #黄色
            self.rect = pygame.Rect(20, self.ScreenHeight - self.TimeBarHeight,
                                    100 * FireFrequency / MaxFireFrequency, 10)
        else:
            self.color = (0, 255, 0)  #绿色
            self.rect = pygame.Rect(20, self.ScreenHeight - self.TimeBarHeight,
                                    100, 10)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class TimeBarPictures():
    """ 缓冲进度标识 """

    def __init__(self, screen, ScreenHeight, height):
        self.ScreenHeight = ScreenHeight
        self.height = height
        self.screen = screen

    def DrawTimeBarLaser(self):
        """ 绘制激光 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarLaser.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarShield(self):
        """ 绘制护盾 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarShield.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarAddFire(self):
        """ 绘制辅助发射器 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarAddFire.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarSpeedUp(self):
        """ 绘制加速 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarSpeedUp.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarAttachAircraft(self):
        """ 绘制跟随飞船 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarAttachAircraft.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarInvincible(self):
        """ 绘制无敌 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarInvincible.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarBulletSupport(self):
        """ 绘制底部火力支援 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarBulletSupport.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarMissile(self):
        """ 绘制导弹 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarMissile.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)

    def DrawTimeBarOmegaLaser(self):
        """ 绘制追踪激光 """
        self.image = pygame.image.load(
            'pictures/TimeBarPictures/TimeBarOmegaLaser.png')
        self.rect = self.image.get_rect()
        self.rect.centery=self.ScreenHeight-self.height
        self.screen.blit(self.image, self.rect)
