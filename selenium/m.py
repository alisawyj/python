from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from browsermobproxy import Server
import urllib.parse

server = Server(r"C:\Users\Administrator\Desktop\browsermob-proxy-2.1.0-beta-6\bin\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()
proxy.new_har()

chrome_options = webdriver.ChromeOptions()
url = urllib.parse.urlparse(proxy.proxy).path
chrome_options.add_argument('--proxy-server=%s' % url)
driver = webdriver.Chrome(
    executable_path=r"c:\chromedriver.exe",
    chrome_options=chrome_options)
driver.get("http://v.pptv.com/show/61uPDHTaSojradE.html")

print (proxy.har)

driver.quit()
server.stop()
