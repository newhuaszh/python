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

# 使用__getattr__，可以在调用不存在的属性时进行相应的返回，不光返回值，还可以返回函数（使用lambda）
# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, item):
#         if item == 'score':
#             return 99
#         if item == 'age':
#             return lambda num: num * num
#
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
#
#
# s = Student()
# print s.name
# print s.score
# print s.age(6)
# print s.abc # __getattr__默认返回的是None

# __getattr__的用途：链式调用
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         if path == 'users':
#             return lambda name: Chain('%s/%s' % (path, name))
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path

# print Chain().status.user.timeline.list
# GET /users/:user/repos 实际调用时需要把:user替换为实际用户名
# print Chain().users('michael').repos

# __call__，一个类如果定义了__call__，则此类的实例可以被当做函数一样调用，__call__还可以定义参数
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print 'My name is %s' % self.name
#
# s = Student('szh')
# s()

# 使用元类
# class Hello(object):
#     def hello(self, name='world'):
#         print 'Hello, %s' % name
#
# h = Hello()
# h.hello()
# print type(Hello) # Hello是一个class，它的类型是type
# print type(h) # h是一个实例，它的类型是class Hello

# type()不仅可以返回一个对象的类型，还可以创建出新的类型
# def fn(self, name='world'):
#     print 'Hello, %s' % name
# dict(fnHello=fn)可以写成{'fnHello': fn}
# CNew = type('ClassHello', (object,), dict(fnHello=fn)) # 第二个参数是一个元组，注意单个元素元组的写法(xxx,)，逗号别忘了。这里fnHello=fn可以用lambda简化。
#
# h2 = CNew() # 疑问：CNew 与 ClassHello的关系是？
# h2.fnHello()

# 使用metaclass来修改类的定义，有点像C#的扩展方法
# class ListMetaclass(type):
#     # cls:当前准备创建的类的对象
#     # name:类的名字
#     # bases:类继承的父类集合
#     # attrs:类的方法集合
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
# class MyList(list):
#     __metaclass__ = ListMetaclass
#
# L = MyList()
# L.add(1)
# print L

# ORM中需要用到metaclass
# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         mappings = dict()
#         for k, v in attrs.iteritems():
#             if isinstance(v, Field):
#                 print 'Found mapping:%s=>%s' % (k, v)
#                 mappings[k] = v
#         for k in mappings.iterkeys():
#             attrs.pop(k)
#         attrs['__table__'] = name
#         attrs['__mappings__'] = mappings
#         return type.__new__(cls, name, bases, attrs)
#
# class Model(dict):
#     __metaclass__ = ModelMetaclass
#
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" & key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.iteritems():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print 'SQL: %s' % sql
#         print 'ARGS: %s' % str(args)
#
# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u.save()

# 错误处理
# try:
#     print 'try...'
#     r = 10 / 0
#     print 'result:', r
# except ZeroDivisionError, e:
#     print 'except:', e
# except ValueError, e:
#     print 'ValueError', e
# else:
#     print 'no error!'
# finally:
#     print 'finally...'
# print 'END'

# 使用logging模块打印堆栈
# import logging
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except StandardError, e:
#         logging.exception(e)
#
# main()
# print 'END'

# 使用raise抛出异常，尽量使用python内置的异常类型
# class FooError(StandardError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')

# 捕获并抛出异常
# def foo(s):
#     n = int(s)
#     return 10 / n
#
# def bar(s):
#     try:
#         return foo(s) * 2
#     except StandardError, e:
#         print 'Error!'
#         raise # raise如果不带参数，则会把当前异常原样抛出; raise ValueError('input error')，把异常类型进行转化
#
# def main():
#     bar('0')
#
# main()

# 调试
# 1.使用print，但程序发布前得删掉

# 2.使用assert，虽然也会导致assert到处都是，但启用Python解释器时可以用-O参数来关闭assert，关闭后所有的assert相当于pass
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is 0' # assert后第一个参数为False，第二个参数才执行；assert会抛出AssertionError
#     return 10 / n
#
# foo('0')

# 3.使用logging，可以输出到控制台、文件
# import logging
# logging.basicConfig(level=logging.INFO) #logging可以指定记录信息的级别，有debug,info,warning,error
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print 10 / n

# 4.使用pdb
# s = '0'
# n = int(s)
# print 10 / n

# 单元测试
# 可以使用python mydict_test.py进行单元测试
# 也可以使用python -m unittest mydict_test来直接运行单元测试，这是推荐做法，因为可以一次批量运行很多单元测试
# setUp() 和 tearDown() 函数在每个测试方法调用前后分别被执行，通常用来减少测试方法中的重复代码，比如说在
# setUP()中连接数据库，在tearDown()关闭数据库

# 文档测试，文档可以使用doctest提取出来运行
# def abs(n):
#     '''
#     Function to get absolute value of number.
#
#     Example:
#
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n >= 0 else (-n)

# 文件读写
# f = open(r'D:\Download\无限开挂.txt'.decode('utf-8'), 'r')
# try:
#     f = open(r'D:\Download\test2.txt'.decode('utf-8'), 'r')
#     print f.read()
# except IOError, e:
#     print '打开错误'
# finally:
#     if f:
#         f.close()
# with open(r'C:\Users\Sun Zehua\Downloads\test.txt'.decode('utf-8'), 'rb') as f:
#     print f.read().decode('gbk')
# 如果文件很大，使用read()会爆内存。为了保险起见，可以使用read(size)方法，使用readline()读取一行，readlines()一次读取所有内容并按行返回
# readlines()比较适合用在配置文件上
# with open(r'C:\Users\Sun Zehua\Downloads\test.txt'.decode('utf-8'), 'r') as f:
#     for line in f.readlines():
#         print line.strip().decode('gbk', 'utf-8')
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
# 空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没
# 有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
# 所以，还是用with语句来得保险。

# import os
# nt:windows系统 posix:Linux、Unix或MacOS
# print os.name
# uname()函数获取详细的系统信息，但在windows上不提供，所以os模块的有些函数是跟操作系统相关的
# print os.uname()
# 环境变量
# print os.environ
# 获取某个环境变量的值
# print os.getenv('path')
# 查看当前目录的绝对路径
# print os.path.abspath('.').decode('gbk')
# 在当前目录下创建文件夹testDir
# 两个路径合并时，最好用join，因为不同系统的连接符不一样，有的是\，有的是/
# strDir = os.path.join(os.path.abspath('.'), 'testDir')
# os.mkdir(strDir)
# 删除一个目录
# os.rmdir(strDir)
# 拆分路径时用split，同样是为了避免不同系统间的差异，用了split后，可以把路径拆为两部分，后一部分总是最后级别的目录或文件名
# print os.path.split(strDir)
# 对文件重命名
# os.rename(r'C:\Users\Sun Zehua\Downloads\test.txt', r'C:\Users\Sun Zehua\Downloads\test2.txt')
# os.remove(r'C:\Users\Sun Zehua\Downloads\test2.txt')
# 但os模块中没有提供复制文件的函数，复制文件的函数在shutil模块中
# import shutil
# shutil.copyfile(r'C:\Users\Sun Zehua\Downloads\test.txt', r'C:\Users\Sun Zehua\Downloads\test2.txt')
# 列出当前目录下的所有文件夹
# print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出当前目录下的所有的.py文件
# print [x for x in os.listdir('.') if os.path.isfile(x) and x.endswith('.py')]
# 或
# print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# 注意是splittext，而不是split

# dict的序列化
# d = dict(name='szh', age=29, score=99)
# d['age'] = 30
# print d
#
# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle

# print pickle.dumps(d)

# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)
#
# with open('dump.txt', 'rb') as f:
#     d2 = pickle.load(f)
#     print d2
# pickle只能在python中使用，可能不同python版本间都不兼容
# 只能用pickle保存一些不重要的数据，不能成功反序列化也没关系
# 要想在不同编程语言之间传递，可以使用XML，但更推荐使用JSON。JSON更快，可以直接在web页面读取

# JSON类型    Python类型
# {}          dict
# []          list
# "string"    'str' 或 u'unicode'
# 1234.56     int 或 float
# true/false  True/False
# null        None

# import json
# d = dict(name='szh', age=29, score=99)
# print d
# print json.dumps(d) # 注意json的内容都是双引号，而dict是单引号
# json_str = '{"age": 30, "score": 100, "name": "zzq"}'
# print json.loads(json_str) # 注意反序列后得到字符串对象默认都是unicode而不是str，JSON编码是utf-8

# 类的序列化
# import json
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('szh', 1, 0)
# def std2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
# print json.dumps(s, default=std2dict)
# 可以用lambda来简化
# print json.dumps(s, default=lambda std: {'name': std.name, 'age': std.age, 'score': std.score})
# 可以使用__dict__，把任意class实例转化为dict，除了定义了__slots__的class
# print json.dumps(s, default=lambda std: std.__dict__)
# JSON反序列化
# json_str = '{"age": 30, "score": 100, "name": "zzq"}'
# def dict2std(d):
#     return Student(d['name'], d['age'], d['score'])
#
# print json.loads(json_str, object_hook=dict2std)
# 使用lambda简化
# print json.loads(json_str, object_hook=lambda d: Student(d['name'], d['age'], d['score']))

# 多进程
# import os
# print os.getpid()
# print os.fork() # fork在windows下不可用
# multiprocessing是在Unix、Linux、MacOS、Windows下都通用的多进程模块
# multiprocessing提供一个Process类代表一个进程对象
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print 'Run child process %s (%s)...' % (name, os.getpid())
#
# if __name__ == '__main__':
#     print 'Parent process %s' % os.getpid()
#     p = Process(target=run_proc, args=('test',))
#     print 'Process will start'
#     p.start()
#     p.join() # 等待子进程结束，用于进程间同步
#     print 'Process end'

# 如果要启动大量子进程，可以使用Pool进程池的方式批量创建子进程
# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#     print 'Run task %s (%s)' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds' % (name, end - start)
#
# if __name__ == '__main__':
#     print 'Parent process %s' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close() # 调用join()前必须调用close()，调用close()后就不能继续添加新的Process了
#     p.join()  # join()会等待所有子进程执行完毕
#     print 'All subprocesses done'
# 从输出结果可以看到，task 0,1,2,3是立刻执行的，而task 4要等待前面某个task执行完毕才能执行
# 这是因为，Pool的默认大小在我的电脑上时4（默认是cpu的核数），因此最多同时执行4个进程
# 这是Pool有意设计的限制，不是操作系统的限制
# 可以通过p = Pool(5)的方式，同时跑5个进程

# 进程间通信
# multiprocessing模块包装了操作系统底层的机制，提供了Queue、Pipes等方式来交换数据
# from multiprocessing import Process, Queue
# import os, time, random

# 写数据进程
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())
# 读数据进程
# def read(q):
#     while q:
#         value = q.get(True) # 为空时一直等待
#         print 'Get %s from queue' % value
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传递给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动写
#     pw.start()
#     # 启动读
#     pr.start()
#     # 等待写结束
#     pw.join()
#     # 读进程是死循环，强行结束
#     pr.terminate()

# 多线程
# pyhton的线程是Posix Thread，而不是虚拟出来的线程
# python标准库提供了两个模块，thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装
# 绝大多数情况下，我们只需要使用threading这个模块
# import time, threading
# def loop():
#     print 'thread %s is running...' % threading.current_thread().name
#     n = 0
#     while n < 5:
#         n += 1
#         print 'thread %s >>> %s' % (threading.current_thread().name, n)
#         time.sleep(1)
#     print 'thread %s ended' % threading.current_thread().name
#
# print 'thread %s is running...' % threading.current_thread().name
# # newThread是创建的子线程的名字，如果不起名字，python会自动起Thread-1，Thread-2
# t = threading.Thread(target=loop, name='newThread')
# t.start()
# t.join()
# print 'thread %s ended' % threading.current_thread().name

# lock锁
# import time,threading
#
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     lock.acquire() # 为什么这里可以直接使用lock，不用先global？
#     try:
#         global balance
#         balance += n
#         balance -= n
#     finally:
#         lock.release()
#
# def run_thread(n):
#     for i in range(1000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# 死循环测试cpu占用
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# 利用多线程只能最多占满一个cpu，这是历史遗留问题，官方的解释器CPython执行代码时有个GIL锁，线程执行前，必须先获得GIL锁
# 然后每执行100条字节码，CPython就会自动释放GIL锁，让别的线程有机会执行。这个GIL锁实际上把所有线程的执行代码都给上了锁
# 所以，多线程在CPyhton中只能交替执行，即使100个线程跑在100核的cpu上，也只能用到1核
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# 利用多进程，可以占满cpu，因为每个进程的GIL锁是独立的，互不影响
# if __name__ == '__main__':
#     for i in range(multiprocessing.cpu_count()):
#         t = multiprocessing.Process(target=loop)
#         t.start()

# 多线程间的传值，利用全局dict以线程为key，存储对应的值
# import threading, time
# global_dict = {}
#
# def loop():
#     val = global_dict[threading.current_thread()]
#     time.sleep(1)
#     print val
#
# t1 = threading.Thread(target=loop)
# t2 = threading.Thread(target=loop)
# global_dict[t1] = 't1'
# global_dict[t2] = 't2'
# t1.start()
# t2.start()
# 上面这种方式还是比较麻烦，实际上ThreadLocal就是解决此问题的
# ThreadLocal里的属性对于不同线程来说是独立的
# ThreadLocal最常用的地方是为每个线程绑定一个数据库连接，http请求，用户身份信息等
# import threading
# local_school = threading.local()
#
# def process_student():
#     print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='ThreadA')
# t2 = threading.Thread(target=process_thread, args=('Bob,',), name='ThreadB')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# 分布式见 taskmanager.py、taskworker.py

# 正则表达式
# 匹配
# import re
#
# if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
#     print 'OK'
# else:
#     print 'Failed'
#
# if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
#     print 'OK'
# else:
#     print 'Failed'

# 切分字符串
# 传统的方式
# print 'a b   c'.split(' ')
# 正则表达式的方式
# print re.split(r'\s+', 'a b   c')
# print re.split(r'[\,\s]+', 'a,b, c   d')
# print re.split(r'[\;\,\s]+', 'a,b;;c   d')
# 分组
# m = re.match(r'(\d{3})-(\d{3,8})', '010-12345')
# print m.group(0)
# print m.group(1)
# print m.group(2)
# 默认贪婪匹配
# print re.match(r'^(\d+)(0*)$', '102300').groups()
# 加个?可以变成非贪婪匹配
# print re.match(r'^(\d+?)(0*)$', '102300').groups()
# 如果一个正则表达式要重复使用很多次，我们需要预编译正则表达式，接下来重复使用时就不需要编译这个步骤了，可以直接匹配
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print re_telephone.match('010-12345').groups()
import re
re_content = re.compile(r'\s*<data name=\"[a-zA-Z\_$][0-9a-zA-Z\_]*.(Text|Tooltip)\" xml:space=\"preserve\"\s*')
if re_content.match('  <data name="ribbonBar1.Text" xml:space="preserve"> '):
    print 'OK'
else:
    print 'NO'

if re_content.match('  <data name="btnFastPhoto.Tooltip" xml:space="preserve">  '):
    print 'OK'
else:
    print NO

