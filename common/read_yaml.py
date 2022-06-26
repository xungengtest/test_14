# -*- coding: utf-8 -*-
#@time :2022-05-22 15:44
#@Author：sky
import os
import yaml
from common.common_path import *

class Read_Yaml():

    def read_yaml(self,dir_path,file_name,section):
        file_path = os.path.join(dir_path,file_name)
        with open(f"{file_path}") as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
        return content[section]


if __name__ == '__main__':
    ry = Read_Yaml()
    content = ry.read_yaml(data_dir,"query_personel.yaml","test0001")
    print(type(content))