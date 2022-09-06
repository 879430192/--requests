from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

web = Chrome()  #创建无头浏览器

url = "https://www.lagou.com/"  #网站的URL

web.get(url)

web.find_element_by_xpath('//*[@id="cboxClose"]').click()   #选择事件并点击

time.sleep(2)  #休眠时长

web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER) #在窗口中输入文本并回车

time.sleep(2)

#寻找网页数据存放的位置，提取出来

list_li = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
for li in list_li:
    job_name = li.find_element_by_tag_name('div[1]/div[1]/div[1]/a').text
    print(job_name)
