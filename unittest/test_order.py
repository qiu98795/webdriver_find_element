'''
测试用例执行顺序:
在使用unittest.main（）执行所有用例时，测试类或测试方法的顺序跟数字
与字母顺序0--9，A--Z
如果想突破这个顺序，我们可以使用suite=unittest.TestSuite()******
suite.addTest()逐个添加自己想要测试的用例，用例就会按照添加的顺序执行
*重点：如果在PyCharm里没有按照自己添加的排序执行，我们就直接使用cmd
命令控制台执行python文件，这样可以解决问题。 这个是由版本引起的问题
'''
import unittest

class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1 start")

    def tearDown(self):
        print("Test1 end")

    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")


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
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Test2("test_d"))
    suite.addTest(Test1("test_c"))
    suite.addTest(Test2("test_a"))
    suite.addTest(Test1("test_b"))

    runner=unittest.TextTestRunner()
    runner.run(suite)