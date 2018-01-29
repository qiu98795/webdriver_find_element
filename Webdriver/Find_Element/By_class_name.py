from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)
driver.find_element_by_class_name("s_ipt").send_keys("Selenium")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()
