import pygame


class OmegaLaser(pygame.sprite.Sprite):
    """ 追踪激光 """

    def __init__(self, screen, position):
        super(OmegaLaser, self).__init__()
        """ 显示屏幕 """
        self.screen = screen
        """ 追踪激光位置 """
        self.position = position
        """ 颜色 """
        self.color = (255, 0, 0)
        """ 加载矩形 """
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.centerx = self.position[0]
        self.rect.bottom = self.position[1]

    def draw(self):
        """ 显示追踪激光 """
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self, group):
        """ 追踪外星人 """
        for target in group:
            if self.rect.centerx > target.rect.centerx:
                self.rect.centerx -= 10
            elif self.rect.centerx < target.rect.centerx:
                self.rect.centerx += 10
            if self.rect.centery > target.rect.centery:
                self.rect.centery -= 10
            elif self.rect.centery < target.rect.centery:
                self.rect.centery += 10
            break

