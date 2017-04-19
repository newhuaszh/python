# coding=utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

# 格式化邮件的地址，不能简单地传入name <addr@example.com>。如果包含中文，则需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_adr = raw_input('From:')
password = raw_input('Password:')
to_addr = raw_input('To:')
smtp_server = raw_input('SMTP server:')

# 如果要添加附件，则使用MIMEMultipart，再构造一个MIMEText作为邮件正文
msg = MIMEMultipart()
# 如果要发送HTML邮件，而不是普通的纯文本文件怎么办？
# 在构造MIMEText对象时，传入HTML字符串，把第二个参数由plain改为html即可
# 如
mainbody = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_adr)
# 如果有多个邮件地址，则用,分隔
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候', 'utf-8').encode()
# 添加正文
msg.attach(mainbody)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_adr, password)
server.sendmail(from_adr, [to_addr], msg.as_string())
server.quit()