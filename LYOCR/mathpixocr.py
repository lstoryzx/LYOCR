# -*- coding:utf8 -*-
import base64
import requests
import json
import screenshots

def mathpixkey():
    with open('apikey.json', 'r') as f:
            data = json.load(f)
    math_Id = data['mathpixapi']['AppID']
    math_KEY = data['mathpixapi']['AppKey']
    myheader = {
        "content-type": "application/json",
        "app_id": math_Id,
        "app_key": math_KEY
    }
    return myheader

def mathtext():
    img = screenshots.baiduimage()
    image_uri = "data:image/jpg;base64," + base64.b64encode(img).decode()
    header = mathpixkey()
    postdata = {
                "src": image_uri,
                "formats": ["text", "data"],
                "data_options": {
                    "include_mathml": True,
                    "include_latex": True
                }
            }
    r = requests.post("https://api.mathpix.com/v3/text",
    data=json.dumps(postdata),
    headers=header)
    resp = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    result = json.loads(resp)
    alpha = []
    for gama in result['data']:
        alpha.append(gama['value'])
    return alpha
