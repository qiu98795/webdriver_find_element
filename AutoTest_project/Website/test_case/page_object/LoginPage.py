from .BasePage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    '''登录页面'''
    url='/forum.php'

    #定位器（以后维护只需要修改这里就好）
    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.CSS_SELECTOR,'[type="submit"]')

    #用户名输入框元素
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #密码输入框元素
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc=(By.LINK_TEXT,"好友")
    loginFail_loc=(By.NAME,"username")

    #成功的断言响应
    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    #失败的断言响应
    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text