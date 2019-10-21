import pygame

pygame.mixer.init()


class Music():
    """ 关于音乐播放 """

    def __init__(self):
        """ 加载音乐 """
        self.MusicList=[]
        self.MusicList.append('Music/9h00')
        self.MusicList.append('Music/Distress_Signa')
        self.MusicList.append('Music/Exchange')
        self.MusicList.append('Music/MN84_Theme')
        self.MusicList.append('Music/Shoulder_of_Orion')
        self.MusicList.append('Music/Sung-Thunder_Love')
        self.MusicList.append('Music/SYNTHWAVE_DEMO_02')
        self.MusicList.append('Music/Spoiler_Original_Mix')

    def PlayMusic(self, MusicNumber):
        """ 播放音乐 """
        self.MusicNumber = MusicNumber
        pygame.mixer.music.load(self.MusicList[self.MusicNumber] + '.mp3')
        pygame.mixer.music.play(loops=-1)
