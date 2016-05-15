#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python - BrowserMob - WebDriver"""
from browsermobproxy import Server
from selenium import webdriver
import json
 
class CreateHar(object):
    """create HTTP archive file"""
 
    def __init__(self, mob_path):
        """initial setup"""
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None
 
    @staticmethod
    def __store_into_file(title, result):
        """store result"""
        har_file = open(title + '.har', 'w')
        har_file.write(str(result))
        har_file.close()
 
    def __start_server(self):
        """prepare and start server"""
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()
 
    def __start_driver(self):
        """prepare and start driver"""
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--proxy-server={0}".format(self.proxy.proxy))

        capabilities = webdriver.DesiredCapabilities.CHROME
        capabilities['chrome.binary']=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        capabilities['proxy'] = {
            'httpProxy' : "%s" %(self.proxy.proxy),
            'ftpProxy' : "%s" %(self.proxy.proxy),
            'sslProxy' : "%s" %(self.proxy.proxy),
            'noProxy' : None,
            'proxyType' : "MANUAL",
            'class' : "org.openqa.selenium.Proxy",
            'autodetect' : False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:9515", capabilities)
 
    def start_all(self):
        """start server and driver"""
        self.__start_server()
        self.__start_driver()
 
    def create_har(self, title, url):
        """start request and parse response"""
        self.proxy.new_har(title)
        self.driver.get(url)
        result = json.dumps(self.proxy.har, ensure_ascii=False)
        self.__store_into_file(title, result)
 
    def stop_all(self):
        """stop server and driver"""
        self.server.stop()
        self.driver.quit()
 
 
if __name__ == '__main__':
    path = r"C:\Users\Administrator\Desktop\browsermob-proxy-2.1.0-beta-6\bin\browsermob-proxy.bat"
    RUN = CreateHar(path)
    RUN.start_all()
    # RUN.create_har('stackoverflow', 'http://stackoverflow.com')
    # RUN.create_har('PPTV首页', 'http://www.pptv.com')
    # RUN.create_har('百度一下，你就知道', 'http://www.pptv.com')
    RUN.create_har(u'欢乐颂(第01集)-高清在线观看-PPTV聚力-始终和你同一频道', 'http://v.pptv.com/show/61uPDHTaSojradE.html')
    
    RUN.stop_all()