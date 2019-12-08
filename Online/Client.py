import pygame
import socket
import threading
import sys
import time

sys.path.append('..')


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'pictures/AttachAircraft.png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()

    def draw(self, position):
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        self.screen.blit(self.image, self.rect)


class OtherShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(OtherShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'pictures/AttachAircraft.png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()

    def draw(self, position):
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        self.screen.blit(self.image, self.rect)


class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'pictures/EnemyShipClassic.png')
        self.rect = self.image.get_rect()

    def draw(self, position):
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        self.screen.blit(self.image, self.rect)


# class Bullet(pygame.sprite.Sprite):
#     def __init__(self,screen):
#         super(Bullet, self).__init__()
#         self.screen = screen
#         self.image = pygame.image.load(r'pictures/Bullet.png')
#         self.image = pygame.transform.smoothscale(self.image, (3, 10))
#         self.rect = self.image.get_rect()

#     def draw(self, position):
#         self.rect.centerx = position[0]
#         self.rect.centery = position[1]

#         self.screen.blit(self.image, self.rect)



def get_keys():
    keys = pygame.key.get_pressed()
    key_set = set()
    key_str = ''

    if keys[pygame.K_w]:
        key_set.add('w')
    if keys[pygame.K_a]:
        key_set.add('a')
    if keys[pygame.K_s]:
        key_set.add('s')
    if keys[pygame.K_d]:
        key_set.add('d')
    # if keys[pygame.K_j]:
    #     key_set.add('j')

    for key in key_set:
        key_str += key

    return key_str


def receive_from_server(my_name, s, HOST, PORT):
    global my_position
    global other_position
    global enemy_info
    # global bullet_info

    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode().split(' ')
            # print(data)
            if data[0] == my_name:  #仅支持2人联机
                my_position = [int(data[1]), int(data[2])]
                other_position = [int(data[4]), int(data[5])]
            elif data[3] == my_name:
                my_position = [int(data[4]), int(data[5])]
                other_position = [int(data[1]), int(data[2])]
            elif data[0] == 'enemy':
                enemy_info = [int(data[1]), int(data[2])]
                # print(enemy_info)
            # elif data[0] == 'bullet':
            #     bullet_info = [int(data[1]), int(data[2])]
            #     # print(bullet_info)
        except:
            pass


def run_game(my_name, s, HOST, PORT):
    global my_position
    global other_position
    global enemy_info
    # global bullet_info
    """ 窗口设置 """
    FpsClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    """ 建立Group """
    ShipGroup = pygame.sprite.Group()
    ShipGroup.add(Ship(screen))
    OtherShipGroup = pygame.sprite.Group()
    OtherShipGroup.add(OtherShip(screen))
    EnemyShipGroup = pygame.sprite.Group()
    EnemyShipGroup.add(EnemyShip(screen))
    # BulletGroup = pygame.sprite.Group()
    # BulletGroup.add(Bullet(screen))

    while 1:
        FpsClock.tick(80)
        screen.fill((5, 70, 160))

        for i in ShipGroup:
            try:
                i.draw(my_position)
            except:
                pass
            message = ' '.join((my_name, str(i.rect.centerx),
                                str(i.rect.centery), get_keys()))
            s.sendto(message.encode(), (HOST, PORT))

        for i in OtherShipGroup:
            try:
                i.draw(other_position)
            except:
                pass

        for i in EnemyShipGroup:
            try:
                i.draw(enemy_info)
            except:
                pass
        
        # for i in BulletGroup:
        #     try:
        #         i.draw(bullet_info)
        #     except:
        #         pass

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


def launch_client(my_name):
    # my_name = input('input your name: ')
    # print(my_name)

    HOST = '172.22.12.150'
    PORT = 30000
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_position = []
    other_position = []
    enemy_info = []
    # bullet_info = []

    threading.Thread(target=run_game, args=(my_name, s, HOST, PORT)).start()
    threading.Thread(target=receive_from_server,
                     args=(my_name, s, HOST, PORT)).start()


if __name__ == '__main__':
    try:
        my_name = sys.argv[1]
        launch_client(my_name)

    except IndexError:
        launch_client(input('Please input your name: '))