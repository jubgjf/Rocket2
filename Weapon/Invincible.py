import pygame


class Invincible(pygame.sprite.Sprite):
    """ 无敌 """

    def __init__(self, screen, position):
        super(Invincible, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 无敌位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load(
            'pictures/Invincible.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 显示无敌 """
        self.screen.blit(self.image, self.rect)

    def move(self, ShipPosition, lenspeedup):
        """ 无敌移动 """
        if self.rect.centerx > ShipPosition[0]:
            self.rect.centerx -= 4 * (lenspeedup + 1)
        elif self.rect.centerx < ShipPosition[0]:
            self.rect.centerx += 4 * (lenspeedup + 1)
        if self.rect.centery > ShipPosition[1]:
            self.rect.centery -= 4 * (lenspeedup + 1)
        elif self.rect.centery < ShipPosition[1]:
            self.rect.centery += 4 * (lenspeedup + 1)
