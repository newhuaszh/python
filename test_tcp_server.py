# coding=utf-8
import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意bind的参数是一个tuple
s.bind(('127.0.0.1', 9999))
# 5表示等待连接的最大数量
s.listen(5)
print 'waiting for connection...'

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send('Hello, %s' % data)
    sock.close()
    print 'Connection from %s:%s closed' % addr

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



