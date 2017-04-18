# coding=utf-8
'''
摘要算法，又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
目的是为了判断原始数据是否被篡改
'''
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5_2 = hashlib.md5()
md5_2.update('how to use md5 in ')
md5_2.update('python hashlib?')
print md5_2.hexdigest()
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示
# 另一种场景的摘要算是SHA1，使用方式跟MD5一致
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()
# SHA1的结果是160bit字节，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长

# 摘要算法应用
#
# 摘要算法能应用到什么地方？举个常用例子：
#
# 任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
#
# name    | password
# --------+----------
# michael | 123456
# bob     | abc999
# alice   | alice2008
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
#
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
#
# username | password
# ---------+---------------------------------
# michael  | e10adc3949ba59abbe56e057f20f883e
# bob      | 878ef96e86145580c38c87f0410ad153
# alice    | 99b1c2188db85afee403b1536010c2c9
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。
#
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5_login = hashlib.md5()
    md5_login.update(password)
    if md5_login.hexdigest() == db[user]:
        print '验证通过'
    else:
        print '验证不通过'

login('michael', '123456')

# 由于常用口令的MD5值很容易被计算出来
