# coding=utf-8
def application(environ, start_response):
    # 参数1：HTTP响应码
    # 参数2：一个list，每个元素是由两个str组成的tuple
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
