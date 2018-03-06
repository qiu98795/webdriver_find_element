# unittest Web测试应用实战
from selenium import webdriver
from time import sleep
import unittest

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        driver=self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium自学网")
        driver.find_element_by_id("su").click()
        sleep(3)

        title="Selenium自学网_百度搜索"
        self.assertEqual(title,"Selenium自学网_百度搜索")

        driver.find_element_by_partial_link_text("Selenium自动化测试").click()
        sleep(3)

if __name__ == '__main__':
    unittest.main()

