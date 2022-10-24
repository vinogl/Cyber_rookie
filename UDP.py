import socket


class UdpClient:

    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self):
        # remote地址信息
        remote = str(input('请输入UDP接收地址: ')).split(':')
        self.remote = (str(remote[0]), int(remote[1]))  # remote接收消息的ip地址与port
        # 发送消息
        print('<<<<<开始发送消息>>>>>')
        while True:
            message = str(input('localhost: '))
            self.udp.sendto(message.encode('utf-8'), self.remote)

    def receive(self):
        # local地址信息
        udp_port = int(input('请输入UDP接收端口号(port): '))
        print('接收地址: %s:%d' % (self.get_host_ip(), udp_port))
        self.local = (self.get_host_ip(), udp_port)  # local接收消息的ip地址与port
        self.udp.bind(self.local)  # 将在指定IP地址的指定端口接受消息
        # 接收消息
        print('<<<<<开始接收消息>>>>>')
        while True:
            data, addr = self.udp.recvfrom(1024)
            print('%s: %s' % (addr[0], data.decode('utf-8')))

    @staticmethod
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
    udp = UdpClient()
    udp_type = str(input('udp选项-receive(r)/send(s): '))
    if udp_type == 'r':
        udp.receive()
    elif udp_type == 's':
        udp.send()
