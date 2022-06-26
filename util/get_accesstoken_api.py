# -*- coding: utf-8 -*-
#@time :2022-05-22 14:14
#@Author：sky
import json
import requests


class Get_AccessToken_API():

    def __init__(self,host,port):
        self.host = host
        self.port = port

    #获取access_token
    def  get_access_token(self):
        url = f'http://{self.host}:{self.port}/qyapi.weixin.qq.com/cgi-bin/gettoken'
        res = requests.get(url)
        print(res.status_code)
        #反序列化
        result = json.loads(res.text)
        return result

