'''
用例综合框架管理；
前面测试用例与执行都是写在一个文件，当用例数量不断增加的时候，用例的执行与管理
变得非常麻烦，因此需要对用例根据具体的功能模块来使用单独的模块来管理。就像一所
学校要根据不同年级进行分班管理，也是同样道理。
'''
import unittest

class Setup_tearDown(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")