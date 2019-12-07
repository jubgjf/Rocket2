import socket
import sys

# 获取本地ip
HOST = '172.22.12.150'
PORT = 30000
# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 将socket绑定到本机IP和端口
s.bind((HOST, PORT))


def response_keys(key_str, position):
    position_str=''

    if 'w' in key_str:
        position[1] -= 1
    if 'a' in key_str:
        position[0] -= 1
    if 's' in key_str:
        position[1] += 1
    if 'd' in key_str:
        position[0] += 1

    position_str=' '.join((str(position[0]),str(position[1])))
    return position_str


def receive_message(s):
    global player_dict

    """ 接收数据 """
    data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址
    data = data.decode()

    """ 拆分数据内容 """
    data_list = data.split(' ')
    name = data_list[0]
    position = [int(data_list[1]), int(data_list[2])]
    key_str = data_list[3]

    """ 更新位置 """
    position=response_keys(key_str, position)
    
    """ 玩家集合 """
    player_dict[addr]=' '.join((name,position))
    
    """ 发送信息 """
    message=''
    for info in player_dict.values():
        message =message +info+' '
    for player in player_dict:
        s.sendto(message.encode(),player)
        

if __name__ == '__main__':
    player_dict={}
    
    while 1:
        receive_message(s)
