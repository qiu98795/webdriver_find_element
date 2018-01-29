from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)

# 利用Select类来进行定位
select=Select(driver.find_element_by_css_selector('[name="CookieDate"]'))

# 通过下标
# select.select_by_index(2)

# 通过文本信息
# select.select_by_visible_text("留一年")

# 通过value值
select.select_by_value("1")

sleep(2)
driver.quit()