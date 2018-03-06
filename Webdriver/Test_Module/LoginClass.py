'''
模块化驱动测试：
线性模型虽然每个用例都可以拿出来独立运行，但是用例之间重复代码很多，开发维护
成本高。其实把重复的操作代码封装为独立的公共模块，当用例执行时需要用到这部分，
直接调用即可，这就是模块驱动的方式。比如登录系统、退出登录、截图函数等等。
'''
from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,driver):
        driver.find_element_by_css_selector("#ls_username").clear()
        driver.find_element_by_css_selector("#ls_username").send_keys("qiu98795")

        driver.find_element_by_css_selector("#ls_password").clear()
        driver.find_element_by_css_selector("#ls_password").send_keys("456852")

        driver.find_element_by_css_selector('[type="submit"]').click()

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(3)

if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://localhost/upload/forum.php")
    driver.implicitly_wait(10)

    Login().user_login(driver)
    Login().user_logout(driver)
