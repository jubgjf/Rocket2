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

    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode().split(' ')
            # print(data)
            if data[0] == my_name:  #仅支持2人联机
                my_position = [int(data[1]), int(data[2])]
                other_position = [int(data[4]), int(data[5])]
            elif len(data) >= 4 and data[3] == my_name:
                my_position = [int(data[4]), int(data[5])]
                other_position = [int(data[1]), int(data[2])]
            elif data[0] == 'enemy':
                enemy_info = [int(data[i]) for i in range(1, len(data) - 1)]
                # print(enemy_info)
            elif data[0] == 'bullet':
                bullet_info = [int(data[i]) for i in range(1, len(data) - 1)]
                # print(bullet_info)
            elif data[0] == 'kill':
                print(data[1], 'is killed')
        except:
            # print('%s' % sys.exc_info()[1])
            pass


def run_game(my_name, s, HOST, PORT):
    # time.sleep(1)  # 让recvive_from_server先启动
    global my_position
    global other_position
    global enemy_info
    global bullet_info
    """ 窗口设置 """
    FpsClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Rocket Online --- ' + my_name)
    pygame.display.set_icon(pygame.image.load('pictures/Icon.png'))
    """ 建立Group """
    ShipGroup = pygame.sprite.Group()
    ShipGroup.add(Ship(screen))
    OtherShipGroup = pygame.sprite.Group()
    OtherShipGroup.add(OtherShip(screen))
    EnemyShipGroup = pygame.sprite.Group()
    enemy_index_pointer = 1
    BulletGroup = pygame.sprite.Group()
    bullet_index_pointer = 1

    while 1:
        FpsClock.tick(80)
        screen.fill((5, 70, 160))
        """ 玩家飞船 """
        for i in ShipGroup:
            try:
                i.draw(my_position)
                """ 检测与外星人碰撞 """
                if pygame.sprite.spritecollide(i, EnemyShipGroup, False):
                    message = ' '.join(('$ kill', my_name))
                    s.sendto(message.encode(), (HOST, PORT))
            except:
                # print('>> Error! %s\n' % sys.exc_info()[1])
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
        try:
            # print(len(EnemyShipGroup), len(enemy_info))
            if 3 * len(EnemyShipGroup) < len(enemy_info):
                for i in range(3 * enemy_index_pointer - 1,
                               len(enemy_info) - 3, 3):
                    # enemy_info=[100, 200, 1, 300, 400, 2, 190, 230, 3, 200, 800, 4]
                    EnemyShipGroup.add(EnemyShip(screen, enemy_info[i]))
                    enemy_index_pointer = enemy_info[i + 3]  #记录enemy_index到哪里了
        except:
            pass

        for i in EnemyShipGroup:
            try:
                for j in range(0, len(enemy_info), 3):
                    if i.index == enemy_info[j + 2]:
                        i.draw((enemy_info[j], enemy_info[j + 1]))
            except:
                pass
        """ 子弹 """
        try:
            # print(bullet_info)
            if 3 * len(BulletGroup) < len(bullet_info):
                BulletGroup.add(Bullet(screen, bullet_index_pointer))
                # bullet_index_pointer += 1
                bullet_index_pointer = bullet_info[len(bullet_info) - 1] + 1
                # 重新调整pointer，防止过大，否则无法发射子弹（不知道这个bug为什么出现）
            elif 3 * len(BulletGroup) > len(bullet_info):
                for bullet in BulletGroup:
                    if bullet.index not in bullet_info:
                        BulletGroup.remove(bullet)
        except:
            pass

        for bullet in BulletGroup:
            for i in range(0, len(bullet_info), 3):
                if bullet.index == bullet_info[i + 2]:
                    bullet.draw((bullet_info[i], bullet_info[i + 1]))
                    # print(bullet_info)
                    break
        """ 刷新屏幕 """
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


def launch_client(my_name):
    # my_name = input('input your name: ')
    # print(my_name)

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
    bullet_info = []
    bullet_fire_frequency = 0

    try:
        my_name = sys.argv[1]
        launch_client(my_name)

    except IndexError:
        launch_client(input('Please input your name: '))