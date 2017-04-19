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
        print 'sax:char_data: %s' % text

xml = r'''<?xml version="1.0"?>
<ol>
<li><a href="/python">Python</a></li>
<li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler  = DefaultSaxHandler()
parser = ParserCreate()
# returns_unicode为True时，返回的所有element名称和char_data都是unicode，处理国家化更加方便
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
# 如果读取一大段字符串，CharacterDataHandler可能会被多次调用，就需要把每次获取的内容保存起来，在EndElementHandler里进行合并
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 大部分情况下，需要生成的XML结构都是非常简单的，所以最简单和最高效的生成XML的方法是拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data')
L.append(r'</root>')
# 将list输出成str的方式
print ''.join(L)
# 如果要生成复杂的XML呢？就不要用XML了，用JSON