'''
Selenium极力推荐使用css定位，而不是XPath来定位元素，原因是css定位
比XPath定位速度快，语法也更加简洁
'''
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

# 根据id来定位
# driver.find_element_by_css_selector('#kw').send_keys("Selenium")

# 根据class定位
# driver.find_element_by_css_selector('.s_ipt').send_keys("Selenium")

# 通过属性来定位,中括号外面用双引号，里面就用单引号或者相反
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("Selenium")

# 通过元素层级来定位
driver.find_element_by_css_selector('form.fm>span>input').send_keys("Selenium")

driver.find_element_by_id('su').click()
sleep(2)
driver.quit()