from selenium import webdriver
from fin import *
import unittest
import time
import sys

class MiddleShortVideo(unittest.TestCase):
    '''3-5min的中短视频'''
    def setUp(self):
        url = "http://www.pptv.com"
        self.RUN = open_host(url)
    def test_msvideo(self):
        '''中短视频：出一个广告'''
        keyword = u"我是剧大大"
        xpath = "//*[@id='search-result']/div/div[2]/div/div/ul/li[1]/a"
        waittime=20
        adlen=1
        host_search(self.RUN,keyword,xpath,waittime)
        self.assertTrue(self.RUN.check_ads(adlen) == 0,msg="check log file!")
    def tearDown(self):
        self.RUN.stop_all()
if __name__ == '__main__':
    unittest.main()



