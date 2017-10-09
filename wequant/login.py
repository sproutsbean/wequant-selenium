#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 2017/9/13
# @Author     : lijie
# @File       : Monitor.py
# @Software   : PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
import logging.handlers
import time
from tools import tools

driver = tools.getdriver()
#打开wequant主页
driver.get("https://www.wequant.io")
#点击主页上的登录按钮
driver.find_element_by_css_selector("input[value='登录']").click()
#输入用户名
driver.find_element_by_id("loginName").send_keys("15817372277")
time.sleep(1)
#输入密码
driver.find_element_by_css_selector("input.password").send_keys("sprouts+888")
#点击登录界面上的登录按钮
driver.find_element_by_css_selector("input[type='submit']").click()
# sp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[text()='实盘交易']")))
# sp.click()
time.sleep(5)