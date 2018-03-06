from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#截图方法
def insert_img(driver,filename):
    #找到当前文件的路径
    func_path=os.path.dirname(__file__)
    print(func_path)

    #找到当前文件的上一层路径
    base_dir=os.path.dirname(func_path)
    print(base_dir)

    #转换成Str类型，然后把双斜杠，改成单“反斜杠”
    base_dir=str(base_dir)
    base_dir.replace("\\","/")
    print(base_dir)

    #以“/Website”来分割成列表形式，并且取下标为0的元素
    base=base_dir.split("/Website")[0]
    print(base)

    # 文件路径的重新组合，并且给文件取名
    # filepath=base+r"/Website/test_report/screenshot/"+filename
    # 因为当时相对路径，使用出了点问题，所以换成了绝对路径
    filepath = r"D:/Users/AutoTest_project/Website/test_report/screenshot/" + filename

    driver.get_screenshot_as_file(filepath)

#发送邮件方法
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

#查找最新报告的方法
def latest_report(report_dir):
    lists=os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
    print("the latest report is"+lists[-1])

    file=os.path.join(report_dir,lists[-1])
    print(file)
    return file


if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com/")
    insert_img(driver,"bai.jpg")
    driver.quit()