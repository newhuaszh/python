# coding=utf-8
from email.mime.text import MIMEText
import smtplib

'''
参数1：邮件正文
参数2：MIME的subtype，传入'plain', 最终的MIME就是'text/plain'
参数3：用utf-8保证多语言的兼容性
'''
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = raw_input('From:')
password = raw_input('Password:')
smtp_server = raw_input('SMTP server:')
to_addr = raw_input('To:')

server = smtplib.SMTP(smtp_server, 25)
# set_debuglevel(1)可以打印和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# login()登录SMTP服务器
server.login(from_addr, password)
# sendmail()就是发邮件，由于可以发给多个人，所以第二个参数是一个list，邮件正文是str，所有要用as_string()把MIMEText对象转成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()