# coding=utf-8
import time

# consumer是一个generator生成器
def consumer():
    print 'first enter consumer'
    r = ''
    while True:
        print 'loop'
        n = yield r
        if not n:
            return
        print '[CONSUMER] Consuming %s' % n
        time.sleep(1)
        r = '200 OK'

def produce(c):
    print 'first enter produce'
    # 启动生成器
    c.next()
    n = 0
    while n < 5:
        n += 1
        print '[PRODUCER] Producing %s' % n
        # 通过调用c.send(n)，切换到consumer执行
        r = c.send(n)
        print '[PRODUCER] Cosumer return: %s' % r
    c.close()

c = consumer()
produce(c)