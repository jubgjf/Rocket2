import pygame
from sys import exit
from Buttons import AgainButton


class CheckActions():
    """ 检测玩家活动 """

    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def CheckAlterChoose(self, Choose, ChooseStart, ChooseEnd, IfLoop):
        """ 检测更换选择 """
        if self.keys[pygame.K_s] and Choose <= ChooseEnd - 1:
            return 1, Choose + 1
        elif self.keys[pygame.K_w] and Choose >= ChooseStart + 1:
            return 1, Choose - 1
        if IfLoop:
            if self.keys[pygame.K_s] and Choose == ChooseEnd:
                return 1, ChooseStart
            elif self.keys[pygame.K_w] and Choose == ChooseStart:
                return 1, ChooseEnd
        return 0, Choose

    def CheckConfirmChoose(self, Choose, ResultTuple):
        """ 检测选择确认 """
        if self.keys[pygame.K_RETURN]:
            for i in range(1, len(ResultTuple) + 1):
                if Choose == i:
                    return ResultTuple[i - 1]

    def CheckConfirmMusicAircraft(self, Choose):
        """ 检测音乐/火箭确认 """
        if self.keys[pygame.K_RETURN]:
            return Choose

    def CheckGoBack(self, status):
        """ 检测返回 """
        if status:
            if self.keys[pygame.K_ESCAPE]:
                return 0
        return status

    def CheckQuitGame(self):
        """ 检测退出 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        return 1

    def CheckPause(self, PauseStatus):
        """ 检测暂停 """
        if self.keys[pygame.K_ESCAPE]:
            return 1
        return PauseStatus

    def CheckFire(self, group, element, key, addfireready=0, addfire=0):
        """ 检测使用武器 """
        if not addfireready and self.keys[key]:
            group.add(element)
            return 1
        elif addfireready and not addfire and self.keys[key]:
            group.add(element[0])
            return 1
        elif addfireready and addfire and self.keys[key]:
            for ele in element:
                group.add(ele)
            return 1

    def CheckAgainChoose(self, screen, width, height, ifagain):
        """ 检测重新开始 """
        AgainButton(width, height).draw(screen)
        pygame.display.update(AgainButton(width, height).rect)
        """ 检测退出游戏 """
        self.CheckQuitGame()
        """ 检测重新开始 """
        if self.keys[pygame.K_RETURN]:
            return 1
        else:
            return ifagain

    def CheckMouse(self, SomeRect):
        if self.mouse[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if SomeRect.collidepoint(mouse_x, mouse_y):
                return [SomeRect.centerx, SomeRect.centery]
