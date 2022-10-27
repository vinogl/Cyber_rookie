import socket


# TCP服务端信息
tcp_server = str(input('请输入TCP服务地址: ')).split(':')
address = (str(tcp_server[0]), int(tcp_server[1]))

# 建立连接
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(address)  # 建立tcp连接

while True:

    # 发送消息
    message = str(input('client: '))
    tcp.send(message.encode('utf-8'))

    # 判断是否关闭连接
    if message == 'close':
        tcp.close()
        print('关闭连接')
        break

    # 接受消息
    response = tcp.recv(1024).decode('utf-8')
    print('server: %s' % response)

    # 判断是否关闭连接
    if response == 'close':
        tcp.close()
        print('关闭连接')
        break
