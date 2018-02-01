'''
鼠标操作实现思路：
1.需要引入ActionChains
2.定位相关元素
3.在ActionChains（）.调用相关鼠标操作方法
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector('#kw').send_keys("Selenium")

# 获取搜索框对象
element=driver.find_element_by_css_selector('#kw')
sleep(3)

# 双击操作
ActionChains(driver).double_click(element).perform()
sleep(2)

# 右键操作
ActionChains(driver).context_click(element).perform()
sleep(2)

# 鼠标悬停
above=driver.find_element_by_css_selector('.pf')
ActionChains(driver).move_to_element(above).perform()

sleep(3)
driver.quit()