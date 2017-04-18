# coding=utf-8
# 匹配
import re

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print 'OK'
else:
    print 'Failed'

if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
    print 'OK'
else:
    print 'Failed'


# 切分字符串
# 传统的方式
print 'a b   c'.split(' ')
# 正则表达式的方式
print re.split(r'\s+', 'a b   c')
print re.split(r'[\,\s]+', 'a,b, c   d')
print re.split(r'[\;\,\s]+', 'a,b;;c   d')
# 分组
m = re.match(r'(\d{3})-(\d{3,8})', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)
# 默认贪婪匹配
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 加个?可以变成非贪婪匹配
print re.match(r'^(\d+?)(0*)$', '102300').groups()
# 如果一个正则表达式要重复使用很多次，我们需要预编译正则表达式，接下来重复使用时就不需要编译这个步骤了，可以直接匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
# 测试
re_content = re.compile(r'\s*<data name=\"[a-zA-Z\_$][0-9a-zA-Z\_]*.(Text|Tooltip)\" xml:space=\"preserve\"\s*')
if re_content.match('  <data name="ribbonBar1.Text" xml:space="preserve"> '):
    print 'OK'
else:
    print 'NO'

if re_content.match('  <data name="btnFastPhoto.Tooltip" xml:space="preserve">  '):
    print 'OK'
else:
    print 'NO'