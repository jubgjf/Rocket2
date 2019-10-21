import pygame


class Missile(pygame.sprite.Sprite):
    """ 火箭导弹 """

    def __init__(self, screen, position):
        super(Missile, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 导弹位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Missile.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.bottom = self.position[1]

    def draw(self):
        """ 绘制导弹 """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ 导弹移动 """
        self.rect.centery -= 10


class MissileRange(pygame.sprite.Sprite):
    """ 火箭导弹溅射范围 """

    def __init__(self, screen, position):
        super(MissileRange, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 导弹溅射范围位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/MissileRange.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 绘制导弹溅射范围 """
        self.screen.blit(self.image, self.rect)

