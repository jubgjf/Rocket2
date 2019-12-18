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


class AircraftMap(pygame.sprite.Sprite):
    def __init__(self, screen, index):
        super(AircraftMap, self).__init__()
        self.screen = screen
        self.index = index
        self.image = pygame.image.load(r'pictures/Online/AircraftMap.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = -50

    def draw(self):
        self.screen.blit(self.image, self.rect)


class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, screen, index):
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.index = index
        self.image = pygame.image.load(r'pictures/EnemyShipClassic.png')
        self.rect = self.image.get_rect()

    def draw(self, position):
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        self.screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, index):
        super(Bullet, self).__init__()
        self.screen = screen
        self.index = index
        self.image = pygame.image.load(r'pictures/Bullet.png')
        self.image = pygame.transform.smoothscale(self.image, (3, 10))
        self.rect = self.image.get_rect()

    def draw(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.screen.blit(self.image, self.rect)


def get_keys():
    global bullet_fire_frequency
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
    if keys[pygame.K_p]:
        key_set.add('p')
    if keys[pygame.K_j] and time.time() - bullet_fire_frequency > 0.2:
        key_set.add('j')
        bullet_fire_frequency = time.time()

    for key in key_set:
        key_str += key

    return key_str


def receive_from_server(my_name, s, HOST, PORT):
    global my_position
    global other_position
    global enemy_info
    global bullet_info

    while 1:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode().split(' ')
            """ 以下对data进行分类 """
            if data[0] == my_name:
                """ 仅支持两人联机 """
                my_position = [int(data[1]), int(data[2])]
                other_position = [int(data[4]), int(data[5])]
            elif len(data) >= 4 and data[3] == my_name:
                my_position = [int(data[4]), int(data[5])]
                other_position = [int(data[1]), int(data[2])]
            elif data[0] == 'enemy':
                """ 外星人信息 """
                enemy_info = [int(data[i]) for i in range(1, len(data) - 1)]
                for i in range(0, len(enemy_info), 3):
                    enemy_info[i + 2] = str(enemy_info[i + 2])
            elif data[0] == 'bullet':
                """ 子弹信息 """
                bullet_info = [int(data[i]) for i in range(1, len(data) - 1)]
                for i in range(0, len(bullet_info), 3):
                    bullet_info[i + 2] = str(bullet_info[i + 2])
            elif data[0] == 'kill':
                """ 玩家死亡信息 """
                print(data[1], 'is killed')
        except:
            """ 建立连接刚开始时可能会抛出异常 """
            pass


def avoid_enemy_info_empty(enemy_info):
    """ 由于网络延时，收到的enemy_info有时会突变为空列表，导致所有外星人突然消失 """
    global temp_enemy_info  # 作为enemy_info非空时的缓存

    if enemy_info == []:
        if len(temp_enemy_info) == 3:
            temp_enemy_info = enemy_info
        else:  #说明enemy_info是突变为空列表
            enemy_info = temp_enemy_info
    if enemy_info != []:
        temp_enemy_info = enemy_info

    return enemy_info


def run_game(my_name, s, HOST, PORT):
    pygame.init()

    global my_position
    global other_position
    global enemy_info
    global bullet_info
    """ 窗口设置 """
    FpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Rocket Online --- ' + my_name)
    pygame.display.set_icon(pygame.image.load('pictures/Icon.png'))
    """ 建立Group """
    ShipGroup = pygame.sprite.Group()
    ShipGroup.add(Ship(screen))
    OtherShipGroup = pygame.sprite.Group()
    OtherShipGroup.add(OtherShip(screen))
    AircraftMapGroup = pygame.sprite.Group()
    AircraftMapGroup.add(AircraftMap(screen, 'me'))
    AircraftMapGroup.add(AircraftMap(screen, 'other'))
    EnemyShipGroup = pygame.sprite.Group()
    enemy_index_pointer = '1'
    BulletGroup = pygame.sprite.Group()
    bullet_index_pointer = '1'

    while 1:
        FpsClock.tick(80)
        screen.fill((5, 70, 160))
        """ 飞船重生引导箭头 """
        for pointer in AircraftMapGroup:
            try:
                if pointer.index == 'me':
                    if my_position[1] > 600:
                        pointer.rect.bottom = 600
                        pointer.rect.centerx = my_position[0]
                    else:
                        pointer.rect.centery = -50
                elif pointer.index == 'other':
                    if other_position[1] > 600:
                        pointer.rect.bottom = 600
                        pointer.rect.centerx = my_position[0]
                    else:
                        pointer.rect.centery = -50
                pointer.draw()
            except:
                pass
        """ 玩家飞船 """
        for i in ShipGroup:
            try:
                i.draw(my_position)
                """ 检测与外星人碰撞 """
                if pygame.sprite.spritecollide(i, EnemyShipGroup, False):
                    message = ' '.join(('$ kill', my_name))
                    s.sendto(message.encode(), (HOST, PORT))
            except:
                """ 刚建立连接时，my_position为空，可能会抛出异常 """
                pass
            message = ' '.join((my_name, str(i.rect.centerx),
                                str(i.rect.centery), get_keys()))
            s.sendto(message.encode(), (HOST, PORT))
        """ 联机玩家飞船 """
        for i in OtherShipGroup:
            try:
                i.draw(other_position)
            except:
                pass
        """ 外星人 """
        enemy_info = avoid_enemy_info_empty(enemy_info)
        if 3 * len(EnemyShipGroup) < len(enemy_info):
            EnemyShipGroup.add(EnemyShip(screen, enemy_index_pointer))
            enemy_index_pointer = str(int(enemy_index_pointer) + 1)
        elif 3 * len(EnemyShipGroup) > len(enemy_info):
            for enemy in EnemyShipGroup:
                if enemy.index not in enemy_info:
                    EnemyShipGroup.remove(enemy)

        for enemy in EnemyShipGroup:
            for i in range(0, len(enemy_info), 3):
                if enemy.index == enemy_info[i + 2]:
                    enemy.draw((enemy_info[i], enemy_info[i + 1]))
                    break
        """ 子弹 """
        if 3 * len(BulletGroup) < len(bullet_info):
            BulletGroup.add(Bullet(screen, bullet_index_pointer))
            bullet_index_pointer = str(int(bullet_index_pointer) + 1)
        elif 3 * len(BulletGroup) > len(bullet_info):
            for bullet in BulletGroup:
                if bullet.index not in bullet_info:
                    BulletGroup.remove(bullet)

        for bullet in BulletGroup:
            for i in range(0, len(bullet_info), 3):
                if bullet.index == bullet_info[i + 2]:
                    bullet.draw((bullet_info[i], bullet_info[i + 1]))
                    break
        """ 刷新屏幕 """
        pygame.display.update()
        """ 检测退出 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


def launch_client(my_name):
    HOST = '172.22.12.150'  # 图书馆
    # HOST = '172.22.67.121'  # 寝室
    PORT = 30000
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    threading.Thread(target=run_game, args=(my_name, s, HOST, PORT)).start()
    threading.Thread(target=receive_from_server,
                     args=(my_name, s, HOST, PORT)).start()


if __name__ == '__main__':
    my_position = []
    other_position = []
    enemy_info = []
    temp_enemy_info = []
    bullet_info = []
    bullet_fire_frequency = 0

    try:
        my_name = sys.argv[1]
        launch_client(my_name)

    except IndexError:
        launch_client(input('Please input your name: '))