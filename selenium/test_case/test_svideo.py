from selenium import webdriver
from fin import *
import unittest
import time
import sys

class ShortVideo(unittest.TestCase):
    '''3min以下的短视频'''
    def setUp(self):
        url = "http://www.pptv.com"
        self.RUN = open_host(url)
    def test_svideo(self):
        '''短视频：不出广告'''
        keyword = u"热点快报"
        xpath = "//*[@id='search-result']/div[1]/div[2]/div/div/ul/li[1]/a"
        waittime=10
        adlen=0
        host_search(self.RUN,keyword,xpath,waittime)
        self.assertTrue(self.RUN.check_ads(adlen) == 0,msg="check log file!")

    def tearDown(self):
        self.RUN.stop_all()
if __name__ == '__main__':
    unittest.main()



