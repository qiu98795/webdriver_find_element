# XPath的层级与逻辑定位
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

# 层级和属性结合定位--百度首页！此处input不按照数组下标，不需要从0开始算
# driver.find_element_by_xpath("//form[@name='f']/span/input[1]").send_keys("Selenium")

# 逻辑运算组合定位--在属性不唯一的时候可以使用
driver.find_element_by_xpath("//input[@name='wd' and @id='kw']").send_keys("Selenium")

sleep(2)
driver.quit()