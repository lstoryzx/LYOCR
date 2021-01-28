# -*- coding:utf8 -*-
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
from screenshots import get_image_data
import pandas as pd
import datetime
import openpyxl
import json
import re
import base64

def tencentkey():
    with open('apikey.json', 'r') as f:
            data = json.load(f)
    Secret_Id = data['tencentapi']['SecretId']
    SECRET_KEY = data['tencentapi']['SecretKey']
    cred = credential.Credential( Secret_Id , SECRET_KEY)
    return cred

def tencentocrbasic1():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.GeneralBasicOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralBasicOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText
    return alpha

def tencentocrbasic0():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.GeneralBasicOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralBasicOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText+'\n'
    return alpha

def tencentocr_script1():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.GeneralHandwritingOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralHandwritingOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText
    return alpha

def tencentocr_script0():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.GeneralHandwritingOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralHandwritingOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText+'\n'
    return alpha

def tencentocr_hp1():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred , "ap-beijing", clientProfile) 
    req = models.GeneralAccurateOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralAccurateOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText
    return alpha

def tencentocr_hp0():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred , "ap-beijing", clientProfile) 
    req = models.GeneralAccurateOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.GeneralAccurateOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText+'\n'
    return alpha

def tencentocr_eng1():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.EnglishOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.EnglishOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText
    return alpha

def tencentocr_eng0():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.EnglishOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.EnglishOCR(req) 
    alpha = ''
    for gama in resp.TextDetections:
        alpha = alpha + gama.DetectedText+'\n'
    return alpha

def tencent_table():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
    req = models.RecognizeTableOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.RecognizeTableOCR(req)
    result1 = json.loads(resp.to_json_string())
    rowIndex = []
    colIndex = []
    content = []
    for item in result1['TableDetections']:
        for item2 in item['Cells']:
            rowIndex.append(item2['RowTl'])
            colIndex.append(item2['ColTl'])
            content.append(item2['Text'])
    rowIndex = pd.Series(rowIndex)
    colIndex = pd.Series(colIndex)
    index = rowIndex.unique()
    index.sort()
    columns = colIndex.unique()
    columns.sort()
    data = pd.DataFrame(index = index, columns = columns)
    for i in range(len(rowIndex)):
        data.loc[rowIndex[i],colIndex[i]] = re.sub(" ","",content[i])
    excelname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    excel_path = './Tables/'+excelname+'.xlsx'
    data.to_excel(excel_path)
    alpha = result1['Data']
    return alpha

def tencent_qr():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.QrcodeOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.QrcodeOCR(req) 
    alpha = ''
    for gama in resp.CodeResults:
        alpha = alpha + gama.Url+'\n'
    return alpha

def tencent_math():
    cred = tencentkey()
    base64data = get_image_data()
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 
    req = models.FormulaOCRRequest()
    params = {
        "ImageBase64": base64data
    }
    req.from_json_string(json.dumps(params))
    resp = client.FormulaOCR(req) 
    alpha = ''
    for gama in resp.FormulaInfos:
        alpha = alpha + gama.DetectedText+'\n'
    return alpha