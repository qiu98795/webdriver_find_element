# Python邮件同时发送多人
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver="smtp.163.com"

user="13682397784@163.com"
password="456852q"

sender="13682397784@163.com"
# 输入你要发送的多个邮箱
receives=["q13682397784@126.com","13682397784@sina.cn"]

subject="Web Selenium 自动化测试报告"
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=",".join(receives)    #这里是以逗号分隔，并加入的意思

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("start send email...")
smtp.sendmail(sender,receives,msg.as_string())
smtp.quit()
print("send email end!")