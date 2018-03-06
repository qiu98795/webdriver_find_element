'''
Page Object是Selenium自动化测试项目开发实践的最佳设计模式之一，通过对界面元素
和功能模块的封装减少冗余代码，同时在后期维护中，若元素定位或功能模块发生变化，
只需要调整页面元素或功能模块封装的代码，提高测试用例的课维护性。
'''
from time import sleep

class Page():
    '''页面基础类'''

    #初始化
    def __init__(self,driver):
        self.driver=driver
        self.base_url='http://localhost/upload/forum.php'
        self.timeout=10

    #打开不同的子页面（私有方法）
    def _open(self,url):
        url_=self.base_url+url
        print("Test page is %s"%url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url==url_,'Did not land on %s'%url_

    def open(self):
        self._open(self.url)

    #元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)