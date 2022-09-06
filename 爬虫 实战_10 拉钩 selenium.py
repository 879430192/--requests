from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("https://www.lagou.com/")

#找到某个元素来进行点击

el = web.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a')
el.click()   # 点击事件
time.sleep(3)


#找到输入框->输入Python->点击回车/点击搜索

web.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[1]/form/input[1]').send_keys("python",Keys.ENTER)
time.sleep(3)
#查找数据的存放位置，进行数据提取
#找到页面中存放数据的所有的li
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
# print(li_list)
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_price = li.find_element_by_xpath("./div/div/div[2]/div/span").text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(company_name,job_name,job_price)