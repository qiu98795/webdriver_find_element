from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)
# driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_name("wd").send_keys("Selenium")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()