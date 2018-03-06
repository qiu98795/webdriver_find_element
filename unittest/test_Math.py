# 对Math类进行单元测试
# 重点：测试用例的方法名一定要是test开头，否则不被执行
from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)#断言方法有很多，可以自己多去网上查，了解一下。
        # 用例失败场景
        # self.assertEqual(j.add(), 13)
        print("=====================")

    def tearDown(self):
        print("test end")

# 调试时选中“下面一条代码”或者直接用“cmd控制台”，不然有可能出错
if __name__=='__main__':

    # 构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add"))

    # 执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)