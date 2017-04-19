# coding=utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
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
# msg = MIMEMultipart()
# 如果有的设备不支持查看HTML，那么就需要在提供HTML的同时再附加一个纯文本
# 这样，在无法查看HTML时可以自动降级查看纯文本
# MIMEMUltipart的subtype是alternative
msg = MIMEMultipart('alternative')
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
# msg.attach(mainbody)
# 如果想把图片嵌入到正文中，直接链接图片地址是行不通的，需要先把图片作为附件添加进去，再在HTML中通过引用src="cid:0"
# 就可以把附件图片嵌入到正文了，如果有多个图片，则给它们以依次编号，然后引用不同的cid:x
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
# 添加附件，一个本地图片
fname = 'verification_code.jpeg'
with open(fname, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型
    mimebase = MIMEBase('image', 'png', filename=fname)
    # 必要的头信息
    mimebase.add_header('Content-Disposition', 'attachment', filename=fname)
    mimebase.add_header('Content-ID', '<0>')
    mimebase.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mimebase.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mimebase)
    # 添加到 MIMEMultipart
    msg.attach(mimebase)

# 一般的smtp服务器的端口是25，qq、gmail邮箱是587
server = smtplib.SMTP(smtp_server, 587)
# qq、gmail要创建SSL安全连接
server.starttls()
server.set_debuglevel(1)
server.login(from_adr, password)
server.sendmail(from_adr, [to_addr], msg.as_string())
server.quit()