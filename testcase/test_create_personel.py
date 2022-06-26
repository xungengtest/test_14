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

@pytest.fixture(scope="function",autouse=True)
def init_data(request):
    data = request.param
    return data

@allure.feature("创建成员")
class Test_Create_Personel():

    @allure.title("缺失必要access_token参数_接口报错_返回相应的报错信息")
    @pytest.mark.parametrize("init_data",RY.read_yaml(data_dir,"create_personel.yaml","test0001"),indirect=True)
    def test0001(self,init_data):
        result = AB.create_personel(access_token=init_data["access_token"],userid=init_data["userid"],name=init_data["name"],mobile=init_data["mobile"],\
                                    department=init_data["department"],email=init_data["email"],extattr_type=init_data["extattr_type"], \
                                    extattr_name=init_data["extattr_name"],extattr_text_value=init_data["extattr_text_value"],\
                                    extattr_web_url=init_data["extattr_web_url"], extattr_web_title=init_data["extattr_web_title"],\
                                    access_token_flag=init_data["access_token_flag"])
        assert result[0] == 200
        assert result[1]["errcode"] == 41001
        assert  "access_token missing"  in  result[1]["errmsg"]
        allure.attach(f"result->{result}")

    @allure.title("缺失必要access_token参数_接口报错_返回相应的报错信息")
    @pytest.mark.parametrize("init_data",RY.read_yaml(data_dir,"create_personel.yaml","test0001"),indirect=True)
    def test00011(self,init_data):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = init_data
        result = AB.create_personel_new(url,data)
        assert result[0] == 200
        assert result[1]["errcode"] == 41001
        assert  "access_token missing"  in  result[1]["errmsg"]
        allure.attach(f"result->{result}")

    @allure.title("缺失必要userid参数_接口报错_返回相应的报错信息")
    @pytest.mark.parametrize("init_data",RY.read_yaml(data_dir,"create_personel.yaml","test0002"),indirect=True)
    def test0002(self,init_data,get_access_token):
        access_token = get_access_token
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}'
        data = init_data
        result = AB.create_personel_new(url,data)
        assert result[0] == 200
        assert result[1]["errcode"] == 41009
        assert  "missing userid"  in  result[1]["errmsg"]
        allure.attach(f"result->{result}")

    @allure.title("缺失必要userid参数_接口报错_返回相应的报错信息")
    @pytest.mark.parametrize("init_data",RY.read_yaml(data_dir,"create_personel.yaml","test0003"),indirect=True)
    def test0003(self,init_data,get_access_token):
        access_token = get_access_token
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}'
        data = init_data
        result = AB.create_personel_new(url,data)
        assert result[0] == 200
        assert result[1]["errcode"] == 60112
        assert  "invalid name"  in  result[1]["errmsg"]
        allure.attach(f"result->{result}")
