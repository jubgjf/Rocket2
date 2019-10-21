import pygame


class BulletSupport(pygame.sprite.Sprite):
    """ 底部火力支援 """

    def __init__(self, screen, position):
        super(BulletSupport, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 子弹位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/BulletSupport.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (3, 10))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.top = self.position[1]

    def draw(self):
        """ 绘制子弹 """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ 子弹移动 """
        self.rect.centery -= 10
