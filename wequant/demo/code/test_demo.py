#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:lijie 
@file: select.py 
@time: 2017/09/28 
@software: PyCharm
"""

import pandas as pd
# import matplotlib.pyplot as plt

# pd.set_option("expand_frame_repr", False)
# pd.set_option()
stock_data = pd.read_excel("/Users/lijie/PycharmProjects/wequant/demo/data/test_data.xlsx")
print stock_data
stock_data.columns = [i.encode('utf8') for i in stock_data.columns]
stock_data['交易日期'] = pd.to_datetime(stock_data['交易日期'])

print stock_data[['交易日期','股票代码']]