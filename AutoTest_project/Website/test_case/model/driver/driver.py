#浏览器driver定义
from selenium import webdriver

#启动浏览器驱动
def browser():
    # driver =webdriver.Firefox()
    # driver =webdriver.Chrome()
    # driver =webdriver.Ie()
    driver=webdriver.PhantomJS()#无头浏览器

    # driver.get("http://www.baidu.com")

    return driver

#测试运行
if __name__ == '__main__':
    browser()