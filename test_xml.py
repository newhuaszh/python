# coding=utf-8
'''
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可
以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。
'''
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print 'sax:start_elememt: %s, attrs: %s' % (name, str(attrs))

    def end_element(self, name):
        print 'sex:end_element: %s, ' % name

    def char_data(self, text):
        print 'sax:char_num: ' % text