import pygame
import json

pygame.init()


class ScoreBoard():
    """ 计分 """

    def __init__(self, screen, score, width, height, HighestScore=0):
        self.screen = screen
        """ 字体设置 """
        self.color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.score = str(score)
        self.HighestScore = str(self.LoadScore())

        self.ScoreSeq = (self.score, self.HighestScore)

        self.image = self.font.render('/'.join(self.ScoreSeq), True,
                                      self.color, (5, 70, 160))

        self.rect = self.image.get_rect()
        self.rect.right = width - 10
        self.rect.bottom = height - 10

    def draw(self):
        """ 显示分数 """
        self.screen.blit(self.image, self.rect)

    def LoadScore(self):
        """ 加载历史分数 """
        try:
            with open('ScoreBoard/HistoryScore.json', 'r') as f:
                HistoryScore = json.load(f)
        except:
            with open('ScoreBoard/HistoryScore.json', 'w') as f:
                json.dump(0, f)
                HistoryScore = 0
        return HistoryScore

    def UpdateScore(self, NewScore):
        """ 更新分数 """
        try:
            if NewScore > self.LoadScore():
                with open('ScoreBoard/HistoryScore.json', 'w') as f:
                    json.dump(NewScore, f)
        except:
            pass
