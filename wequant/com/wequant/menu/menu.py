#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: menu.py 
@time: 2017/09/25 
@software: PyCharm
"""

from com.wequant.common import tools
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def click_home_page(driver,wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"li.top_word.home_page.navigation_color")))
    driver.find_element_by_css_selector("li.top_word.home_page.navigation_color").click()

def click_policy_edit(driver,wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"li.top_word.tactics")))
    driver.find_element_by_css_selector("li.top_word.tactics").click()

def click_shipan(driver,wait):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"li.top_word.trade")))
    driver.find_element_by_css_selector("li.top_word.trade").click()