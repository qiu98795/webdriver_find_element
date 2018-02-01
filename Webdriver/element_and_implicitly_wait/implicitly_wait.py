'''
原理：隐式等待，就是在创建driver时，为浏览器对象创建一个等待时间，这
个方法是得不到某个元素就等待一段时间，直到拿到某个元素位置。

'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)

driver.implicitly_wait(5)#隐式等待时间设定5秒

#检测搜索框是否存在
try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("Selenium")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(2)
driver.quit()