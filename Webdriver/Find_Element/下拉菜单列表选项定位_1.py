from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")

# 根据option标签来定位
# driver.find_elements_by_tag_name('option')[1].click()

# 根据属性来定位
driver.find_element_by_css_selector('[value="2"]').click()

sleep(2)
driver.quit()