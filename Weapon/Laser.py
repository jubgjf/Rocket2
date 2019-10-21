import pygame


class Laser(pygame.sprite.Sprite):
    """ 激光 """

    def __init__(self, screen, position):
        super(Laser, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 激光位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Laser.png').convert_alpha()
        self.image.set_colorkey((5, 70, 160))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.bottom = self.position[1]

    def draw(self):
        """ 绘制激光 """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ 激光移动 """
        self.rect.centery -= 10
