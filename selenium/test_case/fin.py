#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python - BrowserMob - WebDriver"""
'''
1.准备工作

1) 安装python package
运行前请安装好selenium
参考链接-> http://selenium-python.readthedocs.io/installation.html
pip install selenium
运行前请安装好browsermob-proxy
参考链接-> https://browsermob-proxy-py.readthedocs.io/en/stable/
pip install browsermob-proxy

2) 下载运行环境所需软件

#1 下载代理软件,该软件需要有java运行环境
参考链接-> https://bmp.lightbody.net/
下载链接-> https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.1.0/browsermob-proxy-2.1.0-bin.zip

#2 下载chromedriver
参考链接-> https://sites.google.com/a/chromium.org/chromedriver/downloads
下载链接-> http://chromedriver.storage.googleapis.com/index.html?path=2.21/

#3 下载chrome
自行百度安装

2.运行环境
1) 运行chromedriver
解压下载的chromedriver zip包，在命令行中cd 到解压目录 然后运行chromedriver(在mac or linux 下 ./chromedriver，在windows下 chromedriver.exe )

2) 运行browsermob-proxy
解压下载browsermob-proxy包, 在命令行中cd 到解压目录 在进入bin目录 运行browsermob-proxy(运行方式参考chromedriver)

3.进行测试
配置fin.py 参数:proxy_path,chrome_binary_path,chromedriver_service_url
python fin.py
'''
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
import os
import re

#网页代理地址 windows上面应该是browsermob-proxy.bat文件
proxy_path=r"C:\Users\Administrator\Desktop\browsermob-proxy-2.1.0-beta-6\bin\browsermob-proxy.bat"
#chrome browser 可执行文件所在路径
chrome_binary_path=r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
#运行chromedriver,看下绑定的端口,主要配置下端口
chromedriver_service_url="http://127.0.0.1:9515"
new_url="http://127.0.0.1:4444/wd/hub"

class CreateHar(object):
    """create HTTP archive file"""

    def __init__(self, mob_path):
        """initial setup"""
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None
        self.resultlist = []
        self.adsdict = {}

    @staticmethod
    def __store_into_file(title, result):
        """store result"""
        # print(result)

        if os.path.isfile(title):
          har_file = open(title, 'a')
          har_file.write(str(result))
          har_file.close()
        else:
          har_file = open(title, 'w')
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
        #这里配置的是chrome 可执行文件的地址，windows上面应该以.exe结尾
        capabilities['chrome.binary']=chrome_binary_path
        capabilities['proxy'] = {
            'httpProxy' : "%s" %(self.proxy.proxy),
            'ftpProxy' : "%s" %(self.proxy.proxy),
            'sslProxy' : "%s" %(self.proxy.proxy),
            'noProxy' : None,
            'proxyType' : "MANUAL",
            'class' : "org.openqa.selenium.Proxy",
            'autodetect' : False
        }
        self.driver = webdriver.Remote(chromedriver_service_url, capabilities)

    def start_all(self):
        """start server and driver"""
        self.__start_server()
        self.__start_driver()

    def create_har(self, title, url,waittime):
        """start request and parse response"""
        self.proxy.new_har(title)
        sleep(waittime)
        result = json.dumps(self.proxy.har, ensure_ascii=False)
        #self.__store_into_file(title+'原始',result)
        data = json.loads(result)
        if "log" in data.keys() and "entries" in data['log'].keys():
          for index, req in enumerate(data['log']["entries"]):
            # print('index:%d'%index)
            # print("request" in req.keys())
            # print("url" in req["request"].keys())
            # print("jp.as.pptv.com" in req["request"]["url"])
            if "request" in req.keys() and "url" in req["request"].keys() and "jp.as.pptv.com" in req["request"]["url"]:
              self.resultlist.append(req["request"]["url"])
              tid_pattern=re.compile("tid=(\w+)")
              tid = tid_pattern.findall(req["request"]["url"])
              act_pattern=re.compile("act=(\d+)")
              act = act_pattern.findall(req["request"]["url"])
              if tid[0] in self.adsdict.keys():
                self.adsdict[tid[0]].append(act[0])
              else:
                self.adsdict[tid[0]] = act
        self.__store_into_file(title, self.resultlist)


    def check_ads(self,adlen):
      err = ""
      adslen = len(self.adsdict)
      if adslen == adlen:
        for key in self.adsdict.keys():
          if not (list(self.adsdict[key]).count("1000") == 1):
            err += key + ":act=1000 is empty or have much \n"
          if not (list(self.adsdict[key]).count("1001") == 1):
            err += key + ":act=1001 is empty or have much \n"
      else:
        err += "this video's maxl and maxc is err,maxc=" + adslen
      self.__store_into_file("ads_errlog",err)
      return len(err)


    def stop_all(self):
        """stop server and driver"""
        self.server.stop()
        self.driver.quit()

    def switch_to_last_window(self):
        hand = self.driver.window_handles
        self.driver.switch_to_window(hand[len(hand)-1])

def open_host(url):
    RUN = CreateHar(proxy_path)
    RUN.start_all()
    RUN.driver.maximize_window()
    RUN.driver.implicitly_wait(10)
    RUN.driver.get(url)
    return RUN

def host_search(RUN,keyword,xpath,waittime):
    kw_input=RUN.driver.find_element_by_name('kw')
    kw_input.clear()
    kw_input.send_keys(keyword + Keys.RETURN)
    sleep(1)
    RUN.switch_to_last_window()
    RUN.driver.find_element_by_xpath(xpath).click()
    sleep(1)
    RUN.switch_to_last_window()
    #这里是你要请求的网页的title和网页链接地址 har文件保存在和执行python文件同一目录中
    RUN.create_har(RUN.driver.title, RUN.driver.current_url,waittime)
    #json数据过滤后加上断言
def close_all(RUN):
    RUN.stop_all()





if __name__ == '__main__':

    RUN = CreateHar(proxy_path)
    RUN.start_all()

    RUN.driver.get('http://www.pptv.com')
    kw_input=RUN.driver.find_element_by_name('kw')
    kw_input.clear()
    kw_input.send_keys(u'欢乐颂' + Keys.RETURN)
    RUN.switch_to_last_window()
    RUN.driver.find_element_by_xpath("//*[@id='search-result']/div[1]/div[2]/div/div[1]/ul/li[1]/a").click()
    RUN.switch_to_last_window()
    #这里是你要请求的网页的title和网页链接地址 har文件保存在和执行python文件同一目录中
    RUN.create_har(RUN.driver.title, RUN.driver.current_url)
    RUN.stop_all()

