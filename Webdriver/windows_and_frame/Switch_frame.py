# frame嵌套页面元素定位
# 案例：在Frame.html文件中定位搜狗搜索页面，进行搜索操作
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
# 设置网页文件路径，r代表路径转义
file_path=r"D:\Users\Webdriver\Frame.html"
# 路径转义另一种写法
# file_path="D:\\Users\\Webdriver\\Frame.html"
driver.get(file_path)

#***切换到frame页面内,search是id属性
# driver.switch_to_frame("search")此方法已过时
driver.switch_to.frame("search")

#定位到搜索框按钮输入关键字
driver.find_element_by_css_selector("#query").send_keys("Selenium")
sleep(2)

driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()