from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("http://www.python.org")
element1 = browser.find_element_by_name('q')
element1.clear()
element1.send_keys("tensorflow")
element1.send_keys(Keys.RETURN)
result = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems = result[0].find_elements_by_tag_name("li")
for r in allItems:
    content = r.find_elements_by_tag_name("a")
    print(content[0].text)

#time.sleep(10)
#browser.close()