# -*- coding:utf-8 -*-
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, os, sys
import random
from Constant.sys_constant import *
from test_case.PubModule import PS_Login
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Test_login(unittest.TestCase):
    def setUp(self):

        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        wd = self.wd
        PS_Login.Login(self,"wangshuai04@inspur.com","pllilu1314!@")

    def test_01_videos(self):
        success = True
        wd = self.wd

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()