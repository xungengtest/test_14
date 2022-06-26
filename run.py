# -*- coding: utf-8 -*-
#@time :2022-05-22 14:08
#@Author：sky
import os
from common.common_path import *

if __name__ == '__main__':
    # os.system(r"pytest -v    ./testcase/test_get_access_token.py   --alluredir ./report/xml  --clean-alluredir  -o log_cli=true  -o log_lic_level=INFO")
    # os.system(r"allure generate ./report/xml  -o ./report/html  --clean")
    os.system(r"pytest -s    ./testcase   --alluredir ./allure-results --clean-alluredir  -o log_cli=true  -o log_lic_level=INFO")
