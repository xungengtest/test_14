# -*- coding: utf-8 -*-
#@time :2022-05-29 9:56
#@Author：sky
import allure
import pytest
from util.get_accesstoken_api import Get_AccessToken_API
from common.common_path import *
from common.read_config import Config

cf = Config()

host = cf.get_value("envi.ini","sit","host")
port = cf.get_value("envi.ini","sit","port")

access_token = Get_AccessToken_API(host,port)



@allure.feature("获取access token")
class Test_Get_Access_Token():
    def test_case_01(self):
        result = access_token.get_access_token()
        allure.attach(f"result->{result}")
        assert result["flag"] == "02"




