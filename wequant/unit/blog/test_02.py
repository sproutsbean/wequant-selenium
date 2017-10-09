#coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("blog02start")

    def tearDown(self):
        print("blog02end")

    def test01(self):
        print("执行测试用例10")

    def test03(self):
        print("执行测试用例12")

    def test02(self):
        print("执行测试用例11")

if __name__ == "__main__":
    unittest.main()