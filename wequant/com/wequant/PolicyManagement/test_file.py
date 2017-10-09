#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: test_file.py 
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
        pass

    def test_add_file(self):
        file_name = "auto_create_file"
        # 点击左上角的加号按钮
        wait.until(EC.visibility_of_element_located((By.ID, "strategyName")))
        driver.find_element_by_id("strategyName").click()
        # 选择海龟策略
        time.sleep(1)
        driver.find_element_by_css_selector("li[title='海龟策略']").click()
        # 点击保存按钮
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[title^='海龟策略']")))
        driver.find_element_by_css_selector("span.save_text").click()
        time.sleep(1)
        #clear filename and input filename
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.new_file_name1")))
        driver.find_element_by_css_selector("input.new_file_name1").clear()
        driver.find_element_by_css_selector("input.new_file_name1").send_keys(file_name)
        #click down list
        driver.find_element_by_id("otherSaveText").click()
        time.sleep(1)
        #choose the first one
        folder = driver.find_elements_by_css_selector("#folderNames>li>span")
        folder[0].click()
        #点击保存按钮
        driver.find_element_by_css_selector("div.otherSave_content>div>input[class='save_sure_btn']").click()
        #click sure button
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.save_success_bt")))
        time.sleep(3)
        driver.find_elements_by_css_selector("input.save_success_btn")[0].click()


        driver.find_element_by_id("file_manage").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span.file_name.hidden_text")))
        filename_els = driver.find_elements_by_css_selector("span.file_name.hidden_text")
        filenames = [filename.text for filename in filename_els]
        self.assertIn(file_name,filenames)



    # def test_add_file(self):
    #     self.assertEqual(True, False)
    #
    # def test_add_file(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
