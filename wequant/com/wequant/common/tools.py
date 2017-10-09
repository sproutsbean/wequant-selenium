#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 2017/9/13
# @Author     : lijie
# @File       : Monitor.py
# @Software   : PyCharm

import platform
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
import logging.handlers
import time
import ConfigParser

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log/log.txt')
fh = logging.FileHandler(log_path)
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


platatt = platform.system()
conf = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resource')
conf.read(config_path+"/config.ini")
def getdriver():
    if platatt == 'Darwin':
        # chromeoptions = webdriver.ChromeOptions()
        # chromeoptions.add_argument("--kiosk")
        # 实例化一个Chrome浏览器
        driver = webdriver.Chrome()
        driver.set_window_size(1180,1000)
    elif platatt == "Windows":
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("--start-maximized")
        # 实例化一个Chrome浏览器
        driver = webdriver.Chrome(chrome_options=chromeoptions)
    else:
        logger.info("This platform is not Mac and Windows!! Please check!!")
        raise
    # 隐式设置等待时间为3秒
    driver.implicitly_wait(3)
    # 显示设置等待时间为20秒，每0.5秒循环一次
    wait = WebDriverWait(driver, 10, 0.5)
    return driver,wait

def login(driver,wait):
    url = conf.get("login","url")
    username = conf.get("login","username")
    password = conf.get("login","password")
    # 打开wequant主页
    driver.get(url)
    # 点击主页上的登录按钮
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[value='登录']")))
    driver.find_element_by_css_selector("input[value='登录']").click()
    # 输入用户名
    wait.until(EC.presence_of_element_located((By.ID,"loginName")))
    driver.find_element_by_id("loginName").send_keys(username)
    # 输入密码
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.password")))
    driver.find_element_by_css_selector("input.password").send_keys(password)
    # 点击登录界面上的登录按钮
    driver.find_element_by_css_selector("input[type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "input[type='button'][value='登录']")))
    logger.info("登录成功")