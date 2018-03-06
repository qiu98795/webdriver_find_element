import unittest
from test_case.model.function import *
from BSTestRunner import BSTestRunner
import time

# 这个相对路径在cmd命令窗口会报错（找不到启动目录），建议可以直接使用绝对路径
report_dir=r'D:\Users\AutoTest_project\Website\test_report'
test_dir=r'D:\Users\AutoTest_project\Website\test_case'

print("start run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'

print("start write report..")
#运行前记得把BSTestrunner.py 120 行‘unicode’换成‘str’
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="Test Report",description="localhost login test")
    runner.run(discover)
    f.close()

print("find latest report")
latest_report=latest_report(report_dir)

print("find latest report")
send_mail(latest_report)

print("Test end")