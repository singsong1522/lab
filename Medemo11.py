from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("https://www.ruten.com.tw/")
element1 = browser.find_element_by_id('keyword')
# 找出網頁serch的text id <input type="text" id="keyword" class="text left" />
element1.clear()
element1.send_keys("fx6300")
element1.send_keys(Keys.RETURN)
time.sleep(10)

#browser.close()