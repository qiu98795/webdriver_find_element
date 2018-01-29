from selenium import webdriver
from time import sleep

# 加载浏览器启动
driver=webdriver.Firefox()

# 打开一个网页
driver.get("http://www.baidu.com")
driver.maximize_window()#最大化浏览器
sleep(3)

# 打开另一个页面
driver.get("https://news.baidu.com/")
driver.set_window_size(400,400)#设置浏览器窗口大小
driver.refresh()#刷新页面，等于按F5
sleep(3)

driver.back()#返回上一页
sleep(2)

driver.forward()#返回下一页
sleep(3)

driver.quit()