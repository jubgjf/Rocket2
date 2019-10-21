import pygame
import random


class Stars(pygame.sprite.Sprite):
    """ 星空 """

    def __init__(self,screen,width,height,StarRemove=0):
        super(Stars, self).__init__()
        """ 显示屏幕 """
        self.screen=screen
        self.width = width
        self.height = height
        """ 是否由于刷新 """
        self.StarRemove=StarRemove
        """ 生成范围 """
        GenerateWidth=random.randrange(0,self.width,step=1)
        GenerateHeight=random.randrange(0,self.height,step=1)
        """ 矩形 """
        if StarRemove:
            self.rect = pygame.Rect(GenerateWidth, 0, 2, 2)
        else:
            self.rect = pygame.Rect(GenerateWidth, GenerateHeight, 2, 2)
        """ 颜色 """
        self.color = (255, 255, 255)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def move(self):
        self.rect.centery+=1

        