from selenium import webdriver
from fin import *
import unittest
import time
import sys

class LongVideo(unittest.TestCase):
  '''大于10min的长视频'''
  def setUp(self):
    url = "http://www.pptv.com"
    self.RUN = open_host(url)

  def test_lvideo(self):
    '''长视频：出五个广告'''
    keyword = u"欢乐颂"
    xpath = "//*[@id='search-result']/div[1]/div[2]/div/div[1]/ul/li[1]/a"
    waittime=85
    adlen=5
    host_search(self.RUN,keyword,xpath,waittime)
    self.assertTrue(self.RUN.check_ads(adlen) == 0 ,msg="check log file!")

  def tearDown(self):
    self.RUN.stop_all()


if __name__ == '__main__':
  unittest.main()



