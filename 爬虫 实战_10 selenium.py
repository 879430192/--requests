from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象
web = Chrome()

URL ='https://www.zhulang.com/'

web.get(url=URL)

web.find_element_by_xpath('//*[@id="topsch"]/form/input').send_keys("天",Keys.ENTER)

time.sleep(2)

list_li = book = web.find_elements_by_xpath('//*[@id="sch-result"]/div[2]/ul/li')
#遍历并提取数据
for li in list_li:
    book_name = li.find_element_by_xpath('/dl/dt/a[1]/span').text
    print(book_name)