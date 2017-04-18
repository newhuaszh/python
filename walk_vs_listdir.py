# coding=utf-8
import os

# 路径如果有中文，需要解码
# 字符串在python内部的表示是unicode编码
# 因此，在做编码转换时，需要以unicode作为中间码
# 即先将其它编码的字符串解码(decode)成unicode
# 再从unicode编码(encode)成另一种编码
# decode('utf-8')表示将utf-8编码的字符串转成unicode编码的字符串
# encode('utf-8')表示将unicode编码的字符串转成utf-8编码的字符串
dirname = u'D:\控件'

# 利用os.walk遍历某个目录下的所有文件
def walk_dir(dirname):
    for parent, dirnames, filenames in os.walk(dirname):
        for f in filenames:
            print os.path.join(parent, f)


walk_dir(dirname)

# 利用os.listdir遍历某个目录下的所有文件
def walk_dir_listdir(dirname):
    for d in os.listdir(dirname):
        fullname = os.path.join(dirname, d)
        if os.path.isdir(fullname):
            walk_dir_listdir(fullname)
        elif os.path.isfile(fullname):
            print fullname

walk_dir_listdir(dirname)

# 利用os.listdir遍历某个目录下的所有文件，配合yield做成generater
def walk_dir_listdir_yield(dirname):
    for d in os.listdir(dirname):
        fullname = os.path.join(dirname, d)
        if os.path.isdir(fullname):
            for dsub in walk_dir_listdir_yield(fullname):
                yield dsub
        elif os.path.isfile(fullname):
            yield fullname

for d in walk_dir_listdir_yield(dirname):
    print d