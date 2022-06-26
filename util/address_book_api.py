# -*- coding: utf-8 -*-
#@time :2022-05-22 14:14
#@Author：sky
import json
import requests


class Address_Book_API():

    # def __init__(self,host,port):
    #     self.host = host
    #     self.port = port

    #获取access_token
    def  get_access_token(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        data = {
            "corpid":"ww69eaf3b7176fe4f5",
            "corpsecret":"MmA23kY75YDI6ZHshoqS9GBDNcJUDmdMmeYFPqetehw"
            }
        res = requests.get(url,params=data)
        print(res.status_code)
        #反序列化
        result = json.loads(res.text)
        return result["access_token"]

    #创建成员
    def create_personel(self,access_token,userid,name,mobile,department,email,extattr_type,extattr_name,extattr_text_value,extattr_web_url,extattr_web_title,\
                        access_token_flag=1,userid_flag=1,name_flag=1,mobile_flag=1,department_flag=1,email_flag=1,extattr_type_flag=1,extattr_name_flag=1,extattr_text_value_flag=1,extattr_web_url_flag=1,extattr_web_title_flag=1):
        if access_token_flag:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
        else:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"

        data = {}
        if userid_flag:
            data["userid"] = userid

        if name_flag:
            data["name"] = name

        if mobile_flag:
            data["mobile"] = mobile

        if department_flag:
            data["department"] = department

        if email_flag:
            data["email"] = email

        if extattr_type_flag:
            data["extattr.type"] = extattr_type

        if extattr_name_flag:
            data["extattr.name"] = extattr_name

        if extattr_text_value_flag:
            data["extattr.text.value"] = extattr_text_value

        if extattr_web_url_flag:
            data["extattr.web.url"] = extattr_web_url

        if extattr_web_title_flag:
            data["extattr.web.title"] = extattr_web_title

        print(url)
        print(data)
        res = requests.post(url,json=data)
        code = res.status_code
        content = json.loads(res.text)

        return code,content

    def create_personel_new(self,url,data):
        print(url)
        print(data)
        res = requests.post(url,json=data)
        code = res.status_code
        content = json.loads(res.text)

        return code,content

    #查询成员
    def query_personel(self,access_token=None,userid=None,access_token_flag=1,userid_flag=1):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        if access_token_flag and userid_flag:
            url =f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={userid}"
        elif access_token_flag:
            url =f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}"
        elif userid_flag:
            url =f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        else:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"

        res = requests.get(url)

        code = res.status_code
        content = json.loads(res.text)

        return code,content


    #更新成员
    #删除成员

if __name__ == '__main__':
    AB = Address_Book_API()
    access_token = AB.get_access_token()
    cp = AB.create_personel(access_token,"test01","测试01","13120000000",[1],"test01@163.com",0,"test","ssssddddd","https://www.baidu.com","tongxunlu",userid_flag=0)
    print(cp[0])
    print(cp[1])