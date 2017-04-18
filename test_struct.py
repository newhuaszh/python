# coding=utf-8
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)
print b1 + b2 + b3 + b4

import struct
# pack函数可以把任意数据类型转成字符串
# '>I'
# >表示字节顺序是big-endian，也就是网络序
# I表示4字节无符号整数
print struct.pack('>I', 10240099)
# H表示2字节无符号整数
# \xf0\xf0\xf0\xf0转成4042322160L
# \x80\x80转成32896
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
'''
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH', s)