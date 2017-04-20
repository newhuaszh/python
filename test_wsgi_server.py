# coding=utf-8
from wsgiref.simple_server import make_server
from test_wsgi_hello import application

# 第一个参数为地址，端口8000，处理函数是application
httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000...'
# 开始监听http请求
httpd.serve_forever()