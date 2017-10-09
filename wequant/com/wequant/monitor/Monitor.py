#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 2017/9/13
# @Author     : lijie
# @File       : Monitor.py
# @Software   : PyCharm

import ConfigParser
import datetime
import logging.handlers
import platform
import time
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from com.wequant.common import mail

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

platatt = platform.system()
# 设置Mac环境下Chrome浏览器全屏参数
if platatt == 'Darwin':
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--kiosk")
    # 实例化一个Chrome浏览器
    driver = webdriver.Chrome()
    driver.set_window_size(1080, 800)
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
wait = WebDriverWait(driver, 20, 0.5)
conf = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resource')
screenshot_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'screenshot')
conf.read(config_path + "/config.ini")
url = conf.get("login", "url")
username = conf.get("login", "username")
password = conf.get("login", "password")

try:
    # 打开wequant主页
    driver.get(url)
    # 点击主页上的登录按钮
    driver.find_element_by_css_selector("input[value='登录']").click()
    # 输入用户名
    driver.find_element_by_id("loginName").send_keys(username)
    time.sleep(1)
    # 输入密码
    driver.find_element_by_css_selector("input.password").send_keys(password)
    # 点击登录界面上的登录按钮
    # time.sleep(10)
    driver.find_element_by_css_selector("input[type='submit']").click()
except Exception as e:
    raise Exception
# sp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[text()='实盘交易']")))
# sp.click()
time.sleep(5)
i = 0
count = 5
while i < count:
    # 点击实盘按钮
    logger.info("第" + str(i + 1) + "次点击实盘交易按钮")
    driver.find_element_by_xpath("//li[text()='实盘交易']").click()

    # 判断实盘数据是否加载出来
    timeout = 10
    end_time = time.time() + timeout
    while True:
        els = driver.find_elements_by_xpath("//li[1]/div[@class='num_text black']")
        if len(els) != 0:
            logger.info("实盘数据加载完成")
            break
        time.sleep(0.5)
        if time.time() > end_time:
            shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S'))
            driver.get_screenshot_as_file(screenshot_path + "/" + shottime + ".png")
            picname = screenshot_path + "/" + shottime + ".png"
            mail.sendHtmlEmail(picname)
            raise TimeoutException()

    # 查看日志是否正确打印
    logger.info("第" + str(i + 1) + "次点击日志按钮")
    driver.find_element_by_xpath("//li[text()='日志']").click()
    time.sleep(1)
    logtimeout = 10
    log_end_time = time.time() + timeout
    while True:
        logels = driver.find_elements_by_xpath("//pre[1]/span[@style='padding-right: 0.1px;']")
        if len(logels) != 0:
            log = driver.find_element_by_xpath("//pre[1]/span[@style='padding-right: 0.1px;']").text
            logger.info(log)
            t = ' '.join(log.split(' ', 2)[:2])
            lasttime = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
            now = datetime.datetime.now()
            x = (now - lasttime).seconds / 60
            if x > 2:
                shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S'))
                driver.get_screenshot_as_file(screenshot_path + "/" + shottime + ".png")
                picname = screenshot_path + "/" + shottime + ".png"
                mail.sendHtmlEmail(picname)
                raise TimeoutException()
            logger.info("日志打印正确")
            break
        time.sleep(0.5)
        if time.time() > log_end_time:
            shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S'))
            driver.get_screenshot_as_file(screenshot_path + "/" + shottime + ".png")
            picname = screenshot_path + "/" + shottime + ".png"
            mail.sendHtmlEmail(picname)
            raise TimeoutException()
    i = i + 1
    time.sleep(10)

driver.close()
