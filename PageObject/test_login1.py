from selenium import webdriver
from LoginPage import *

driver=webdriver.Firefox()

username="qiu98795"
password="456852"

test_user_login(driver,username,password)
sleep(3)
driver.quit()