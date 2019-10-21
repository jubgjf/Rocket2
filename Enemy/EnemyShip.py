import pygame
import random
import time


class EnemyShip(pygame.sprite.Sprite):
    """ 外星人 """

    def __init__(self, screen, position):
        super(EnemyShip, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 外星人位置 """
        self.position = position
        """ 移动速度 """
        self.speed = [1, 1]
        """ 血量 """
        self.hp = 4
        """ 外星人发射子弹功能 """
        self.notShoot = random.randrange(0, 2, step=1)  #二分之一概率
        """ 加载图片 """
        if self.notShoot:
            if random.choice((0, 1)):
                self.image = pygame.image.load('pictures/EnemyShip.png')
                self.image = pygame.transform.smoothscale(self.image, (30, 40))
            else:
                self.image = pygame.image.load('pictures/EnemyShipClassic.png')
        else:
            if random.choice((0, 1)):
                self.image = pygame.image.load('pictures/EnemyShipShoot.png')
                self.image = pygame.transform.smoothscale(self.image, (30, 40))
            else:
                self.image = pygame.image.load(
                    'pictures/EnemyShipShootClassic.png')

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 绘制外星人 """
        self.screen.blit(self.image, self.rect)

    def move(self, width, height, AimDirection):
        """ 移动飞船 """
        if AimDirection[0] > self.rect.centerx:
            self.rect.centerx += self.speed[0]
        elif AimDirection[0] < self.rect.centerx:
            self.rect.centerx -= self.speed[0]
        if self.notShoot:
            if AimDirection[1] > self.rect.centery:
                self.rect.centery += self.speed[1]
            elif AimDirection[1] < self.rect.centery:
                self.rect.centery -= self.speed[1]
        else:
            if self.rect.centery >= height / 4:
                self.rect.centery -= self.speed[1]
            elif self.rect.centery < height / 4 - 10:
                self.rect.centery += self.speed[1]

    def drawHealth(self):
        """ 外星人血量 """
        self.healthRect = pygame.Rect(self.rect.left, self.rect.top - 5,
                                      7.5 * self.hp, 5)
        if self.hp == 4:
            self.healthColor = (50, 255, 50)
        elif self.hp == 2 or self.hp == 3:
            self.healthColor = (255, 255, 50)
        elif self.hp == 1:
            self.healthColor = (255, 50, 50)
        pygame.draw.rect(self.screen, self.healthColor, self.healthRect)

    def DrawGetFire(self, position):
        """ 外星人着火 """
        self.FireImage = pygame.image.load('pictures/EnemyShipGetFire.png')
        self.FireImage = pygame.transform.smoothscale(self.FireImage, (20, 20))
        self.FireRect = self.image.get_rect()
        self.FireRect.centerx, self.FireRect.centery = position[0], position[1]
        self.screen.blit(self.FireImage, self.FireRect)
        pygame.display.update(self.FireRect)
        time.sleep(0.001)


class EnemyBossShip(pygame.sprite.Sprite):
    """ 外星人Boss """

    def __init__(self, screen, position):
        super(EnemyBossShip, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 外星人位置 """
        self.position = position
        """ 移动速度 """
        self.speed = [1, 1]
        """ 血量 """
        self.hp = 20
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/EnemyBossShip.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (160, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 绘制外星人 """
        self.screen.blit(self.image, self.rect)

    def move(self, width, height, AimDirection):
        """ 移动飞船 """
        if AimDirection[0] > self.rect.centerx:
            self.rect.centerx += self.speed[0]
        elif AimDirection[0] < self.rect.centerx:
            self.rect.centerx -= self.speed[0]

        if self.rect.centery < height / 6:
            self.rect.centery += self.speed[1]

    def drawHealth(self):
        """ Boss血量 """
        self.healthRect = pygame.Rect(self.rect.left, self.rect.top - 5,
                                      8 * self.hp, 5)

        if self.hp >= 14:
            self.healthColor = (50, 255, 50)
        elif self.hp >= 6:
            self.healthColor = (255, 255, 50)
        else:
            self.healthColor = (255, 50, 50)
        pygame.draw.rect(self.screen, self.healthColor, self.healthRect)

