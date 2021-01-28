# -*- coding:utf8 -*-
import requests
import http.client
import hashlib
import urllib
import random
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

def baidu_trans(userstr):
    with open('apikey.json', 'r') as f:
        keydata = json.load(f)
    appid = keydata['bdfyapi']['AppID']  # 填写你的appid
    secretKey = keydata['bdfyapi']['AppKey']  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q= userstr
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)
    alpha = ''
    for gama in result['trans_result']:
        alpha += gama['dst']
    if httpClient:
        httpClient.close()
    return alpha

def caiyun_trans(userstr):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    with open('apikey.json', 'r') as f:
        keydata = json.load(f)
    token = keydata['caiyunapi']['token']  # 填写你的密钥
    payload = {
            "source" : userstr, 
            "trans_type" : "en2zh",
            "request_id" : "demo",
            "detect": True,
            }
    headers = {
            'content-type': "application/json",
            'x-authorization': "token " + token,
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    result =  json.loads(response.text)['target']
    return result

def tencent_trans(userstr):
    with open('apikey.json', 'r') as f:
            data = json.load(f)
    Secret_Id = data['tencentapi']['SecretId']
    SECRET_KEY = data['tencentapi']['SecretKey']
    cred = credential.Credential( Secret_Id , SECRET_KEY)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tmt.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile) 
    req = models.TextTranslateRequest()
    params = {
        "SourceText": userstr, 
        "Source": "auto",
        "Target": "zh",
        "ProjectId": 0
    }
    req.from_json_string(json.dumps(params))
    resp = client.TextTranslate(req) 
    resu = resp.TargetText
    return resu
