import socket
import sys
import time

# 获取本地ip
HOST = '172.22.12.150'
PORT = 30000
# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 将socket绑定到本机IP和端口
s.bind((HOST, PORT))


def response_move_keys(key_str, position):
    position_str = ''

    if 'w' in key_str:
        position[1] -= 1
    if 'a' in key_str:
        position[0] -= 1
    if 's' in key_str:
        position[1] += 1
    if 'd' in key_str:
        position[0] += 1

    position_str = ' '.join((str(position[0]), str(position[1])))
    return position_str


# def response_bullet_keys(key_str, player_position):
#     global bullet_info
#     bullet_position_str = ''

#     if 'j' in key_str:
#         bullet_info = [player_position[0], player_position[1]]

#     bullet_position_str = ' '.join((str(bullet_info[0]), str(bullet_info[1])))
#     return bullet_position_str


def enemy_move():
    global enemy_info
    # ['100', '200', 1, 1] 分别是横坐标、纵坐标，横向速度，纵向速度
    global enemy_move_frequency

    if time.time() - enemy_move_frequency>0.01:
        enemy_info[0] = int(enemy_info[0])
        enemy_info[1] = int(enemy_info[1])

        enemy_info[0] += enemy_info[2]
        enemy_info[1] += enemy_info[3]

        if enemy_info[0] > 800 or enemy_info[0] < 0:
            enemy_info[2] = -enemy_info[2]
        if enemy_info[1] > 600 or enemy_info[1] < 0:
            enemy_info[3] = -enemy_info[3]

        enemy_info[0] = str(enemy_info[0])
        enemy_info[1] = str(enemy_info[1])

        enemy_move_frequency=time.time()

    return ' '.join((enemy_info[0], enemy_info[1])) + '  '


def receive_message(s):
    global player_dict
    """ 接收数据 """
    try:
        data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址
        data = data.decode()
        """ 拆分数据内容 """
        data_list = data.split(' ')
        # data_list = ['guan', '100', '200', 'wasdj']
        name = data_list[0]  # 'guan'
        position = [int(data_list[1]), int(data_list[2])]  # [100, 200]
        key_str = data_list[3]  # 'wasdj'
        """ 更新位置 """
        # bullet_position = response_bullet_keys(key_str, position)  # '100 205'
        position = response_move_keys(key_str, position)  # '102 201'
        """ 玩家集合 """
        player_dict[addr] = ' '.join((name, position))
        # { addr1 : "guan 100 200" , addr2 : "liu 200 230" }
        """ 发送信息 """
        message = ''
        for info in player_dict.values():
            message = message + info + ' '
        # "guan 100 200 liu 200 230 "
        for player in player_dict:
            s.sendto(message.encode(), player)  #发送玩家飞船位置信息
            s.sendto(('enemy ' + enemy_move()).encode(), player)  #发送外星人位置信息
            # s.sendto(('bullet ' + bullet_position).encode(), player)  #发送子弹位置信息

    except:
        print('>> Error! %s\n' % sys.exc_info()[1])
        sys.exit(0)


if __name__ == '__main__':
    player_dict = {}
    enemy_info = ['100', '200', 1, 1]
    # bullet_info = ['-100', '-100']
    enemy_move_frequency=0

    while 1:
        receive_message(s)
