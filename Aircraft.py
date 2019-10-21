import pygame
import json


class Aircraft(pygame.sprite.Sprite):
    """ 玩家控制的飞行器 """

    def __init__(self, screen, position):
        super(Aircraft, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 火箭种类 """
        self.AircraftNumber = self.LoadAircraftChoose()
        """ 火箭位置 """
        self.position = position
        """ 火箭速度 """
        self.speed = [2, 2]
        """ 加载图片 """
        self.AllImage = []
        self.AllImage.append(
            pygame.image.load('pictures/Aircraft/0.png').convert_alpha())
        self.AllImage.append(
            pygame.image.load('pictures/Aircraft/1.png').convert_alpha())
        self.AllImage.append(
            pygame.image.load('pictures/Aircraft/2.png').convert_alpha())
        self.AllImage.append(
            pygame.image.load('pictures/Aircraft/3.png').convert_alpha())
        self.AllImage.append(
            pygame.image.load('pictures/Aircraft/4.png').convert_alpha())
        self.image = pygame.transform.smoothscale(self.AllImage[self.AircraftNumber], (50, 40))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 绘制火箭 """
        self.screen.blit(self.image, self.rect)

    def move(self, width, height):
        """ 火箭移动 """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.centery -= self.speed[1]
        if keys[pygame.K_s] and self.rect.bottom <= height:
            self.rect.centery += self.speed[1]
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.centerx -= self.speed[0]
        if keys[pygame.K_d] and self.rect.right <= width:
            self.rect.centerx += self.speed[0]

    def OptionDraw(self,width,height,choose):
        """ 设置界面绘制火箭 """
        self.OptionImage = self.AllImage[choose]
        self.OptionRect = self.AllImage[choose].get_rect()
        self.OptionRect.centerx=400
        self.OptionRect.centery=height/2
        self.screen.blit(self.OptionImage,self.OptionRect)

    def LoadAircraftChoose(self):
        """ 读取火箭选择 """
        try:
            with open('AircraftChoose.json', 'r') as f:
                HistoryChoose = json.load(f)
            return HistoryChoose
        except:
            DefaultChoose = 1
            with open('AircraftChoose.json', 'w') as f:
                HistoryChoose = json.dump(DefaultChoose, f)
            return DefaultChoose
    
