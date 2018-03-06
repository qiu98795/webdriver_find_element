# 数据驱动调用--实现多个账户登录
from LoginClass_para import *
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/upload/forum.php")
driver.implicitly_wait(10)

Login().user_login(driver,"qiu98795",456852)
sleep(3)
Login().user_logout(driver)
sleep(2)

Login().user_login(driver,"qiu98795plus","q456852")
sleep(3)
Login().user_logout(driver)
sleep(2)

driver.quit()