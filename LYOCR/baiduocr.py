# -*- coding:utf8 -*-
from aip import AipOcr
import json
import time
from screenshots import baiduimage
def baidukey():
    with open('apikey.json', 'r') as f:
            data = json.load(f)
    APP_ID = data['baiduapi']['APPID']
    API_KEY = data['baiduapi']['APIKey']
    SECRET_KEY = data['baiduapi']['SecretKey']
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

def baidubasic1():
    options = {}
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    image = baiduimage()
    client = baidukey()
    response = client.basicAccurate(image, options)
    alpha =''
    for gama in response['words_result']:
        alpha += gama['words']
    return alpha

def baidubasic0():
    options = {}
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    image = baiduimage()
    client = baidukey()
    response = client.basicAccurate(image, options)
    alpha =''
    for gama in response['words_result']:
        alpha =alpha+ gama['words']+'\n'
    return alpha

def baidu_hp1():
    options = {}
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    image = baiduimage()
    client = baidukey()
    response = client.basicAccurate(image, options)
    alpha =''
    for gama in response['words_result']:
        alpha += gama['words']
    return alpha

def baidu_hp0():
    options = {}
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    image = baiduimage()
    client = baidukey()
    response = client.basicAccurate(image, options)
    alpha =''
    for gama in response['words_result']:
        alpha =alpha+ gama['words']+'\n'
    return alpha

def baidu_table():
    image = baiduimage()
    client = baidukey()
    response = client.tableRecognitionAsync(image)
    requestId = response['result'][0]['request_id']
    time.sleep(7)
    options = {}
    options["result_type"] = "excel"
    resu = client.getTableRecognitionResult(requestId, options)
    alpha = resu['result']['result_data']
    return alpha
