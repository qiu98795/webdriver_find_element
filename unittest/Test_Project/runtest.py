# 用例执行管理
import unittest

# 设置要测试的文件夹路径，可以使用相对路径，也可以使用绝对路径。注意转义
test_dir='./'

'''
这里给两个参数，测试的文件夹路径和要测试的模块，"test*.py"的意思是以
test开头，以'.py'结尾的模块。
'''
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discovery)