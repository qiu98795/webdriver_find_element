'''
数据驱动测试：
模块驱动的模型虽然解决了脚本重复的问题，但是需要测试不同数据的用例时，模块驱动
的方式就不很合适了。数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测
试结果的改变。装载数据的方式可以是列表、字典或是外部文件（txt、csv、xml、
excel），目的就是实现数据和脚本的分离
'''
from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_css_selector("#ls_username").clear()
        driver.find_element_by_css_selector("#ls_username").send_keys(username)

        driver.find_element_by_css_selector("#ls_password").clear()
        driver.find_element_by_css_selector("#ls_password").send_keys(password)

        driver.find_element_by_css_selector('[type="submit"]').click()

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(3)