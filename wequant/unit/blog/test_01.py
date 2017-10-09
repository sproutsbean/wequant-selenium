#coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("blog01start")

    def tearDown(self):
        print("blog01end")

    def test01(self):
        print("执行测试用例07")

    def test03(self):
        print("执行测试用例09")

    def test02(self):
        print("执行测试用例08")

if __name__ == "__main__":
    unittest.main()