import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

class TestLogin(myunit.StarEnd):
    def test_login1_normal(self):
        '''username and passwd isnormal'''
        print("test_login1_normal is star test...")
        po=LoginPage(self.driver)
        po.Login_action("qiu98795",456852)
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'好友')
        function.insert_img(self.driver,"warp_login1_normal.jpg")
        print("test_login1_normal test end!")

    def test_login2_PasswdError(self):
        '''username is ok,passwd is error'''
        print("test_login2_passwdError is start test...")
        po=LoginPage(self.driver)
        po.Login_action("qiu98795",123456)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_login2_PasswdError.jpg")
        print("test_login2_PasswdError test end!")

    def test_login3_empty(self):
        '''username and passwd is empty'''
        print("test_login3_empty is start test...")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_login3_empty.jpg")
        print("test_login3_empty test end")

if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(TestLogin("test_login1_normal"))
    # suite.addTest(TestLogin("test_login2_PasswdError"))
    # suite.addTest(TestLogin("test_login3_empty"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
