import socket
import threading
import sys

# 获取本地ip
HostName = socket.gethostname()
HOST = socket.gethostbyname(HostName)
PORT = 30000
# 定义保存所有socket的列表
socket_list = []
# 创建socket对象
ss = socket.socket()
# 将socket绑定到本机IP和端口
ss.bind((HOST, PORT))
# 服务端开始监听来自客户端的连接
ss.listen()


def read_from_client(s):
    try:
        return str(s.recv(2048), encoding='utf8')
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        # 删除该socket
        socket_list.remove(s)


def server_target(s):
    try:
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            Name = content.split(' ')[0]
            PositionStr = (content.split(' ')[1], content.split(' ')[2])
            PositionStr=' '.join(PositionStr)
            # print(Name)
            # print(PositionStr)

            if PositionStr is None:
                break

            # else:
            #     """ 显示客户端飞船位置 """
            #     print('%s: %s' % (Name, PositionStr))

            for client_s in socket_list:
                client_s.sendall(bytes(content, encoding='utf8'))
    except AttributeError:
        print('>> AttributeError. Client may offline')
        print('Remain %d Client Online' % len(socket_list))
    except:
        print('>> Unexpected Error :', sys.exc_info()[1])


while True:
    # 此行代码会阻塞，将一直等待别人的连接
    s, addr = ss.accept()
    socket_list.append(s)
    print('%d Client Online' % len(socket_list))
    # 每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s, )).start()
