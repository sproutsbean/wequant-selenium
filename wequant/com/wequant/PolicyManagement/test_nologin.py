#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: test_nologin.py 
@time: 2017/09/25 
@software: PyCharm
"""

import unittest
from com.wequant.common import tools
from com.wequant.common.tools import logger
from com.wequant.menu import menu
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver, wait = tools.getdriver()
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver.get(tools.conf.get("login", "url"))
        logger.info("打开浏览器,不登录")
        menu.click_policy_edit(driver, wait)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img.nextBtn.step1")))
        driver.find_element_by_css_selector("img.nextBtn.step1").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img.nextBtn.step2")))
        driver.find_element_by_css_selector("img.nextBtn.step2").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img.nextBtn.step3")))
        driver.find_element_by_css_selector("img.nextBtn.step3").click()


    @classmethod
    def tearDownClass(cls):
        driver.quit()


    def setUp(self):
        pass

    def tearDown(self):
        driver.find_element_by_css_selector("span.close_all_sign").click()

    #未登录点击修改文件名按钮
    def test_nologin_update_filename(self):
        wait.until(EC.visibility_of_element_located((By.ID,"rename_file")))
        driver.find_element_by_id("rename_file").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els),1)

    #未登录点击文件夹管理按钮
    def test_nologin_policy_management(self):
        wait.until(EC.visibility_of_element_located((By.ID,"file_manage")))
        driver.find_element_by_id("file_manage").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els),1)

    #未登录点击保存按钮
    def test_nologin_save(self):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.save_text")))
        driver.find_element_by_css_selector("span.save_text").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els), 1)

    #未登录点击另存为按钮
    def test_nologin_save_as(self):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.code_down_img_content")))
        driver.find_element_by_css_selector("span.code_down_img_content").click()
        driver.find_element_by_css_selector("#save_not_login>span.operation_text").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els), 1)

    #未登录点击保存并部署到实盘
    def test_nologin_save_deploy(self):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.code_down_img_content")))
        driver.find_element_by_css_selector("span.code_down_img_content").click()
        driver.find_element_by_xpath("//span[text()='保存并部署实盘']").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els), 1)

    #未登录点击运行回测按钮
    def test_nologin_back_test(self):
        wait.until(EC.visibility_of_element_located((By.ID, "run_strategy")))
        driver.find_element_by_id("run_strategy").click()
        els = driver.find_elements_by_css_selector("input.lo_btn.submit_btn")
        self.assertEqual(len(els), 1)

if __name__ == '__main__':
    unittest.main()
