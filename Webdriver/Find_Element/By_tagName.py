#用tag_name定位元素，其实就是用html里的的标签名来定位。
# 因为标签名容易重复，所以视情况来用
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")
sleep(2)
# driver.find_element_by_tag_name("input").send_keys("Selenium")
driver.find_elements_by_tag_name("input")[0].send_keys("Selenium")
sleep(2)

driver.quit()