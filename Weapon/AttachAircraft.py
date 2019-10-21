import pygame


class AttachAircraft(pygame.sprite.Sprite):
    """ 跟随飞船 """

    def __init__(self, screen, position):
        super(AttachAircraft, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 跟随飞船位置 """
        self.position = position
        """ 移动速度 """
        self.speed = [2, 2]
        """ 血量 """
        self.hp = 5
        """ 加载图片 """
        self.image = pygame.image.load('pictures/AttachAircraft.png')
        self.image = pygame.transform.smoothscale(self.image, (40,30))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 绘制跟随飞船 """
        self.screen.blit(self.image, self.rect)

    def move(self, height,group):
        """ 追踪外星人 """
        for target in group:
            if self.rect.centerx > target.rect.centerx:
                self.rect.centerx -= self.speed[0]
            elif self.rect.centerx < target.rect.centerx:
                self.rect.centerx += self.speed[0]
            if self.rect.centery > target.rect.centery+200:
                self.rect.centery -= self.speed[1]
            elif self.rect.centery < target.rect.centery+200 and self.rect.bottom<=height:
                self.rect.centery += self.speed[1]
            break

    def DrawHealth(self):
        """ 跟随飞船血量 """
        self.HealthRect = pygame.Rect(self.rect.left, self.rect.bottom,
                                      8 * self.hp, 2)
        if self.hp ==5:
            self.HealthColor = (50, 255, 50)
        elif self.hp == 3 or self.hp==4:
            self.HealthColor = (255, 255, 50)
        elif self.hp <= 2:
            self.HealthColor = (255, 50, 50)
        pygame.draw.rect(self.screen, self.HealthColor, self.HealthRect)
