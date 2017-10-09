#coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("baidu02start")

    def tearDown(self):
        print("baidu02end")

    def test01(self):
        print("执行测试用例04")

    def test03(self):
        print("执行测试用例05")

    def test02(self):
        print("执行测试用例06")

if __name__ == "__main__":
    unittest.main()