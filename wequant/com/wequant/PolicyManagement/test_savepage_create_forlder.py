#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: test_savepage_create_forlder.py 
@time: 2017/09/26 
@software: PyCharm
"""

import unittest
from com.wequant.common import tools
from com.wequant.common.tools import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from com.wequant.menu import menu
import time

driver,wait = tools.getdriver()
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tools.login(driver, wait)
        menu.click_policy_edit(driver, wait)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.nextBtn.step1")))
        driver.find_element_by_css_selector("img.nextBtn.step1").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.nextBtn.step2")))
        driver.find_element_by_css_selector("img.nextBtn.step2").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.nextBtn.step3")))
        driver.find_element_by_css_selector("img.nextBtn.step3").click()



    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        driver.find_element_by_css_selector("span.deletefile_text").click()
        driver.find_element_by_xpath("//div/span[@title='auto_temp']/../../input").click()
        driver.find_element_by_css_selector("span.deletefile_text").click()
        driver.find_element_by_id("delteFolder").click()
        driver.find_element_by_css_selector("input[type='button'][value='确认删除']").click()


    def test_savepage_create_forlder(self):
        # 点击左上角的加号按钮
        wait.until(EC.visibility_of_element_located((By.ID, "strategyName")))
        driver.find_element_by_id("strategyName").click()
        # 选择海龟策略
        time.sleep(1)
        driver.find_element_by_css_selector("li[title='海龟策略']").click()
        # 点击保存按钮
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[title^='海龟策略']")))
        driver.find_element_by_css_selector("span.save_text").click()
        # 点击新建按钮
        wait.until(EC.visibility_of_element_located((By.ID,"add_folder_btn1")))
        driver.find_element_by_id("add_folder_btn1").click()
        # 输入框中输入auto_temp
        time.sleep(1)
        driver.find_element_by_id("otherSaveText2").send_keys("auto_temp")
        # 点击对勾按钮
        time.sleep(1)
        driver.find_element_by_css_selector("span>img[src='/img/algorithms/rename_confirm.png']").click()
        # 点击取消按钮
        time.sleep(1)
        driver.find_element_by_css_selector("div.otherSave_content>div>input.save_cancel_btn").click()
        #点击文件夹按钮
        wait.until(EC.visibility_of_element_located((By.ID,"file_manage")))
        driver.find_element_by_id("file_manage").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span.folder_name.hidden_text")))
        results = driver.find_elements_by_css_selector("span.folder_name.hidden_text")
        content = [result.text for result in results]
        self.assertIn("auto_temp", content)


if __name__ == '__main__':
    unittest.main()
