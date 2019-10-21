import pygame
from Settings import *


class HelpScreen():
    """ 帮助界面 """

    def __init__(self, width,height):
        self.width=width
        self.height=height
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Help.png').convert_alpha()
        """ 矩形 """
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width/2
        self.rect.centery = self.height / 2

    def draw(self, screen):
        """ 显示按钮 """
        self.screen = screen
        self.screen.blit(self.image, self.rect)
