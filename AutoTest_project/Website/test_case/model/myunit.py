#用例运行前后的环境准备工作
import unittest
from .driver.driver import *

class StarEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()