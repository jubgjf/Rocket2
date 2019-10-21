import pygame
import json


class Settings():
    """ 游戏设置 """

    def __init__(self):
        """ 窗口 """
        self.MainScreenWidth = int(self.LoadScreenSettings()[0])
        self.MainScreenHeight = int(self.LoadScreenSettings()[1])
        self.WindowsTitle = 'Rocket'
        self.WindowsIcon = pygame.image.load(
            'pictures/Icon.png')
        """ 背景 """
        self.MainScreenBackground = (5, 70, 160)

    def LoadScreenSettings(self):
        """ 读取屏幕设置 """
        try:
            with open('ScreenSettings.json', 'r') as f:
                HistorySettings = json.load(f)
            return HistorySettings.split('_')
        except:
            DefaultSettings='1200_800_NotFull'
            with open('ScreenSettings.json', 'w') as f:
                HistorySettings = json.dump(DefaultSettings, f)
            return DefaultSettings.split('_')

    def SetMainScreen(self):
        """ 屏幕设置 """
        if self.LoadScreenSettings()[2]=='Full':
            self.MainScreen = pygame.display.set_mode(
                (self.MainScreenWidth, self.MainScreenHeight),flags=pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
        elif self.LoadScreenSettings()[2]=='NotFull':
            self.MainScreen = pygame.display.set_mode(
                (self.MainScreenWidth, self.MainScreenHeight))
        pygame.display.set_caption(self.WindowsTitle)
        pygame.display.set_icon(self.WindowsIcon)
        return self.MainScreen
    
    def LoadAircraft(self):
        """ 读取火箭选择 """
        try:
            with open('AircraftChoose.json', 'r') as f:
                return json.load(f)
        except:
            pass

    def SetAircraftChoose(self,choose):
        """ 设置火箭选择 """
        try:
            with open('AircraftChoose.json', 'w') as f:
                json.dump(choose, f)
        except:
            pass

    def OptionSetScreenSize(self,CenterList):
        """ 设置屏幕尺寸 """
        OptionSettings = [0, 0, 0]
        try:
            with open('ScreenSettings.json', 'w') as f:
                for i in range(1, 7):
                    if CenterList[0][1] == 100 * i + 100:
                        OptionSettings[0] = str(200 * i + 400)
                for i in range(1, 5):
                    if CenterList[1][1] == 100 * i + 100:
                        OptionSettings[1] = str(200 * i + 400)
                if CenterList[2][1] == 200:
                    OptionSettings[2]='Full'
                elif CenterList[2][1] == 300:
                    OptionSettings[2] = 'NotFull'
                json.dump(OptionSettings[0] + '_' + OptionSettings[1] + '_' + OptionSettings[2], f)
        except:
            pass
