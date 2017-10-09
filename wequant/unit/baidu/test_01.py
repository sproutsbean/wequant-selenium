#coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("baidu01start")

    def tearDown(self):
        print("baidu01end")

    def test01(self):
        print("执行测试用例01")

    def test03(self):
        print("执行测试用例03")

    def test02(self):
        print("执行测试用例02")

if __name__ == "__main__":
    unittest.main()