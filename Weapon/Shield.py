import pygame


class Shield(pygame.sprite.Sprite):
    """ 护盾 """

    def __init__(self, screen, position):
        super(Shield, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 护盾位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/Shield.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 显示护盾 """
        self.screen.blit(self.image, self.rect)

    def move(self, ShipPosition, lenspeedup):
        """ 护盾移动 """
        if self.rect.centerx > ShipPosition[0]:
            self.rect.centerx -= 2 * (lenspeedup + 1)
        elif self.rect.centerx < ShipPosition[0]:
            self.rect.centerx += 2 * (lenspeedup + 1)
        if self.rect.centery > ShipPosition[1]:
            self.rect.centery -= 2 * (lenspeedup + 1)
        elif self.rect.centery < ShipPosition[1]:
            self.rect.centery += 2 * (lenspeedup + 1)
