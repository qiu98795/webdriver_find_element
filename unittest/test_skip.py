'''
跳过测试和预期失败：
unittest.skip() 直接跳过测试
unittest.skipIf() 条件为真，跳过测试
unittest.skipUnless() 条件为假，跳过测试
unittest.expectedFailure 预期设置失败
**方法，要填类名或者方法名，这个视情况自己填
'''
# 把方法放在需要跳过的用例或者类上面即可，注意要对齐（缩进问题）
import unittest

class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1 start")

    def tearDown(self):
        print("Test1 end")
    # @unittest.skipIf(3>2,"skip test_c")
    @unittest.expectedFailure
    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")

@unittest.skip("skip Test_2")
class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")

    def tearDown(self):
        print("Test2 end")

    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")

if __name__ == '__main__':
    unittest.main()