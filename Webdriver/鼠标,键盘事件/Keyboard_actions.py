'''
键盘操作案列：
在百度搜索关键字“Python”，然后将关键词复制或剪切到搜狗搜索框进行搜索
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('#kw').send_keys("Python")
sleep(2)

# 键盘全选操作Ctrl+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
sleep(1)

# 键盘选择复制或剪切操作 Ctrl+C 或 Ctrl+X
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')
sleep(2)

# 打开搜狗页面
driver.get("http://www.sogou.com/")
sleep(2)

# 粘贴复制内容
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
sleep(2)

# 点击搜索按钮
driver.find_element_by_css_selector("#stb").click()

sleep(2)
driver.quit()