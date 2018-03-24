from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('Hello, This message was sent by Python.\n吴远航大帅哥！！！！', 'plain', 'utf-8')
msg['From'] = _format_addr('你的超级大粉丝Sam Du <%s>' % from_addr)
msg['To'] = _format_addr('吴远航 <%s>' % to_addr)
msg['Subject'] = Header('来自 Sam Du PyCharm的粉丝来信...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
