# 用例公共部分合并
# 以下例子是假设初始化和善后工作是一样的情况，是可以合并的
# 这是一个设计理念，大家可以灵活使用。千万不要盲目使用
from calculator import *
import unittest

class Test_StarEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Testadd(Test_StarEnd):
    def test_add(self):
        j=Math(10,5)
        self.assertEqual(j.add(),15)

class TestSub(Test_StarEnd):
    def test_sub(self):
        i=Math(5,3)
        self.assertEqual(i.sub(),2)

if __name__ == '__main__':
    # 执行所有用例
    unittest.main()