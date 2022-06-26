# -*- coding: utf-8 -*-
#@time :2022-05-22 15:26
#@Author：sky
import allure
import pytest
from util.address_book_api import Address_Book_API
from common.common_path import *
from common.read_yaml import Read_Yaml

AB = Address_Book_API()
RY = Read_Yaml()

#生成access_token
@pytest.fixture(scope="class",autouse=True)
def get_access_token():
    access_token = AB.get_access_token()
    return access_token

@pytest.fixture(scope="class",autouse=True)
def init_create_personel(get_access_token):
    access_token = get_access_token
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}'
    data = RY.read_yaml(data_dir,"query_personel.yaml","create_personel")[0]
    result = AB.create_personel_new(url,data)
    assert result[0] == 200
    allure.attach(f"result->{result}")

    return data["userid"],data["name"]

@pytest.fixture(scope="function",autouse=True)
def init_data(request):
    data = request.param
    return data

@allure.feature("查询成员")
class Test_Query_Personel():

    @allure.title("缺失必要access_token参数_接口报错_返回相应的报错信息")
    @pytest.mark.parametrize("init_data",RY.read_yaml(data_dir,"query_personel.yaml","test0001"),indirect=True)
    def test0001(self,init_data,init_create_personel):
        userid = init_create_personel[0]
        result = AB.query_personel(userid=userid,access_token_flag=init_data["access_token_flag"])
        assert result[0] == 200
        assert result[1]["errcode"] ==  41001
        assert result[1]["errmsg"] != "access_token missing"

        allure.attach(f"result->{result}")

