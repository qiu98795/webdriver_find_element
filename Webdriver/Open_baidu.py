from selenium import webdriver
from time import sleep

# 加载浏览器启动
# driver=webdriver.Firefox()
# driver=webdriver.Chrome()
#支持ie8，ie11有兼容性问题
driver=webdriver.Ie()

# 打开一个网站页面
driver.get("https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&rsv_idx=2&tn=baiduhome_pg&ie=utf-8&rsv_cq=selenium&rsv_dl=0_right_recommends_merge_20826&euri=3ad3768e9ef2410f83541687bde37f7f")
print(driver.title)
sleep(3)

# 打开百度首页
driver.get("http://www.baidu.com")
print(driver.title)
sleep(3)

# 关闭浏览器
driver.quit()