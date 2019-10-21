import pygame


class Bullet(pygame.sprite.Sprite):
    """ 火箭子弹 """

    def __init__(self, screen, position):
        super(Bullet, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 子弹位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Bullet.png').convert_alpha()
        self.image.set_colorkey((5, 70, 160))
        self.image = pygame.transform.smoothscale(self.image, (3, 10))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.bottom = self.position[1]

    def draw(self):
        """ 绘制子弹 """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ 子弹移动 """
        self.rect.centery -= 5
