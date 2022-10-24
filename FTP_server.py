import os
import socket
import sys
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def get_host_ip():
    """获取本机ip地址"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


def get_homedir():
    """获取ftp服务的路径"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return os.getcwd()


handler = FTPHandler
handler.authorizer.add_user(username='admin', password='123456',
                            homedir=get_homedir(), perm='elradfmwMT')

server = FTPServer((get_host_ip(), 8080), handler)
server.serve_forever()
