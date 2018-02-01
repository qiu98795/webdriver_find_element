# 多窗口切换操作
'''
案例：打开百度首页，然后搜“搜狗引擎”转向搜狗，再回到百度首页
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

# 获取百度首页的句柄，这里相当于给此页面下“标记”
baidu_index=driver.current_window_handle
sleep(2)

driver.find_element_by_css_selector("#kw").send_keys("搜狗引擎")
sleep(2)

driver.find_element_by_partial_link_text("上网从搜狗开始").click()
sleep(3)

# 跳转回到百度首页
driver.switch_to.window(baidu_index)
sleep(3)
driver.find_element_by_css_selector("#kw").send_keys("Selenium")
sleep(2)

driver.quit()