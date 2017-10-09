#!/user/bin/env python
# -*-coding:utf-8-*-

import time

from selenium import webdriver

# /Users/lijie/Library/Application\ Support/Google/Chrome/Default/

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--user-data-dir=/Users/lijie/Library/Application\ Support/Google/Chrome/Default/")
# 实例化一个Chrome浏览器
driver = webdriver.Chrome(chrome_options=chromeoptions)

driver.get("https://www.wequant.io")
time.sleep(1)
driver.find_element_by_css_selector("input[value='登录']").click()
driver.find_element_by_id("loginName").send_keys("15817372277")
time.sleep(1)
driver.find_element_by_css_selector("input.password").send_keys("sprouts+888")
driver.find_element_by_css_selector("input[type='submit']").click()