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

    for key in key_set:
        key_str += key

    return key_str


def receive_from_server(my_name,s, HOST, PORT):
    global my_position
    global other_position

    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode().split(' ')
            print(data)
            if data[0]==my_name:
                my_position = [int(data[1]), int(data[2])]
                other_position=[int(data[4]), int(data[5])]
            else:
                my_position=[int(data[4]), int(data[5])]
                other_position = [int(data[1]), int(data[2])]
        except:
            pass


def run_game(my_name, s, HOST, PORT):
    global my_position
    global other_position

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

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


if __name__ == '__main__':
    my_name = input('input your name: ')

    HOST = '172.22.12.150'
    PORT = 30000
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_position = []
    other_position=[]

    threading.Thread(target=run_game, args=(my_name, s, HOST, PORT)).start()
    threading.Thread(target=receive_from_server, args=(my_name,s, HOST, PORT)).start()
