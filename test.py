# coding:utf-8
import sys
import math


# print sys.version
# print'\n'.join([''.join([('AndyLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])
# print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)])for y in range(-20,20)])

# 集合
# p = ['apple', 1, True]
# s = ['python', p, 2, 'php']
# print len(s)
#
# 元组
# tpl = ('apple', 1, True)
# # tpl[0] = 'orange'
# print tpl
# tpl = (1,)
# print tpl
#
# if语句
# age = 20
# if age >= 18:
#     print 123
#     print 'lalala'
# elif age < 5:
#     print 'haha'
#
# 0 空字符串 空列表 空元组 作为条件时都为False
# condition = ()
#
# if condition:
#     print '1'
# else:
#     print '2'

# for循环
# names = ['m', 'b', 't']
# for name in names:
#     print name
#
# in 后面可以直接定义列表或元组
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum += x
# print sum

# range使用
# sum = 0
# for x in range(101):
#     sum += x
# print sum

# while循环
# sum = 0
# n = 99
# while n > 0:
#     sum += n
#     n -= 2
# print sum

# 键盘输入 raw_input
# birth = raw_input('生日：')
# if birth.isdigit() and int(birth) > 2000:
#     print 'a'
# else:
#     print 'b'

# 字典用法
# d = {}
# d['mm'] = 67
# print d['mm']
# print 'm' in d
# print d.get('mm', 222)

# set用法
# s = set([1,1,1,1])
# s.add(2)
# s.remove(1)
# print s

# set用做求交集和并集 set的元素不可变，可以是元组
# s1 = set([1, 2, (4, 5, 6)])
# s2 = set([2, 3, 4])
# print s1 & s2
# print s1 | s2

# sort用法
# a = ['c', 'b', 'a']
# a.sort()
# print a

# 字符串是不可变的，而字符串变量是可变的
# a = 'abc'
# b = a.replace('a', 'A')
# print b, a

# 内置的一些函数 需要import math
# print abs(-10)
# print cmp(3, 1)
# print cmp(3, 3)
# print cmp(3, 5)

# 数据类型转换
# print int('123')
# print int(12.34)
# print float('12.34')
# print str(123)
# print unicode(100)
# print bool([1])
# print bool('')

# 函数名只是一个引用，可以使用其它变量来重命名
# a = abs
# print a(-100)

# 可以使用isinstance来判断数据的类型
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print my_abs('a')

# 函数可以返回多个值，如下方的x, y，实际上x, y是一个元组
# def move(x, y, step, angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
# x, y = move(100, 100, 60, math.pi / 6)
# z = move(100, 100, 60, math.pi / 6)
# print x, y
# print z

# 默认参数，有多个参数时，变化小的放在后面作为默认参数
# 必选参数在前面，默认参数在后面，否则会报错
# def power(x, n=2):
#     s = 1
#     if n > 0:
#         while n > 0:
#             s *= x
#             n -= 1
#         return s
#     else:
#         return 1
# print power(5, n=4)

# 这里有个关于默认参数的坑，多次调用每次的返回值不一样，像是记住上一次的结果
# 解释：默认参数的值初始是[]，是引用类型，每次调用函数add_end会修改l，也就修改了默认参数的值，调用一次增加一个‘end’
#      第二次调用时，默认参数的值是['end']，第三次调用时，默认参数的值是['end', 'end']
# 注意：为了避免这种情况发生，默认参数必须设为不可变的对象
# def add_end(l=[]):
#     l.append('end')
#     return l
#
# print add_end()
# print add_end()
# print add_end()
#
# def add_end_new(l=None):
#     if l is None:
#         l = []
#     l.append('end')
#     return l
#
# print add_end_new()
# print add_end_new()
# print add_end_new()
#
# # 注意l1、l2是互相引用的关系,指向了同一个内容，修改其中一个的值会影响另一个
# l1 = []
# l2 = l1
# l1.append(123)
# print l1, l2

# 可变参数
# 1.使用list或者tuple
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
#
# print calc([1, 2, 3])
# 2.使用可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
#
# print calc(1, 2)
# print calc(1, 2, 3)
# print calc()
# 3.如果已经有了一个list或者tuple，可以在list或者tuple的前面加上*
# nn = (1, 2, 3, 4)
# print calc(*nn)

# 关键字参数
# def person(name, age, **kw):
#     print 'name:', name, ' age:', age, ' other:', kw
#
# person('szh', 20, country='china', province='jiangsu', city='suzhou')
# person('szh', 20, **{'cc': 'china'})
# dic = {'country': 'china'}
# person('szh', 22, **dic)

# 参数组合
# def func(a, b, c=0, *args, **kw):
#     print 'a =', a, ' b =', b, ' c =', c, ' args =', args, ' kw =', kw
#
# func(1, 2, 'a', 'b', cc=9)
# args = (1, 2, 3, 5, 7, 8)
# kw = {'x': 99}
# func(*args, **kw)

# 递归函数 1000层就出错 需要用尾递归优化：return语句不能包含表达式
# def fact(n):
#     if n > 1:
#         return n * fact(n - 1)
#     else:
#         return 1
#
# print fact(999)

# 可惜解释器没有针对尾递归做优化，还是会导致栈溢出
# def factNew(n):
#     return fact_iter(n, 1)
#
# def fact_iter(n, rt):
#     if n == 1:
#         return rt
#     else:
#         return fact_iter(n - 1, n * rt)
#
# print factNew(998)

# print range(1, 100, 2)
# l = []
# n = 1
# while n <= 99:
#     l.append(n)
#     n += 2
# print l

# 取前3个元素 0:3 索引>=0 and <3，取出范围内的所有元素，不管索引有没有越界
# l[起始索引:终止索引:步进(每多少个取一个)]
# l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print l[0:3]
# print l[-5:-2]
# print l[::2]
# print (1, 2, 3, 4, 5, 6)[-3:]

# 迭代字典，默认迭代的是key，可以使用itervalues来迭代value
# d = {'a': 1, 'b': 2, 'c': 3}
# for value in d.itervalues():
#     print value
#
# for k, v in d.iteritems():
#     print k, v

# 判断是否可以迭代
# from collections import Iterable
#
# print isinstance('abc', Iterable)
# print isinstance(123, Iterable)

# enumerate将list转成索引-元素对
# for i, value in enumerate(['A', 'B', 'C']):
#     print i, value

# for循环中引用两个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print x, y

# range使用
# print range(1, 11)
# 生成[1*1, 2*2, 3*3, ...,10*10]
# print [x * x for x in range(1, 11)]
# print [x * x for x in range(1, 11) if x % 2 == 0]
# 循环嵌套
# print [m + n * o for m in 'ABC' for n in 'XYZ' for o in [1, 2, 3]]
# 列出当前目录下的所有文件和目录名
# import os
# print [d for d in os.listdir('.')]
# 使用旧列表生成新列表
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print [k + '=' + v for k, v in d.iteritems()]
# 把list中的所有字符变成小写
# l = ['Hello', 'World', 18, 'IBM', 'Apple']
# print [small.lower() for small in l if isinstance(small, str)]

# 生成器generator 直接创建一个100万个元素的列表很占内存，通过生成器一边循环一边计算，generator保存的是算法
# 方法1：把[]改成()
# l = [x * x for x in range(10)]
# print l
# g = (x * x for x in range(10))
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next() # 超出数量则报错
# for v in g:
#     print v
# 方法2：yield 如果一个函数包含yield关键字，那么这个函数就是个generator
# 斐波那契数列
# def fib(num):
#     first, second, n = 0, 1, 0
#     while n < num:
#         yield second
#         first, second = second, first + second
#         n += 1
#
# for v in fib(90):
#     print v
#
# def odd():
#     yield 1
#     yield 3
#     yield 5
# o = odd()
# print o.next()
# print o.next()
# print o.next()

# 函数作为参数传入另一个函数
# def add(x, y, f):
#     return f(x) + f(y)
#
# print add(-1, -5, abs)

# map 接收两个参数：函数、序列
# print map(abs, (-1, -2, -3))
# reduce 接收两个参数：函数(要能接收两个参数)、序列
# def add(x, y):
#     return str(x) + str(y)
#
# print reduce(add, [x for x in range(10) if x % 2 != 0])
# 整合map和reduce 并使用lambda简化代码
# str2int
# dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# print reduce(lambda x, y: x * 10 + y, map(lambda s: dic[s], '13579'))
# 练习1
# def upperFirst(s):
#     if not isinstance(s, str) or len(s) == 0:
#         return s
#     return s[0].upper() + s[1:]
#
# print map(upperFirst, ['adam', 'LISA', 'barT', 123, ''])
# 练习2
# print reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

# filter
# print filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', ' '])
# 练习
# def isNotPrime(n):
#     if n == 1:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return True
#     return False
#
# print filter(isNotPrime, range(1, 101))

# 排序
# print sorted([36, 5, 12, 9, 21])
# print sorted([36, 5, 12, 9, 21], lambda x, y: -cmp(x, y))
# print sorted(['bob', 'about', 'Zoo', 'Credit'])
# 忽略大小写比较
# print sorted(['bob', 'about', 'Zoo', 'Credit'], lambda s1, s2: cmp(s1.upper(), s2.upper()))

# 函数作为返回值
# def lazy_sum(*args):
#     def sum_number():
#         sm = 0
#         for n in args:
#             sm += n
#         return sm
#     return sum_number
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print f()

# 闭包
# def count_num():
#     fs = []
#     for i in range(1, 4):
#         def f(n):
#             return lambda: n * n
#         fs.append(f(i))
#     return fs
#
# f1, f2, f3 = count_num()
# print f1()
# print f2()
# print f3()

# 装饰器 引入functools解决now函数的__name__被修改成wrapper的问题
# import datetime
# import functools
# def log(text='execute'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log()
# def now():
#     print datetime.datetime.now()
#
# now()

# 偏函数
# print int('101', base=2)
# def int2(x, base=2):
#     return int(x, base)
#
# print int2('1001')
# import functools
# int2_new = functools.partial(int, base=2)
# int2_new2 = lambda x, base=2: int(x, base)
# print int2_new('10101')
# print int2_new2('101')

# 别名
# try:
#     import cStringIO as StringIO
# except ImportError:
#     import StringIO

# try:
#     import json # python >= 2.6
# except ImportError:
#     import simplejson as json # python <= 2.5

# 利用__future__做版本兼容
# from __future__ import unicode_literals
# print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# print '\'xxx\' is str?', isinstance('xxx', str)
# print 'b\'xxx\' is str?', isinstance(b'xxx', str)

# 类名要大写 (object)表示继承自object
# __name 在类的外部无法访问
# szh.sex = 'nan'可以给实例动态增加属性
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print '%s: %s' % (self.__name, self.__score)
#
# szh = Student('szh', 100)
# szh.score = 99
# szh.sex = 'nan'
# szh.name = 'Sun Zehua'
# szh.print_score()
# print szh.sex

# zzq = Student('hbb', 95)
# print zzq.sex

# 继承
# class Animal(object):
#     def run(self):
#         print 'Animall is running'
#
# class Dog(Animal):
#     def run(self):
#         print 'Dog is running'
#
# class Cat(Animal):
#     def run(self):
#         print 'Cat is running'
#
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
#
# print isinstance(dog, Animal)
# print type(cat) == Cat
# import types
# print type('abc') == types.StringType
# dir类似于C#的反射
# print dir(cat)
# print hasattr(cat, 'run')
# r = getattr(cat, 'run')
# print r()


# class Student(object):
#     pass
#
# s = Student()
# 动态绑定一个属性
# s.name = 'Michael'
# print s.name
#
# def set_age(self, age):
#     self.age = age
# 绑定方法 这种方式只能给一个实例绑定，对Student的其它实例不生效
# from types import MethodType
# s.set_age = MethodType(set_age, s, Student)
# s.set_age(25)
# print s.age

# 给所有实例绑定方法
# Student.set_age = MethodType(set_age, None, Student)
# s2 = Student()
# s2.set_age(55)
# print s2.age

# 使用__slots__可以限制能够动态添加的属性，__slots__只对当前类生效，对子类不生效
# class Student(object):
#     __slots__ = ('name', 'age')
#
# s = Student()
# s.name = 'hbb'
# s.age = 1
# s.score = 100 # 出错
#
# class GraduateStudent(Student):
#     pass
# s2 = GraduateStudent()
# s2.score = 0 # __slots__不生效
#
# class GoodStudent(Student):
#     __slots__ = ('score', 'sex')
#
# s3 = GoodStudent()
# s3.name = 'szh'
# s3.sex = 'nan'
# s3.city = 'js' # 出错，子类如果也有__slots__则范围则是父类和子类的并集

# 通过get set方法限制属性的范围和对参数进行检查
# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.set_score(60)
# print s.get_score()

# 上面的方法调用起来略显复杂，可以使用@property来进行简化
# 使用了@property后自动创建了另一个装饰器@get函数的名称.setter
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#     @property
#     def age(self):
#         return 20
#
# s = Student()
# s.score = 77
# print s.score
# s.age = 20 # age是只读属性

# 多重继承 多重继承的方式被称为Mixin
# class Animal(object):
#     pass
# 大类
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
# 各种动物
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
# 要给动物加上Runnable和Flyable的功能，则定义Runnable和Flyable的类
# class Runnable(object):
#     def run(self):
#         print 'Running...'
#
# class Flyable(object):
#     def fly(self):
#         print 'Flying...'

# 对于需要Runnable的动物，则多继承一个Runnable，如Cat
# class Cat(Mammal, Runnable):
#     pass

# 对于需要Flyable的动物，则多继承一个Flyable，如Eagle
# class Eagle(Bird, Flyable):
#     pass

# 一些定制类

# __len__
# class TestLen(object):
#     def __len__(self):
#         return 10
#
# tlen = TestLen()
# print len(tlen)

# __str__返回用户看到的字符串，__repr__返回程序开发者看到字符串，通常__str__和__repr__代码是一样的
# 可以使用__repr__ = __str__来赋值__repr__
# class TestStr(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'TestStr object (name: %s)' % self.name
#     __repr__ = __str__
# print TestStr('Michael')

# __iter__ 如果一个类想被用于for...in循环，则必须实现__iter__方法
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print n

# __getitem__ 如果实现了__iter__虽然能作用于for循环，和list有点像，但没办法像list一样取其中某个元素，
# 要能像list的一样根据下标取元素，就必须实现__getitem__方法
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# print Fib()[20]

# 光实现__getitem__是没办法使用list的切片方法的，例如range(100)[5:100]
# 因为__getitem__传入的参数可能是int，也可能是一个切片对象slice
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start, stop = n.start, n.stop
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# print Fib()[:10]
# 以上没法做到Fib()[:10:2]，所以想要实现一个完整的__getitem__还有很多工作要做