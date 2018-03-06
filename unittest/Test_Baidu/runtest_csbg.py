'''
自动化测试执行完成之后，我们需要生成测试报告来查看测试结果，使用
HTMLTestRunner模块可以直接生成Html格式的报告。
'''
# 下载地址
# http://tungwaiyip.info/software/HTMLTestRunner.html
# 下载后要经过修改才可以使用，因为版本原因（可以上网自己去了解）
# 将修改完成的模块存放在Python路径下Lib目录里面即可
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

# 定义测试用例路径
test_dir="./test_case"
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    # 存放报告的文件夹
    report_dir="./test_report"
    # 报告命名时间格式化
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告文件完整路径
    report_name=report_dir+'/'+now+'result.html'

    # 打开文件在报告文件写入测试结果
    with open(report_name,'wb')as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description='Test case result')
        runner.run(discover)
    f.close()