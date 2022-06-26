# -*- coding: utf-8 -*-
#@time :2022-05-22 15:49
#@Author：sky
import os

#获取当前文件父目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

#配置文件路径
conf_dir = os.path.join(base_dir,"config")
print(conf_dir)

#测试数据路径
data_dir = os.path.join(base_dir,"data")
print(data_dir)

#测试报告路径
report_dir = os.path.join(base_dir,"report")
print(report_dir)

#测试用例路径
testcase_dir = os.path.join(base_dir,"testcase")
print(testcase_dir)

