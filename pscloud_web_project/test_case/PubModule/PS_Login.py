from  selenium import webdriver
import time
def Login(self,name,password):
    wd = self.wd
    wd.get("https://www.mypscloud.com/my")
    time.sleep(0.5)
    # wd.find_element_by_id("login").send_keys("wangshuai04@inspur.com")
    # wd.find_element_by_id("password").send_keys("pllilu1314!@")
    wd.find_element_by_id("login").send_keys(name)
    wd.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    wd.find_element_by_xpath("//*[@id='wrapwrap']/main/div/div/form/div[3]/button").click()
    # wd.find_element_by_class_name("btn").click()
    time.sleep(1)
    wd.find_element_by_xpath("//*[@id='wrapwrap']/header/div[2]/div/div/a").click()
    time.sleep(1)
    wd.find_element_by_link_text("我的数据库").click()
    time.sleep(2)
    wd.find_elements_by_class_name("odoo-oe-instance")[1].click()
    time.sleep(1)
    wd.find_element_by_id("login").send_keys("wangshuai04@inspur.com")
    wd.find_element_by_id("password").send_keys("pllilu1314!@")
    wd.find_element_by_class_name("btn").click()
    time.sleep(2)
