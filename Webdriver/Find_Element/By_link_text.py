# link_text定位就是根据超链接文字进行定位
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
sleep(2)
#此方法“文字”要完全匹配
driver.find_element_by_link_text("新闻").click()
sleep(2)
#此方法只要匹配部分“文字”
driver.find_element_by_partial_link_text("个性").click()
sleep(2)
driver.quit()