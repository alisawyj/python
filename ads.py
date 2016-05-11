from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.pptv.com")
pptv_window = driver.current_window_handle


driver.find_element_by_name("kw").send_keys("欢乐颂")
driver.find_element_by_css_selector("[title='搜索']").click()

#driver.implicitly_wait(10)

all_handles = driver.window_handles
		#进入新的页面
for handle in all_handles:
	if handle !=pptv_window:
		driver.switch_to_window(handle)
		title = driver.title
		print(title)
		driver.find_element_by_xpath("//div[@id='search-result']/div[2]/div[2]/div/div[1]/ul/li[1]/a").click()
		break
'''sleep(60)
driver.find_element_by_xpath("//*[@id='PPTV_PLAYER1462973947719']/embed").click()
driver.find_element_by_xpath("//*[@id='PPTV_PLAYER1462973947719']/embed").send_keys(Keys.SHIFT,Keys.HOME)
driver.find_element_by_xpath("//*[@id='PPTV_PLAYER1462973947719']/embed").send_keys(Keys.CONTROL,'a')
driver.find_element_by_xpath("//*[@id='PPTV_PLAYER1462973947719']/embed").send_keys(Keys.CONTROL,'c')
#driver.find_element_by_xpath("//*[@id="PPTV_PLAYER1462973947719"]/embed").send_keys(Keys.CONTROL,'v')'''

driver.quit()


