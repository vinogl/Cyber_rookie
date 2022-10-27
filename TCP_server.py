import socket
import time


def get_host_ip():
    """获取本机ip地址"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


if __name__ == '__main__':

    # TCP服务端信息
    port = int(input('TCP服务端口号: '))
    print('TCP服务地址: %s:%d' % (get_host_ip(), port))
    address = (get_host_ip(), port)

    # 建立连接
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    """
    setsockopt():
    SOL_SOCKET:对Socket层进行设置
    SO_REUSEADDR: 是否允许在bind过程中本地地址可重复使用(1: 允许)
    
    若不允许，在关闭连接后立刻连接会有以下报错：
    OSError: [Errno 98] Address already in use
    
    这是因为：（MSL指一个片段在网络中最大的存活时间，一般为30s）
    在TCP/IP终止连接的四次握手中，当最后的ACK回复发出后，有个2MSL的时间等待。
    
    为什么要等待2MSL：
    是因为在最后发出ACK后，发送方不能确认ACK是否被另一端正常收到，
    如果另一端没有收到ACK回复的话，将会在1MSL后再次发送FIN。
    所以说发送方等待2MSL时间，如果此时间内都没有再次收到FIN片段的话，
    发送方就假设对方已经正常接收到了ACK回复，此时它就会正常关闭连接！
    """
    tcp.bind(address)  # 服务期需要监听的ip地址和端口号
    tcp.listen(5)  # 最大连接数设为5
    client, address = tcp.accept()  # 建立tcp连接

    while True:

        # 接受client信息
        message = client.recv(1024).decode('utf-8')
        print('client: %s' % message)
        time.sleep(0.1)

        # 判断是否关闭连接
        if message == 'close':
            client.close()
            print('关闭连接')
            break

        # 给client的反馈
        response = str(input('server: '))
        client.send(response.encode('utf-8'))

        # 判断是否关闭连接
        if response == 'close':
            client.close()
            print('关闭连接')
            break
