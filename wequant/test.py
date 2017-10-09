#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 2017/9/13
# @Author     : lijie
# @File       : Monitor.py
# @Software   : PyCharm


from com.wequant.common import tools


driver,wait = tools.getdriver()

tools.login(driver,wait)

tools.logger.info("zhe shi test wenjian dayin d rizhi !!!")