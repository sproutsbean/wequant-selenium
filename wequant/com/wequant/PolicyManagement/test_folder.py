#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: test_folder.py 
@time: 2017/09/25 
@software: PyCharm
"""

import unittest
from com.wequant.common import tools
from com.wequant.menu import menu
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver, wait = tools.getdriver()

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
        wait.until(EC.visibility_of_element_located((By.ID, "file_manage")))
        driver.find_element_by_id("file_manage").click()
    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1_add_folder(self):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.addfile_text")))
        driver.find_element_by_css_selector("span.addfile_text").click()
        time.sleep(1)
        names = driver.find_elements_by_css_selector("input.re_folder_name")
        names[0].send_keys("auto_create_folder")
        gous = driver.find_elements_by_xpath(
            "//div[@class='rename_folder_content']/img[@src='/img/algorithms/rename_confirm.png']")
        gous[0].click()
        results = driver.find_elements_by_css_selector("div>span[title='auto_create_folder']")
        self.assertEqual(len(results), 1)

    def test2_update_folder(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div>span[title='auto_create_folder']+img")))
        driver.find_element_by_css_selector("div>span[title='auto_create_folder']+img").click()
        names = driver.find_elements_by_css_selector("input.re_folder_name")
        names[0].clear()
        names[0].send_keys("update_auto_create_folder")
        gous = driver.find_elements_by_xpath(
            "//div[@class='rename_folder_content']/img[@src='/img/algorithms/rename_confirm.png']")
        gous[0].click()
        results = driver.find_elements_by_css_selector("div>span[title='update_auto_create_folder']")
        self.assertEqual(len(results), 1)

    def test3_delete_folder(self):
        driver.find_element_by_css_selector("span.deletefile_text").click()
        driver.find_element_by_xpath("//div/span[@title='update_auto_create_folder']/../../input").click()
        driver.find_element_by_css_selector("span.deletefile_text").click()
        driver.find_element_by_id("delteFolder").click()
        driver.find_element_by_css_selector("input[type='button'][value='确认删除']").click()
        time.sleep(1)
        results = driver.find_elements_by_css_selector("span.folder_name.hidden_text")
        content = [result.text for result in results]
        self.assertNotIn("update_auto_create_folder",content)


if __name__ == '__main__':
    unittest.main()
