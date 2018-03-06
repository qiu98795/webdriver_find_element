'''
Python邮件发送；
smtplib模块：
Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责
发送邮件。
注意：使用前需要开启SMTP服务
案例：使用163邮箱来结合smtp模块发送邮件
'''
import smtplib                      #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header         #定义邮件标题

#发送邮箱服务器
smtpserver="smtp.163.com"

# 发送邮箱用户名和密码**密码是授权码
user="13682397784@163.com"
password="456852q"

# 发送和接收邮箱
sender="13682397784@163.com"
receive="724487680@qq.com"

# 发送邮件主题和内容
subject="Web Selenium 自动化测试报告"
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

# HTML邮件正文
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=receive

# SSL协议端口号要使用465
smtp=smtplib.SMTP_SSL(smtpserver,465)

# 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录邮箱服务器用户名和授权码
smtp.login(user,password)

# 如果包含一些不被认可的字符可能会被定义为垃圾邮件
print("开始发送邮件...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("邮件发送完成！")