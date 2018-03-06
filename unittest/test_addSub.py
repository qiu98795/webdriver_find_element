# 新增测试用例管理
# 重点：测试用例的方法名一定要是test开头，否则不被执行
from calculator import *
import unittest

class Test_add(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_add1(self):
        j=Math(10,10)
        self.assertEqual(j.add(),20)

    def test_add2(self):
        j = Math(15, 15)
        self.assertEqual(j.add(),30)

class Test_sub(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_sub1(self):
        i=Math(8,8)
        self.assertEqual(i.sub(),0)

    def test_sub2(self):
        i = Math(10, 8)
        self.assertEqual(i.sub(), 2)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_add("test_add2"))
    suite.addTest(Test_sub("test_sub1"))
    suite.addTest(Test_sub("test_sub2"))

    runner=unittest.TextTestRunner()
    runner.run(suite)