'''
XPath即为XML路径语言，它是一种用来确定XML文档中某部分
位置的语言。XPath基于XML的树状结构，提供在数据结构中
找寻节点的能力。
'''
# 浏览器F12,选中元素后右键复制XPath路径即可，也可自己写
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

# 绝对路径
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("Selenium")

# 利用元素熟悉定位--定位到input标签中为kw的元素
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("Selenium")

# 定位input标签中name属性为wd的元素
# driver.find_element_by_xpath("//input[@name='wd']").send_keys("Selenium")

# 定位所有标签元素中，class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Selenium")
sleep(2)

driver.find_element_by_id("su").click()
sleep(2)
driver.quit()