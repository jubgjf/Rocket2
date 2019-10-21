import pygame


class AddFire(pygame.sprite.Sprite):
    """ 辅助发射器 """

    def __init__(self, screen, position):
        super(AddFire, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 辅助发射器位置 """
        self.position = position
        """ 加载图片 """
        self.image = pygame.image.load('pictures/AddFire.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

    def draw(self):
        """ 显示辅助发射器 """
        self.screen.blit(self.image, self.rect)

    def move(self, ShipPosition,lenspeedup,leninvincible):
        """ 辅助发射器移动 """
        if self.rect.centerx > ShipPosition[0]:
            self.rect.centerx -= 2*(lenspeedup+1)*(leninvincible+1)
        elif self.rect.centerx < ShipPosition[0]:
            self.rect.centerx += 2 * (lenspeedup + 1) * (leninvincible + 1)
        if self.rect.centery > ShipPosition[1]:
            self.rect.centery -= 2 * (lenspeedup + 1) * (leninvincible + 1)
        elif self.rect.centery < ShipPosition[1]:
            self.rect.centery += 2 * (lenspeedup + 1) * (leninvincible + 1)
