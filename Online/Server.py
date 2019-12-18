import socket
import sys
import time
import random


def response_client_keys(key_str, position):
    """ 响应用户按键 """
    """ 外星人 """
    global enemy_index
    global enemy_info
    global player_add_enemy_frequency
    """ 子弹 """
    global bullet_info
    global player_bullet_frequency
    global bullet_index
    """ 飞船位置 """
    player_position_str = ''
    player_speed = [2, 2]
    """ 移动 """
    if 'w' in key_str and position[1] > 0:
        position[1] -= player_speed[1]
    if 'a' in key_str and position[0] > 0:
        position[0] -= player_speed[0]
    if 's' in key_str and position[1] < 600:
        position[1] += player_speed[1]
    if 'd' in key_str and position[0] < 800:
        position[0] += player_speed[0]
    """ 添加外星人 """
    if 'p' in key_str:
        if time.time() - player_add_enemy_frequency > 0.5:
            enemy_info.append(str(int(random.randint(0, 800))))
            enemy_info.append(str(int(random.randint(0, 600))))
            enemy_info.append(int(random.randint(1, 3)))
            enemy_info.append(int(random.randint(1, 3)))
            enemy_info.append(enemy_index)
            enemy_index = str(int(enemy_index) + 1)

            player_add_enemy_frequency = time.time()
    """ 发射子弹 """
    if 'j' in key_str:
        if time.time() - player_bullet_frequency > 0.1:
            bullet_info.append(str(position[0]))
            bullet_info.append(str(position[1]))
            bullet_info.append(bullet_index)
            bullet_index = str(int(bullet_index) + 1)

            player_bullet_frequency = time.time()

    player_position_str = ' '.join((str(position[0]), str(position[1])))
    return player_position_str


def enemy_move():
    global enemy_info
    # ['100', '200', 1, 1, '1']
    # 横坐标、纵坐标，横向速度，纵向速度，飞船序号
    global enemy_move_frequency

    if time.time() - enemy_move_frequency > 0.01:
        for i in range(0, len(enemy_info), 5):
            enemy_info[i] = int(enemy_info[i])
            enemy_info[i + 1] = int(enemy_info[i + 1])

            enemy_info[i] += enemy_info[i + 2]
            enemy_info[i + 1] += enemy_info[i + 3]
            """ 在屏幕边缘反弹 """
            if enemy_info[i] > 800 or enemy_info[i] < 0:
                enemy_info[i + 2] = -enemy_info[i + 2]
            if enemy_info[i + 1] > 600 or enemy_info[i + 1] < 0:
                enemy_info[i + 3] = -enemy_info[i + 3]

            enemy_info[i] = str(enemy_info[i])
            enemy_info[i + 1] = str(enemy_info[i + 1])

        enemy_move_frequency = time.time()

    result = []
    for i in range(0, len(enemy_info), 5):
        result.append(enemy_info[i])
        result.append(enemy_info[i + 1])
        result.append(enemy_info[i + 4])

    return ' '.join(result) + ' '


def bullet_move():
    global bullet_info
    # ['100', '200', '1']
    # 横坐标，纵坐标，子弹序号
    global bullet_move_frequency

    try:
        if time.time() - bullet_move_frequency > 0.02:
            for i in range(0, len(bullet_info), 3):
                if int(bullet_info[i + 1]) < -20:
                    for j in range(3):
                        """ 移除屏幕外子弹 """
                        del (bullet_info[i])

                bullet_info[i + 1] = int(bullet_info[i + 1])
                bullet_info[i + 1] -= 10  # 子弹速度为10
                bullet_info[i + 1] = str(bullet_info[i + 1])

            bullet_move_frequency = time.time()

    except:
        """ 删除bullet_info中的子弹时，i可能发生越界 """
        pass

    result = []
    for i in range(0, len(bullet_info), 3):
        result.append(bullet_info[i])
        result.append(bullet_info[i + 1])
        result.append(bullet_info[i + 2])

    return ' '.join(result) + ' '


def bullet_kill():
    global enemy_info
    # ['100', '200', 1, 1, '1'] 分别是横坐标、纵坐标，横向速度，纵向速度，飞船序号
    global bullet_info
    # ['100', '200', '1'] 分别是横坐标，纵坐标，子弹序号

    try:
        for i in range(0, len(enemy_info), 5):
            for j in range(0, len(bullet_info), 3):
                """ 检测碰撞 """
                if int(enemy_info[i + 1]) - int(bullet_info[j + 1])<=10 and \
                    int(enemy_info[i + 1]) - int(bullet_info[j + 1]) >= -10 and \
                    int(enemy_info[i]) - int(bullet_info[j]) <= 20 and \
                    int(enemy_info[i]) - int(bullet_info[j]) >= -20:
                    for k in range(3):
                        del (bullet_info[j])
                    for k in range(5):
                        del (enemy_info[i])
    except:
        """ 删除bullet_info和enemy_info中的元素时，i,j可能发生越界 """
        pass


def receive_message(s):
    global player_dict
    while 1:
        bullet_kill()
        try:
            """ 接收数据 """
            data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址
            data = data.decode()
            """ 拆分数据内容 """
            data_list = data.split(' ')
            # data_list = ['guan', '100', '200', 'wasdj'] -> 一般信息
            # data_list = ['$', '...'] -> 特殊信息
            if data_list[0] != '$':
                name = data_list[0]  # 'guan'
                position = [int(data_list[1]), int(data_list[2])]  # [100, 200]
                key_str = data_list[3]  # 'wasdj'
                """ 更新位置 """
                position = response_client_keys(key_str, position)  # '102 201'
                """ 玩家集合 """
                player_dict[addr] = ' '.join((name, position))
                # { addr1 : "guan 100 200" , addr2 : "liu 200 230" }
                """ 发送信息 """
                message = ''
                for info in player_dict.values():
                    message = message + info + ' '  # "guan 100 200 liu 200 230 "
                for player in player_dict:
                    s.sendto(message.encode(), player)  # 发送玩家飞船位置信息
                    if enemy_move()[0].isdigit():  # 发送外星人位置信息
                        s.sendto(('enemy ' + enemy_move()).encode(), player)
                    else:
                        s.sendto(('enemy ').encode(), player)
                    if bullet_move()[0].isdigit():  # 发送子弹位置信息
                        s.sendto(('bullet ' + bullet_move()).encode(), player)
                    else:
                        s.sendto(('bullet ').encode(), player)
            else:
                if data_list[1] == 'kill':
                    for player in player_dict:
                        message = ' '.join(('kill', data_list[2]))
                        s.sendto(message.encode(), player)
        except:
            print(sys.exc_info())


if __name__ == '__main__':
    """ 获取本地IP """
    HostName = socket.gethostname()
    HOST = socket.gethostbyname(HostName)
    PORT = 30000
    """ 创建socket对象 """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """ 将socket绑定到本机IP和端口 """
    s.bind((HOST, PORT))
    """ 输出服务端启动信息 """
    print('Launch Server Successfully!')
    """ 玩家字典 """
    player_dict = {}
    """ 外星人 """
    enemy_index = '1'
    enemy_info = []
    enemy_move_frequency = 0
    player_add_enemy_frequency = 0
    """ 子弹 """
    bullet_index = '1'
    bullet_info = []
    bullet_move_frequency = 0
    player_bullet_frequency = 0
    """ 接收客户端信息 """
    receive_message(s)
