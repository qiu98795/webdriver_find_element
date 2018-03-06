'''
案例:将D:\Users\unittest\Test_Baidu生成的最新测试报告发送到指定邮箱
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import unittest
from BSTestRunner import BSTestRunner
import time
import os

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = "smtp.163.com"

    user = "13682397784@163.com"
    password = "456852q"

    sender = "13682397784@163.com"
    receives = ["q13682397784@126.com", "13682397784@sina.cn"]

    subject = "Web Selenium 自动化测试报告"

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ",".join(receives)  # 这里是以逗号分隔，并加入的意思

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("send email end!")

def latest_report(report_dir):
    lists=os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
    print("the latest report is"+lists[-1])

    file=os.path.join(report_dir,lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    report_dir = "./test_report"
    test_dir="./test_case"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + "/" + now + "result.html"

    with open(report_name, "wb")as f:
        runner = BSTestRunner(stream=f, title="Test report", description="Test case result")
        runner.run(discover)
    f.close()

    #获取最新测试报告
    latest_report=latest_report(report_dir)
    #发送邮件报告
    send_mail(latest_report)