'''
测试报告美化：
下载后也需要修改，然后放置在Python安装路径的Lib文件夹里
主要不一样的点是导入“BSTestRunner”模块。
'''
import unittest
from BSTestRunner import BSTestRunner
import time

test_dir="./test_case"

discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    report_dir="./test_report"
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+"/"+now+"result.html"

    with open(report_name,"wb")as f:
        runner=BSTestRunner(stream=f,title="Test report",description="Test case result")
        runner.run(discover)
    f.close()