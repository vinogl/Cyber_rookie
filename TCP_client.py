import socket


tcp_server = str(input('请输入TCP服务地址: ')).split(':')
address = (str(tcp_server[0]), int(tcp_server[1]))  # TCP_server地址

while True:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(address)

    # 发送消息
    message = str(input('send_to_server: '))
    tcp.send(message.encode('utf-8'))

    # 接受消息
    response = tcp.recv(1024)
    print('server_response: %s' % response.decode('utf-8'))
