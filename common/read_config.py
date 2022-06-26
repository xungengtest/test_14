# -*- coding: utf-8 -*-
#@time :2022-05-29 9:34
#@Author：sky
import os
import configparser
from  common.common_path import *

class Config():

    #获取文件路径函数
    def get_file_path(self,foldername,filename,childer_folder=None):
        file_path = os.path.join(foldername,filename)
        if childer_folder:
            file_path = os.path.join(file_path,childer_folder)

        return file_path

    #读取配置文件
    def get_config_file(self,file_name):
        try:
            config = configparser.ConfigParser()
            file_path = self.get_file_path(conf_dir,file_name)
            config.read(file_path,encoding="utf-8-sig")
            return config
        except Exception as error:
            print("read config file error" + str(error))

    #指定读取配置文件section和key值
    def get_value(self,filename,section,key):
        try:
            config = self.get_config_file(filename)
            value  = config.get(section,key)
            return value
        except Exception as error:
            print("get value failed:"+str(error))


if __name__ == '__main__':
    cf = Config()
    print(cf.get_value("envi.ini","sit","host"))
    print(cf.get_value("envi.ini","sit","port"))

