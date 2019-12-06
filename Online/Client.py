import pygame
import sys
import socket
import threading
import re

sys.path.append('..')


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'pictures/AttachAircraft.png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 200

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.centery -= 1
        if keys[pygame.K_s]:
            self.rect.centery += 1
        if keys[pygame.K_a]:
            self.rect.centerx -= 1
        if keys[pygame.K_d]:
            self.rect.centerx += 1


class OtherShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(OtherShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'pictures/AttachAircraft.png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()

    def draw(self, PositionStr):
        try:
            self.rect.centerx = int(PositionStr.split(' ')[0])
            self.rect.centery = int(PositionStr.split(' ')[1])
            self.screen.blit(self.image, self.rect)
        except ValueError:
            # self.rect.centerx = int(re.sub(r'\D','',PositionStr.split(' ')[0]))
            # self.rect.centery = int(re.sub(r'\D','',PositionStr.split(' ')[1]))
            # self.screen.blit(self.image, self.rect)
            pass  #若改用上面三行，会存在客户端显示多余飞船的bug。若用pass,会出现飞船闪烁的bug
        except:
            print('>> Unexpected Error!')


def run_game():
    FpsClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    ShipGroup = pygame.sprite.Group()
    ShipGroup.add(Ship(screen))
    OtherShipGroup = pygame.sprite.Group()
    OtherShipGroup.add(OtherShip(screen))

    while 1:
        FpsClock.tick(80)
        screen.fill((5, 70, 160))

        for i in ShipGroup:
            i.draw()
            i.move()
            message = (MyName, str(i.rect.centerx), str(i.rect.centery))
            message = ' '.join(message)
            # print(message)
        s.sendall(bytes(message, encoding='utf8'))

        global PositionDict
        for i in OtherShipGroup:
            for num in range(4):  #设置为最多4人联机，可以任意增加
                try:
                    i.draw(PositionDict[AllName[num]])
                except:
                    break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


def read_from_server(s, MyName):
    global AllName
    AllName = []
    global PositionStr
    global PositionDict
    PositionDict = {}
    while True:
        content = str(s.recv(2048), encoding='utf8')
        Name = content.split(' ')[0]
        # print(Name)
        # print(PositionDict)
        # print(AllName)
        if MyName != Name:
            if Name not in AllName:
                AllName.append(Name)
            PositionStr = content.split(' ')[1] + ' ' + content.split(' ')[2]
            PositionDict[Name] = PositionStr
            # print(content)
            # print(PositionDict)


HOST = '172.22.12.150'
PORT = 30000
# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect((HOST, PORT))

PositionStr = '-100 -100'

# 设置名称
MyName = input('Please input your Name: ')
print("Hello, %s!" % MyName)
# 客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_from_server, args=(s, MyName)).start()
threading.Thread(target=run_game).start()