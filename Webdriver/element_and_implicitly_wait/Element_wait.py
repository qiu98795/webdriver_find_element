'''
原理：显式等待,就是明确的要等到某个元素的出现或者是某个元素的可
点击等条件,等不到,就一直等,除非在规定的时间之内都没找到,那么就
跳出Exception.(简而言之：就是直到元素出现才去操作，如果超时则报异常)
'''
'''
1.WebDriverWait 显示等待针对元素必用
2.expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）
3.NoSuchElementException 用于隐式等待抛出异常
4.By 用于元素定位
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait    #注意大小写
from selenium.webdriver.support import expected_conditions as EC  #给expected_conditions取个别名EC，防止代码冗余
from time import sleep  #sleep是强制等待

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#kw").send_keys("Selenium")
sleep(2)

#WebDriverWait()方法后面跟三个参数（驱动对象，最长等待时间，搜索元素间隔的时间）
#EC.presence_of_element_located（（）） 这个方法比较特殊，后面是跟两个小括号
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"su")))
element.click()
sleep(2)

driver.quit()