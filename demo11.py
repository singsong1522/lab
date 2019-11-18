from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("https://24h.pchome.com.tw/")
element1 = browser.find_element_by_id('keyword')
# 找出網頁serch的text id <input type="text" id="keyword" class="text left" />
element1.clear()
element1.send_keys("床")
element1.send_keys(Keys.RETURN)
time.sleep(20)

#browser.close()