import pygame


class SpeedUp(pygame.sprite.Sprite):
    """ 加速 """

    def __init__(self, screen, position):
        super(SpeedUp, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 加速位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/SpeedUp.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.right = self.position[0]
        self.rect.bottom = self.position[1]

    def draw(self):
        """ 显示加速 """
        self.screen.blit(self.image, self.rect)

