import pygame
import sys
import os
import random

sys.path.append('Enemy')
sys.path.append('Weapon')
sys.path.append('ScoreBoard')
sys.path.append('Music')

from Settings import *
from GameFunctions import *

from Aircraft import *
from Bullet import *
from Laser import *
from Shield import *
from OmegaLaser import *
from AddFire import *
from BulletSupport import *
from Missile import *
from Invincible import *
from AttachAircraft import *
from SpeedUp import *

from TimeBar import *

from EnemyShip import *
from EnemyBullet import *

from Stars import *

from ScoreBoard import *

from Buttons import *

from GreetScreen import *

from Help import *

from Music import *


def RunGame():
    """ 屏幕参数 """
    width, height = Settings().MainScreenWidth, Settings().MainScreenHeight
    BackgroundColor = Settings().MainScreenBackground
    """ 帧数函数 """
    FpsClock = pygame.time.Clock()
    """ 屏幕设置 """
    MainScreen = Settings().SetMainScreen()
    """ 设置Group """
    StartGameButtonGroup = pygame.sprite.Group()
    OptionButtonGroup = pygame.sprite.Group()
    HelpButtonGroup = pygame.sprite.Group()
    QuitGameButtonGroup = pygame.sprite.Group()
    PauseBackgroundGroup = pygame.sprite.Group()
    PauseResumeButtonGroup = pygame.sprite.Group()
    PauseOptionButtonGroup = pygame.sprite.Group()
    PauseGoMenuButtonGroup = pygame.sprite.Group()
    PauseQuitButtonGroup = pygame.sprite.Group()
    OptionBackgroundGroup = pygame.sprite.Group()
    OptionChangeMusicButtonGroup = pygame.sprite.Group()
    OptionChangeAircraftButtonGroup = pygame.sprite.Group()
    OptionChangeModeButtonGroup = pygame.sprite.Group()
    OptionChangeScreenSizeButtonGroup = pygame.sprite.Group()
    ShowMusicAlbumGroup = pygame.sprite.Group()
    """ Group添加Sprite """
    StartGameButtonGroup.add(StartGameButton(width, height))
    OptionButtonGroup.add(OptionButton(width, height))
    HelpButtonGroup.add(HelpButton(width, height))
    QuitGameButtonGroup.add(QuitGameButton(width, height))
    PauseBackgroundGroup.add(PauseBackground(height))
    PauseResumeButtonGroup.add(PauseResumeButton(height))
    PauseOptionButtonGroup.add(PauseOptionButton(height))
    PauseGoMenuButtonGroup.add(PauseGoMenuButton(height))
    PauseQuitButtonGroup.add(PauseQuitButton(height))
    OptionBackgroundGroup.add(OptionBackground(width, height))
    OptionChangeMusicButtonGroup.add(OptionChangeMusicButton(width, height))
    OptionChangeAircraftButtonGroup.add(
        OptionChangeAirCraftButton(width, height))
    OptionChangeModeButtonGroup.add(OptionChangeModeButton(width, height))
    OptionChangeScreenSizeButtonGroup.add(
        OptionChangeScreenSizeButton(width, height))
    ShowMusicAlbumGroup.add(ShowMusicAlbum(width, height))
    """ 暂停按钮结果 """
    PauseButtonResult = 'None'
    """ 播放默认音乐 """
    Music().PlayMusic(4)
    """ 加载飞船选择 """
    AircraftChoose = Settings().LoadAircraft()
    """ 是否重新开始 """
    ifagain = 0

    while 1:
        """ 火箭位置 """
        AircraftPosition = [0, 0]
        """ 外星人初始位置 """
        EnemyShipStartPositionList = [[0, 0], [width, 0], [0, height],
                                      [width, height]]
        """ 设置Group """
        AircraftGroup = pygame.sprite.Group()
        AircraftGroup.add(Aircraft(MainScreen, [width / 2, height / 2]))
        BulletGroup = pygame.sprite.Group()
        LaserGroup = pygame.sprite.Group()
        ShieldGroup = pygame.sprite.Group()
        AddFireGroup = pygame.sprite.Group()
        SpeedUpGroup = pygame.sprite.Group()
        InvincibleGroup = pygame.sprite.Group()
        if AircraftChoose == 0:
            AttachAircraftGroup = pygame.sprite.Group()
            AttachAircraftGroup.add(
                AttachAircraft(MainScreen, [width / 2, height / 2 - 100]))
        elif AircraftChoose == 2:
            BulletSupportGroup = pygame.sprite.Group()
        elif AircraftChoose == 3:
            MissileGroup = pygame.sprite.Group()
            MissileRangeGroup = pygame.sprite.Group()
        elif AircraftChoose == 4:
            OmegaLaserGroup = pygame.sprite.Group()

        EnemyShipGroup = pygame.sprite.Group()
        for position in EnemyShipStartPositionList:
            EnemyShipGroup.add(EnemyShip(MainScreen, position))
        EnemyBulletGroup = pygame.sprite.Group()
        EnemyBossShipGroup = pygame.sprite.Group()

        StarsGroup = pygame.sprite.Group()
        for i in range(50):
            StarsGroup.add(Stars(MainScreen, width, height))
        """ 子弹射击参数 """
        BulletFireFrequency = 0
        BulletFire = 0
        """ 激光射击参数 """
        LaserFireFrequency = 0
        LaserFire = 0
        """ 护盾启动参数 """
        ShieldGenerateFrequency = 0
        ShieldGenerate = 0
        """ 加速启动参数 """
        SpeedUpGenerateFrequency = 0
        SpeedUpGenerate = 0
        if AircraftChoose == 0:
            """ 跟随飞船射击参数 """
            AttachAircraftFireFrequency = 0
            """ 跟随飞船生命恢复参数 """
            AttachAircraftHealthFrequency = 0
        elif AircraftChoose == 1:
            """ 无敌状态 """
            InvincibleGenerateFrequency = 0
            InvincibleGenerate = 0
        elif AircraftChoose == 2:
            """ 底部火力支援启动参数 """
            BulletSupportFireFrequency = 0
            BulletSupportFire = 0
        elif AircraftChoose == 3:
            """ 导弹射击参数 """
            MissileFireFrequency = 0
            MissileFire = 0
            MissileRangeExistTime = 0
        elif AircraftChoose == 4:
            """ 追踪激光射击参数 """
            OmegaLaserFireFrequency = 0
            OmegaLaserFire = 0
        """ 辅助发射器启动参数 """
        AddFireGenerateFrequency = 0
        AddFireGenerate = 0
        """ 外星人子弹射击参数 """
        EnemyBulletFireFrequency = 0
        EnemyBulletFire = 0
        """ 外星人Boss子弹射击参数 """
        EnemyBossBulletFireFrequency = 0
        EnemyBossBulletFire = 0
        """ 按钮选择参数 """
        ButtonChooseFrequency = 0
        ButtonChoose = 0
        PauseButtonChooseFrequency = 0
        PauseButtonChoose = 0
        OptionButtonChooseFrequency = 0
        OptionButtonChoose = 0
        MusicAlterFrequency = 0
        MusicAlter = 0
        AircraftAlterFrequency = 0
        AircraftAlter = 0
        """ 计分 """
        Score = 0
        """ 是否暂停 """
        PauseStatus = 0
        """ 按钮选择 """
        ChooseButton = 0
        PauseChooseButton = 0
        OptionChooseButton = 0
        MusicChoose = 0
        """ 按钮选择结果 """
        ButtonResult = 'None'
        OptionButtonResult = 'None'
        """ 显示帮助界面 """
        DrawHelp = 0
        """ 显示设置界面 """
        GoToOption = 0
        """ 显示音乐封面 """
        DrawAlbum = 0
        """ 显示选择火箭 """
        DrawAircraft = 0
        """ 启动联机模式 """
        LaunchOnline = 0
        """ 显示屏幕尺寸选择 """
        DrawSize = 0
        CenterList = [[150, 0], [400, 0], [650, 0]]
        """ 开始界面 """
        while CheckActions().CheckQuitGame() and ifagain == 0:
            """ 背景填充 """
            MainScreen.fill(BackgroundColor)
            """ 设置帧数 """
            FpsClock.tick(80)
            """ 显示标题 """
            GreetScreen(width).DrawTitle(MainScreen)
            """ 按钮选择更新 """
            if ButtonChooseFrequency >= 5 and not DrawHelp and not GoToOption:
                ButtonChoose, ChooseButton = CheckActions().CheckAlterChoose(
                    ChooseButton, 1, 4, 0)
            if ButtonChoose:
                ButtonChooseFrequency = 0
                ButtonChoose = 0
            """ 显示按钮 """
            for button in StartGameButtonGroup:
                button.draw(MainScreen)
                button.TempChoose(ChooseButton)
            for button in OptionButtonGroup:
                button.draw(MainScreen)
                button.TempChoose(ChooseButton)
            for button in HelpButtonGroup:
                button.draw(MainScreen)
                button.TempChoose(ChooseButton)
            for button in QuitGameButtonGroup:
                button.draw(MainScreen)
                button.TempChoose(ChooseButton)
            """ 选择按钮 """
            ButtonResult = CheckActions().CheckConfirmChoose(
                ChooseButton,
                ('GoToMainGame', 'GoToOption', 'GoToHelp', 'Exit'))
            """ 按钮选择结果生效 """
            if ButtonResult == 'GoToMainGame':
                break
            elif ButtonResult == 'GoToOption':
                GoToOption = 1
            elif ButtonResult == 'GoToHelp':
                DrawHelp = 1
            elif ButtonResult == 'Exit':
                sys.exit(0)
            """ 显示帮助界面 """
            if DrawHelp:
                HelpScreen(width, height).draw(MainScreen)
                DrawHelp = CheckActions().CheckGoBack(DrawHelp)
            """ 设置按钮初始化 """
            if OptionChooseButton != 0:
                OptionChooseButton = 0
            """ 显示设置界面 """
            while GoToOption:
                """ 按钮选择更新 """
                if OptionButtonChooseFrequency >= 30:
                    OptionButtonChoose, OptionChooseButton = CheckActions(
                    ).CheckAlterChoose(OptionChooseButton, 1, 4, 0)
                if OptionButtonChoose:
                    OptionButtonChooseFrequency = 0
                    OptionButtonChoose = 0
                """ 绘制按钮 """
                for background in OptionBackgroundGroup:
                    background.draw(MainScreen)
                for button in OptionChangeMusicButtonGroup:
                    button.draw(MainScreen)
                    button.TempChoose(OptionChooseButton)
                for button in OptionChangeAircraftButtonGroup:
                    button.draw(MainScreen)
                    button.TempChoose(OptionChooseButton)
                for button in OptionChangeModeButtonGroup:
                    button.draw(MainScreen)
                    button.TempChoose(OptionChooseButton)
                for button in OptionChangeScreenSizeButtonGroup:
                    button.draw(MainScreen)
                    button.TempChoose(OptionChooseButton)
                """ 选择按钮 """
                OptionButtonResult = CheckActions().CheckConfirmChoose(
                    OptionChooseButton, ('ChangeMusic', 'ChangeAirCraft',
                                         'ChangeMode', 'ChangeScreenSize'))
                """ 按钮选择结果生效 """
                if OptionButtonResult == 'ChangeMusic':
                    DrawAlbum = 1
                elif OptionButtonResult == 'ChangeAirCraft':
                    DrawAircraft = 1
                elif OptionButtonResult == 'ChangeMode':
                    LaunchOnline = 1
                elif OptionButtonResult == 'ChangeScreenSize':
                    DrawSize = 1
                """ 显示音乐封面 """
                while DrawAlbum:
                    """ 音乐选择更新 """
                    if MusicAlterFrequency >= 200:
                        MusicAlter, MusicChoose = CheckActions(
                        ).CheckAlterChoose(MusicChoose, 0, 7, 1)
                    if MusicAlter:
                        MusicAlterFrequency = 0
                        MusicAlter = 0
                    """ 绘制专辑 """
                    for album in ShowMusicAlbumGroup:
                        album.draw(MainScreen, MusicChoose)
                    """ 检测返回设置主界面 """
                    DrawAlbum = CheckActions().CheckGoBack(DrawAlbum)
                    """ 音乐选择频率更新 """
                    MusicAlterFrequency += 1
                    """ 检测退出 """
                    CheckActions().CheckQuitGame()
                    """ 刷新屏幕 """
                    pygame.display.update()
                    """ 确认音乐选择 """
                    FinalMusic = CheckActions().CheckConfirmMusicAircraft(
                        MusicChoose)
                    if FinalMusic != None:
                        Music().PlayMusic(FinalMusic)
                """ 显示火箭 """
                while DrawAircraft:
                    """ 火箭选择更新 """
                    if AircraftAlterFrequency >= 200:
                        AircraftAlter, AircraftChoose = CheckActions(
                        ).CheckAlterChoose(AircraftChoose, 0, 4, 1)
                    if AircraftAlter:
                        AircraftAlterFrequency = 0
                        AircraftAlter = 0
                    """ 绘制图片 """
                    for ship in AircraftGroup:
                        ship.OptionDraw(width, height, AircraftChoose)
                    """ 检测返回设置主界面 """
                    DrawAircraft = CheckActions().CheckGoBack(DrawAircraft)
                    """ 火箭选择频率更新 """
                    AircraftAlterFrequency += 1
                    """ 检测退出 """
                    CheckActions().CheckQuitGame()
                    """ 刷新屏幕 """
                    pygame.display.update()
                    """ 确认火箭选择 """
                    FinalAircraft = CheckActions().CheckConfirmMusicAircraft(
                        AircraftChoose)
                    if FinalAircraft != None:
                        Settings().SetAircraftChoose(FinalAircraft)  #重新启动游戏生效
                """ 启动联机模式 """
                if LaunchOnline:
                    os.system('python Online/GetName.py')
                """ 显示屏幕尺寸选择 """
                while DrawSize:
                    """ 鼠标点击读取按钮位置 """
                    for ButtonRect in ScreenSize().AllRect:
                        if CheckActions().CheckMouse(ButtonRect) != None:
                            if CenterList[0][1] == 0 and \
                                CheckActions().CheckMouse(ButtonRect)[1]!=100 and \
                                CheckActions().CheckMouse(ButtonRect)[0] == 150:
                                CenterList[0][1] = CheckActions().CheckMouse(
                                    ButtonRect)[1]
                            elif CenterList[1][1] == 0 and \
                                CheckActions().CheckMouse(ButtonRect)[1] != 100 and \
                                    CheckActions().CheckMouse(ButtonRect)[0] == 400:
                                CenterList[1][1] = CheckActions().CheckMouse(
                                    ButtonRect)[1]
                            elif CenterList[2][1] == 0 and \
                                CheckActions().CheckMouse(ButtonRect)[1] != 100 and \
                                    CheckActions().CheckMouse(ButtonRect)[0] == 650:
                                CenterList[2][1] = CheckActions().CheckMouse(
                                    ButtonRect)[1]
                    """ 绘制选择按钮框 """
                    for i in range(0, 3):
                        if CenterList[i][1] != 0:
                            ScreenSize().TempChoose(MainScreen, CenterList[i])
                    """ 绘制图片 """
                    ScreenSize().draw(MainScreen, width, height)
                    """ 检测返回设置主界面 """
                    DrawSize = CheckActions().CheckGoBack(DrawSize)
                    """ 检测退出 """
                    CheckActions().CheckQuitGame()
                    """ 刷新屏幕 """
                    pygame.display.update()
                    """ 更新屏幕尺寸文件 """
                    Settings().OptionSetScreenSize(CenterList)
                """ 按钮选择频率更新 """
                OptionButtonChooseFrequency += 1
                """ 检测退出设置 """
                GoToOption = CheckActions().CheckGoBack(GoToOption)
                """ 检测退出 """
                CheckActions().CheckQuitGame()
                """ 刷新屏幕 """
                pygame.display.update()
            """ 按钮选择频率更新 """
            ButtonChooseFrequency += 1
            """ 屏幕刷新 """
            pygame.display.flip()
            """ 更新暂停按钮结果 """
            PauseButtonResult = 'None'
        """ 游戏主循环 """
        while CheckActions().CheckQuitGame(
        ) and PauseButtonResult != 'BackToMenu':
            """ 无尽模式添加飞船 """
            if len(EnemyShipGroup) <= 7 + Score / 10:
                if random.random() < 0.5:
                    EnemyShipGroup.add(
                        EnemyShip(MainScreen, [width * random.random(), 0]))
                elif random.random() < 0.7:
                    EnemyShipGroup.add(
                        EnemyShip(MainScreen,
                                  [width * random.random(), height]))
                elif random.random() < 0.9:
                    EnemyShipGroup.add(
                        EnemyShip(MainScreen, [0, height * random.random()]))
                else:
                    EnemyShipGroup.add(
                        EnemyShip(MainScreen,
                                  [width, height * random.random()]))
            if Score >= 50 and len(EnemyBossShipGroup) != 1:
                if Score % 50 == 0 or Score % 50 == 1 or Score % 50 == 2:
                    EnemyBossShipGroup.add(
                        EnemyBossShip(MainScreen, [width / 2, 0]))
            """ 背景填充 """
            MainScreen.fill(BackgroundColor)
            """ 设置最大帧数 """
            FpsClock.tick(80)
            """ 星空 """
            for star in StarsGroup:
                star.draw()
                star.move()
                """ 移除屏幕外星星 """
                if star.rect.top >= height:
                    StarsGroup.remove(star)
                    StarsGroup.add(Stars(MainScreen, width, height, 1))
            """ 外星人 """
            OtherEnemyShipGroup = EnemyShipGroup.copy()  #防止外星人重叠
            for ship in EnemyShipGroup:
                ship.draw()
                ship.drawHealth()
                """ 防止外星人重叠 """
                OtherEnemyShipGroup.remove(ship)
                if not pygame.sprite.spritecollide(ship, OtherEnemyShipGroup,
                                                   False):
                    ship.move(width, height, AircraftPosition)
                """ 检测与子弹碰撞 """
                if pygame.sprite.spritecollide(ship, BulletGroup, True):
                    ship.hp -= 1
                    ship.DrawGetFire([ship.rect.centerx, ship.rect.centery])
                if AircraftChoose == 2:
                    if pygame.sprite.spritecollide(ship, BulletSupportGroup,
                                                   False):
                        ship.hp -= 1
                        ship.DrawGetFire(
                            [ship.rect.centerx, ship.rect.centery])
                """ 检测与激光碰撞 """
                if pygame.sprite.spritecollide(ship, LaserGroup, False):
                    ship.hp -= 1
                    ship.DrawGetFire([ship.rect.centerx, ship.rect.centery])
                """ 检测与护盾碰撞 """
                if pygame.sprite.spritecollide(ship, ShieldGroup, True):
                    ship.hp -= 4
                    ship.DrawGetFire([ship.rect.centerx, ship.rect.centery])
                """ 检测与无敌碰撞 """
                if AircraftChoose == 1:
                    if pygame.sprite.spritecollide(ship, InvincibleGroup,
                                                   False):
                        ship.hp -= 2
                        ship.DrawGetFire(
                            [ship.rect.centerx, ship.rect.centery])
                """ 检测与导弹碰撞 """
                if AircraftChoose == 3:
                    if pygame.sprite.spritecollide(ship, MissileGroup, False):
                        for missile in MissileGroup:
                            MissileRangeGroup.add(
                                MissileRange(MainScreen, [
                                    missile.rect.centerx, missile.rect.centery
                                ]))
                            MissileGroup.remove(missile)
                    """ 检查与导弹溅射范围碰撞 """
                    if pygame.sprite.spritecollide(ship, MissileRangeGroup,
                                                   False):
                        ship.hp -= 1
                """ 检测与追踪激光碰撞 """
                if AircraftChoose == 4:
                    if pygame.sprite.spritecollide(ship, OmegaLaserGroup,
                                                   True):
                        ship.hp -= 1
                        ship.DrawGetFire(
                            [ship.rect.centerx, ship.rect.centery])
                """ 计算外星人死亡 """
                if ship.hp <= 0:
                    """ 计分 """
                    if ship.notShoot:
                        Score += 1
                    elif not ship.notShoot:
                        Score += 2
                    EnemyShipGroup.remove(ship)
                """ 外星人发射子弹 """
                if not ship.notShoot:
                    if EnemyBulletFireFrequency >= 200:
                        for ship in EnemyShipGroup:
                            if not ship.notShoot:
                                EnemyBulletGroup.add(
                                    EnemyBullet(
                                        MainScreen,
                                        [ship.rect.centerx, ship.rect.bottom]))

                        EnemyBulletFireFrequency = 0
            """ 外星人Boss """
            for ship in EnemyBossShipGroup:
                ship.move(width, height, AircraftPosition)
                ship.drawHealth()
                ship.draw()
                """ 检测与子弹碰撞 """
                if pygame.sprite.spritecollide(ship, BulletGroup, True):
                    ship.hp -= 0.5
                if AircraftChoose == 2:
                    if pygame.sprite.spritecollide(ship, BulletSupportGroup,
                                                   True):
                        ship.hp -= 0.1
                """ 检测与护盾碰撞 """
                if pygame.sprite.spritecollide(ship, ShieldGroup, True):
                    ship.hp -= 1
                """ 检测与无敌碰撞 """
                if AircraftChoose == 1:
                    if pygame.sprite.spritecollide(ship, InvincibleGroup,
                                                   True):
                        ship.hp -= 2
                """ 检测与导弹碰撞 """
                if AircraftChoose == 3:
                    if pygame.sprite.spritecollide(ship, MissileGroup, False):
                        for missile in MissileGroup:
                            MissileRangeGroup.add(
                                MissileRange(MainScreen, [
                                    missile.rect.centerx, missile.rect.centery
                                ]))
                            MissileGroup.remove(missile)
                        ship.hp -= 5
                """ 检测与追踪激光碰撞 """
                if AircraftChoose == 4:
                    if pygame.sprite.spritecollide(ship, OmegaLaserGroup,
                                                   True):
                        ship.hp -= 1
                """ 计算外星人死亡 """
                if ship.hp <= 0:
                    """ 计分 """
                    Score += 10
                    EnemyBossShipGroup.remove(ship)
                """ 外星人Boss发射子弹 """
                if EnemyBossBulletFireFrequency >= 200:
                    for i in range(-50, 51, 50):
                        EnemyBulletGroup.add(
                            EnemyBullet(
                                MainScreen,
                                [ship.rect.centerx + i, ship.rect.bottom]))
                    EnemyBossBulletFireFrequency = 0
            """ 子弹 """
            for bullet in BulletGroup:
                bullet.draw()
                bullet.move()
                """ 移除屏幕外子弹 """
                if bullet.rect.bottom <= 0:
                    BulletGroup.remove(bullet)
            """ 子弹射击频率更新 """
            BulletFireFrequency += 1
            """ 激光 """
            for laser in LaserGroup:
                laser.draw()
                laser.move()
                """ 移除屏幕外激光 """
                if laser.rect.bottom <= 0:
                    LaserGroup.remove(laser)
            """ 激光射击频率更新 """
            LaserFireFrequency += 1
            """ 激光缓冲进度 """
            TimeBar(MainScreen, height, 100, LaserFireFrequency, 150).draw()
            TimeBarPictures(MainScreen, height, 95).DrawTimeBarLaser()
            """ 护盾 """
            for shield in ShieldGroup:
                shield.draw()
                shield.move(AircraftPosition, len(SpeedUpGroup))
            """ 护盾启动频率更新 """
            ShieldGenerateFrequency += 1
            """ 护盾缓冲进度 """
            TimeBar(MainScreen, height, 80, ShieldGenerateFrequency,
                    200).draw()
            TimeBarPictures(MainScreen, height, 75).DrawTimeBarShield()
            """ 辅助发射器 """
            for addfire in AddFireGroup:
                addfire.draw()
                addfire.move(AircraftPosition, len(SpeedUpGroup),
                             len(InvincibleGroup))
                if AddFireGenerateFrequency >= 100:
                    AddFireGroup.remove(addfire)
            """ 辅助发射器启动频率更新 """
            AddFireGenerateFrequency += 1
            """ 辅助发射器缓冲进度 """
            TimeBar(MainScreen, height, 60, AddFireGenerateFrequency,
                    300).draw()
            TimeBarPictures(MainScreen, height, 55).DrawTimeBarAddFire()
            """ 加速 """
            for speedup in SpeedUpGroup:
                speedup.draw()
                if SpeedUpGenerateFrequency >= 100:
                    SpeedUpGroup.remove(speedup)
            """ 加速启动频率更新 """
            SpeedUpGenerateFrequency += 1
            """ 加速缓冲进度 """
            TimeBar(MainScreen, height, 40, SpeedUpGenerateFrequency,
                    300).draw()
            TimeBarPictures(MainScreen, height, 35).DrawTimeBarSpeedUp()
            """ 跟随飞船 """
            if AircraftChoose == 0:
                for ship in AttachAircraftGroup:
                    ship.draw()
                    ship.DrawHealth()
                    if ship.hp > 0:
                        ship.move(height, EnemyShipGroup)
                        """ 检测损坏情况 """
                        if pygame.sprite.spritecollide(ship, EnemyBulletGroup,
                                                       True):
                            ship.hp -= 1
                        if pygame.sprite.spritecollide(ship, BulletGroup,
                                                       True):
                            ship.hp -= 1
                        if pygame.sprite.spritecollide(ship, LaserGroup,
                                                       False):
                            ship.hp -= 1
                            if pygame.sprite.spritecollide(
                                    ship, InvincibleGroup, False):
                                ship.hp -= 1
                        if AircraftChoose == 2:
                            if pygame.sprite.spritecollide(
                                    ship, BulletSupportGroup, False):
                                ship.hp -= 1
                        if AircraftChoose == 3:
                            if pygame.sprite.spritecollide(
                                    ship, MissileGroup, False):
                                for missile in MissileGroup:
                                    MissileRangeGroup.add(
                                        MissileRange(MainScreen, [
                                            missile.rect.centerx,
                                            missile.rect.centery
                                        ]))
                                    MissileGroup.remove(missile)
                            if pygame.sprite.spritecollide(
                                    ship, MissileRangeGroup, False):
                                ship.hp -= 1
                        if AircraftChoose == 4:
                            if pygame.sprite.spritecollide(
                                    ship, OmegaLaserGroup, True):
                                ship.hp -= 1
                        """ 跟随飞船发射子弹 """
                        if AttachAircraftFireFrequency >= 30:
                            for i in range(-1, 2, 2):
                                BulletGroup.add(
                                    Bullet(MainScreen, [
                                        ship.rect.centerx + 20 * i,
                                        ship.rect.top
                                    ]))
                            AttachAircraftFireFrequency = 0
                    else:
                        """ 跟随飞船生命恢复频率更新 """
                        AttachAircraftHealthFrequency += 1
                        """ 检测复活 """
                        if AttachAircraftHealthFrequency >= 1000:
                            ship.hp = 5
                            AttachAircraftHealthFrequency = 0
                """ 跟随飞船射击频率更新 """
                AttachAircraftFireFrequency += 1
                """ 跟随飞船生命恢复进度 """
                TimeBar(MainScreen, height, 20, AttachAircraftHealthFrequency,
                        1000).draw()
                TimeBarPictures(MainScreen, height,
                                15).DrawTimeBarAttachAircraft()
            """ 无敌 """
            if AircraftChoose == 1:
                for invincible in InvincibleGroup:
                    invincible.draw()
                    invincible.move(AircraftPosition, len(SpeedUpGroup))
                    if InvincibleGenerateFrequency >= 80:
                        InvincibleGroup.remove(invincible)
                """ 无敌频率更新 """
                InvincibleGenerateFrequency += 1
                """ 无敌缓冲进度 """
                TimeBar(MainScreen, height, 20, InvincibleGenerateFrequency,
                        300).draw()
                TimeBarPictures(MainScreen, height, 15).DrawTimeBarInvincible()
            """ 底部火力支援 """
            if AircraftChoose == 2:
                for bullet in BulletSupportGroup:
                    bullet.draw()
                    bullet.move()
                    if bullet.rect.bottom <= 0:
                        BulletSupportGroup.remove(bullet)
                """ 底部火力支援启动频率更新 """
                BulletSupportFireFrequency += 1
                """ 底部火力支援缓冲进度 """
                TimeBar(MainScreen, height, 20, BulletSupportFireFrequency,
                        300).draw()
                TimeBarPictures(MainScreen, height,
                                15).DrawTimeBarBulletSupport()
            """ 导弹 """
            if AircraftChoose == 3:
                for missile in MissileGroup:
                    missile.draw()
                    missile.move()
                    if missile.rect.bottom <= 0:
                        MissileGroup.remove(missile)
                for missilerange in MissileRangeGroup:
                    missilerange.draw()
                    if MissileRangeExistTime >= 100:
                        MissileRangeGroup.remove(missilerange)
                        MissileRangeExistTime = 0
                """ 导弹射击频率更新 """
                MissileFireFrequency += 1
                """ 导弹溅射范围存在时间更新 """
                if len(MissileRangeGroup) != 0:
                    MissileRangeExistTime += 1
                """ 导弹缓冲进度 """
                TimeBar(MainScreen, height, 20, MissileFireFrequency,
                        250).draw()
                TimeBarPictures(MainScreen, height, 15).DrawTimeBarMissile()
            """ 追踪激光 """
            if AircraftChoose == 4:
                OtherOmegaLaserGroup = OmegaLaserGroup.copy()
                for laser in OmegaLaserGroup:
                    laser.draw()
                    """ 防止追踪激光重叠 """
                    OtherOmegaLaserGroup.remove(laser)
                    if not pygame.sprite.spritecollide(
                            laser, OtherOmegaLaserGroup, False):
                        laser.move(EnemyShipGroup)
                """ 追踪激光射击频率更新 """
                OmegaLaserFireFrequency += 1
                """ 追踪激光缓冲进度 """
                TimeBar(MainScreen, height, 20, OmegaLaserFireFrequency,
                        500).draw()
                TimeBarPictures(MainScreen, height, 15).DrawTimeBarOmegaLaser()
            """ 飞船 """
            for ship in AircraftGroup:
                ship.draw()
                ship.move(width, height)
                AircraftPosition[0] = ship.rect.centerx
                AircraftPosition[1] = ship.rect.centery
                if pygame.sprite.spritecollide(ship, EnemyShipGroup, True) or \
                    pygame.sprite.spritecollide(ship, EnemyBulletGroup, True) or \
                        pygame.sprite.spritecollide(ship,EnemyBossShipGroup,True):
                    AircraftGroup.remove(ship)
                """ 检测发射子弹 """
                if BulletFireFrequency >= 15:
                    BulletFire = CheckActions().CheckFire(
                        BulletGroup, [
                            Bullet(MainScreen,
                                   [ship.rect.centerx, ship.rect.top]),
                            Bullet(MainScreen,
                                   [ship.rect.centerx + 40, ship.rect.top]),
                            Bullet(MainScreen,
                                   [ship.rect.centerx - 40, ship.rect.top])
                        ],
                        pygame.K_j,
                        addfireready=1,
                        addfire=len(AddFireGroup))
                if BulletFire:
                    BulletFireFrequency = 0
                    BulletFire = 0
                """ 检测发射激光 """
                if LaserFireFrequency >= 150:
                    LaserFire = CheckActions().CheckFire(
                        LaserGroup, [
                            Laser(MainScreen,
                                  [ship.rect.centerx, ship.rect.top]),
                            Laser(MainScreen,
                                  [ship.rect.centerx + 40, ship.rect.top]),
                            Laser(MainScreen,
                                  [ship.rect.centerx - 40, ship.rect.top])
                        ],
                        pygame.K_k,
                        addfireready=1,
                        addfire=len(AddFireGroup))
                if LaserFire:
                    LaserFireFrequency = 0
                    LaserFire = 0
                """ 检测启动加速 """
                if SpeedUpGenerateFrequency >= 300:
                    SpeedUpGenerate = CheckActions().CheckFire(
                        SpeedUpGroup,
                        SpeedUp(MainScreen, [width - 150, height]), pygame.K_o)
                if SpeedUpGenerate:
                    SpeedUpGenerateFrequency = 0
                    SpeedUpGenerate = 0
                ship.speed = [
                    2 * (len(SpeedUpGroup) + 1), 2 * (len(SpeedUpGroup) + 1)
                ]
                """ 检测启动无敌 """
                if AircraftChoose == 1:
                    if InvincibleGenerateFrequency >= 300 and len(
                            ShieldGroup) == 0:
                        InvincibleGenerate = CheckActions().CheckFire(
                            InvincibleGroup,
                            Invincible(MainScreen,
                                       [ship.rect.centerx, ship.rect.centery]),
                            pygame.K_i)
                    if InvincibleGenerate:
                        InvincibleGenerateFrequency = 0
                        InvincibleGenerate = 0
                    ship.speed = [
                        2 * (len(InvincibleGroup) + 1) *
                        (len(SpeedUpGroup) + 1), 2 *
                        (len(InvincibleGroup) + 1) * (len(SpeedUpGroup) + 1)
                    ]
                """ 检测发射导弹 """
                if AircraftChoose == 3:
                    if MissileFireFrequency >= 250:
                        MissileFire = CheckActions().CheckFire(
                            MissileGroup, [
                                Missile(MainScreen,
                                        [ship.rect.centerx, ship.rect.top]),
                                Missile(
                                    MainScreen,
                                    [ship.rect.centerx + 40, ship.rect.top]),
                                Missile(
                                    MainScreen,
                                    [ship.rect.centerx - 40, ship.rect.top])
                            ],
                            pygame.K_i,
                            addfireready=1,
                            addfire=len(AddFireGroup))
                    if MissileFire:
                        MissileFireFrequency = 0
                        MissileFire = 0
                """ 检测发射追踪激光 """
                if AircraftChoose == 4:
                    if OmegaLaserFireFrequency >= 500:
                        for i in range(50):
                            OmegaLaserFire = CheckActions().CheckFire(
                                OmegaLaserGroup, [
                                    OmegaLaser(MainScreen, [
                                        ship.rect.centerx,
                                        ship.rect.top - 5 * i
                                    ]),
                                    OmegaLaser(MainScreen, [
                                        ship.rect.centerx + 40,
                                        ship.rect.top - 5 * i
                                    ]),
                                    OmegaLaser(MainScreen, [
                                        ship.rect.centerx - 40,
                                        ship.rect.top - 5 * i
                                    ])
                                ],
                                pygame.K_i,
                                addfireready=1,
                                addfire=len(AddFireGroup))
                    if OmegaLaserFire:
                        OmegaLaserFireFrequency = 0
                        OmegaLaserFire = 0
                """ 检测启动护盾 """
                if AircraftChoose == 1:
                    if ShieldGenerateFrequency >= 200 and len(
                            InvincibleGroup) == 0:
                        ShieldGenerate = CheckActions().CheckFire(
                            ShieldGroup,
                            Shield(MainScreen,
                                   [ship.rect.centerx, ship.rect.centery]),
                            pygame.K_u)
                else:
                    if ShieldGenerateFrequency >= 200:
                        ShieldGenerate = CheckActions().CheckFire(
                            ShieldGroup,
                            Shield(MainScreen,
                                   [ship.rect.centerx, ship.rect.centery]),
                            pygame.K_u)
                if ShieldGenerate:
                    ShieldGenerateFrequency = 0
                    ShieldGenerate = 0
                """ 检测启动辅助发射器 """
                if AddFireGenerateFrequency >= 300:
                    AddFireGenerate = CheckActions().CheckFire(
                        AddFireGroup,
                        AddFire(MainScreen,
                                [ship.rect.centerx, ship.rect.centery]),
                        pygame.K_l)
                if AddFireGenerate:
                    AddFireGenerateFrequency = 0
                    AddFireGenerate = 0
            """ 检测底部火力支援 """
            if AircraftChoose == 2:
                if BulletSupportFireFrequency >= 300:
                    BulletSupportFire = CheckActions().CheckFire(
                        BulletSupportGroup, [
                            BulletSupport(MainScreen,
                                          [AircraftPosition[0] + i, height])
                            for i in range(-100 *
                                           (1 + len(AddFireGroup)), 100 *
                                           (1 + len(AddFireGroup)), 25)
                        ],
                        pygame.K_i,
                        addfireready=1,
                        addfire=1)
                if BulletSupportFire:
                    BulletSupportFireFrequency = 0
                    BulletSupportFire = 0
            """ 外星人子弹 """
            for bullet in EnemyBulletGroup:
                bullet.draw()
                bullet.move()
                """ 移除屏幕外子弹 """
                if bullet.rect.top >= height:
                    EnemyBulletGroup.remove(bullet)
                """ 检测与子弹碰撞 """
                if pygame.sprite.spritecollide(bullet, BulletGroup, True):
                    EnemyBulletGroup.remove(bullet)
                """ 检测与激光碰撞 """
                if pygame.sprite.spritecollide(bullet, LaserGroup, False):
                    EnemyBulletGroup.remove(bullet)
                """ 检测与护盾碰撞 """
                if pygame.sprite.spritecollide(bullet, ShieldGroup, True):
                    EnemyBulletGroup.remove(bullet)
                """ 检测与无敌碰撞 """
                if AircraftChoose == 1:
                    if pygame.sprite.spritecollide(bullet, InvincibleGroup,
                                                   False):
                        EnemyBulletGroup.remove(bullet)
            """ 外星人子弹射击频率更新 """
            EnemyBulletFireFrequency += 1
            """ 外星人Boss子弹射击频率更新 """
            EnemyBossBulletFireFrequency += 1
            """ 计分 """
            ScoreBoard(MainScreen, Score, width, height).UpdateScore(Score)
            ScoreBoard(MainScreen, Score, width, height).draw()
            """ 检测暂停 """
            PauseStatus = CheckActions().CheckPause(PauseStatus)
            """ 暂停 """
            while PauseStatus:
                """ 按钮选择更新 """
                if PauseButtonChooseFrequency >= 80:
                    PauseButtonChoose, PauseChooseButton = CheckActions(
                    ).CheckAlterChoose(PauseChooseButton, 1, 4, 0)
                if PauseButtonChoose:
                    PauseButtonChooseFrequency = 0
                    PauseButtonChoose = 0
                """ 绘制按钮 """
                for background in PauseBackgroundGroup:
                    background.draw(MainScreen)
                    background.MoveIn()
                for button in PauseResumeButtonGroup:
                    button.draw(MainScreen)
                    button.MoveIn()
                    button.TempChoose(PauseChooseButton)
                for button in PauseOptionButtonGroup:
                    button.draw(MainScreen)
                    button.MoveIn()
                    button.TempChoose(PauseChooseButton)
                for button in PauseGoMenuButtonGroup:
                    button.draw(MainScreen)
                    button.MoveIn()
                    button.TempChoose(PauseChooseButton)
                for button in PauseQuitButtonGroup:
                    button.draw(MainScreen)
                    button.MoveIn()
                    button.TempChoose(PauseChooseButton)
                """ 选择按钮 """
                PauseButtonResult = CheckActions().CheckConfirmChoose(
                    PauseChooseButton,
                    ('BackToMainGame', 'pass', 'BackToMenu', 'Exit'))
                """ 按钮选择结果生效 """
                if PauseButtonResult == 'BackToMainGame':
                    PauseStatus = 0
                    ifagain = 0
                    for background in PauseBackgroundGroup:
                        PauseBackgroundGroup.remove(background)
                        PauseBackgroundGroup.add(PauseBackground(height))
                    for button in PauseResumeButtonGroup:
                        PauseResumeButtonGroup.remove(button)
                        PauseResumeButtonGroup.add(PauseResumeButton(height))
                    for button in PauseOptionButtonGroup:
                        PauseOptionButtonGroup.remove(button)
                        PauseOptionButtonGroup.add(PauseOptionButton(height))
                    for button in PauseGoMenuButtonGroup:
                        PauseGoMenuButtonGroup.remove(button)
                        PauseGoMenuButtonGroup.add(PauseGoMenuButton(height))
                    for button in PauseQuitButtonGroup:
                        PauseQuitButtonGroup.remove(button)
                        PauseQuitButtonGroup.add(PauseQuitButton(height))
                elif PauseButtonResult == 'BackToMenu':
                    PauseStatus = 0
                    ifagain = 0
                    break
                elif PauseButtonResult == 'Exit':
                    sys.exit(0)
                """ 按钮选择频率更新 """
                PauseButtonChooseFrequency += 1
                """ 检测退出 """
                CheckActions().CheckQuitGame()
                """ 刷新屏幕 """
                pygame.display.flip()
            """ 屏幕刷新 """
            pygame.display.flip()
            """ 重新开始 """
            if len(AircraftGroup) == 0:
                while 1:
                    ifagain = CheckActions().CheckAgainChoose(
                        MainScreen, width, height, ifagain)
                    if ifagain == 1:
                        break
                if ifagain == 1:
                    ifagain = 2
                    break


if __name__ == '__main__':
    RunGame()
