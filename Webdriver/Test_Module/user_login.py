'''
线性模型：线性脚本中每个脚本都互相独立，且不会产生其他依赖与调用，其实就是简
单模拟用户某个操作流程的脚本
案例：在WampServer软件设置主页，实行自动登录和退出操作
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/upload/forum.php")

# 输入用户名
driver.find_element_by_css_selector("#ls_username").clear()
driver.find_element_by_css_selector("#ls_username").send_keys("qiu98795")

# 输入密码
driver.find_element_by_css_selector("#ls_password").clear()
driver.find_element_by_css_selector("#ls_password").send_keys("456852")

# 点击登录
driver.find_element_by_css_selector('[type="submit"]').click()
sleep(3)

# 退出
driver.find_element_by_link_text("退出").click()
sleep(6)

driver.quit()
