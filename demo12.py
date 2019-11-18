from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("https://www.momoshop.com.tw/main/Main.jsp/")
element1 = browser.find_element_by_id('keyword')
# 找出網頁serch的text id <input id="keyword" name="keyword" type="text" placeholder="請輸入關鍵字或品號" class="inputArea ac_input" autocomplete="off" />
element1.clear()
element1.send_keys("apple")
element1.send_keys(Keys.RETURN)
# time.sleep(20)
# browser.close()