# 调用自己写的类和方法
from LoginClass import *
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/upload/forum.php")
driver.implicitly_wait(10)

# 类名要加括号
Login().user_login(driver)
sleep(3)
Login().user_logout(driver)
sleep(2)

driver.quit()