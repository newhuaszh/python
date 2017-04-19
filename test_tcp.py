# coding=utf-8
import socket
# AF_INET表示使用IPv4协议，如果要使用IPv6，则使用AF_INET6
# SOCK_STREAM表示使用的是面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 80端口时web服务的标准端口，SMTP服务是25端口，FTP服务是21端口
# 小于1024的端口时Internet标准服务的端口，端口号大于1024的，可以任意使用
# 注意connect的参数是一个tuple，包含地址和端口号
s.connect(('www.sina.com.cn', 80))
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = ''.join(buffer)
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
