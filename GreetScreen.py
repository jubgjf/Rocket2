import pygame


class GreetScreen():
    """ 游戏标题 """

    def __init__(self, width):
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Title.png').convert_alpha()
        self.image.set_colorkey((5, 70, 160))
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.top = 20

    def DrawTitle(self, screen):
        """ 显示按钮 """
        """ 显示屏幕 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)
