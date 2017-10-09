#coding:utf-8
import unittest
import os
import sys
import HTMLTestRunner
case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
report_path = os.path.join(os.getcwd(),"report/report.html")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
    fr = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title=u"WEQUANT自动化测试报告",description=u"WEQUANT自动化测试用例运行结果如下:")
    runner.run(suite)
