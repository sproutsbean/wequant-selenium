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

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 设置Mac环境下Chrome浏览器全屏参数
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--kiosk")
# 实例化一个Chrome浏览器
driver = webdriver.Chrome(chrome_options=chromeoptions)
# 隐式设置等待时间为3秒
driver.implicitly_wait(3)
# 显示设置等待时间为20秒，每0.5秒循环一次
wait = WebDriverWait(driver, 20, 0.5)
# 打开wequant主页
driver.get("https://www.wequant.io")
# 点击主页上的登录按钮
driver.find_element_by_css_selector("input[value='登录']").click()
# 输入用户名
driver.find_element_by_id("loginName").send_keys("15817372277")
time.sleep(1)
# 输入密码
driver.find_element_by_css_selector("input.password").send_keys("sprouts+888")
# 点击登录界面上的登录按钮
driver.find_element_by_css_selector("input[type='submit']").click()

cookies = driver.get_cookies()
print type(cookies)
print cookies
driver.close()