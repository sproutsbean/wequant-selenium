#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 2017/9/22
# @Author     : lijie
# @File       : clean_admin_cache.py
# @Software   : PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()

url="https://admin-835b749243296168.wequant.io/admin/wequant/block_list/"
username = "282751606@qq.com"
password = "sprouts+888"
driver.get(url)

driver.find_element_by_id("id_username").send_keys(username)
driver.find_element_by_id("id_password").send_keys(password)
driver.find_element_by_css_selector("input[type='submit']").click()


while True:
    driver.find_element_by_xpath("//button[text()='重置被Ban的IP地址状态']").click()
    time.sleep(30)
