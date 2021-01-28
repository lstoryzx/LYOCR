# -*- coding:utf8 -*-
import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, EXTENDED, LEFT, N, NE, NS, NW, RIGHT, SW, VERTICAL, Y

def initializejson():
    if os.path.exists('apikey.json')==0:
        api_data = {
            'baiduapi':{'APPID':'','APIKey':'','SecretKey':''},
            'tencentapi':{'SecretId':'','SecretKey':''},
            'caiyunapi':{'token':''},
            'mathpixapi':{'AppID':'','AppKey':''},
            'bdfyapi':{'AppID':'','AppKey':''},
            'merge':'1',
        }
        with open('apikey.json', 'w') as f:
            json.dump(api_data, f)

class Apiset():
    def __init__(self,win):
        self.master = win
        self.__UI()

    def __UI(self):
        with open('apikey.json', 'r') as f:
            basicdata = json.load(f)
        self.baidudata1 = basicdata['baiduapi']['APPID'] 
        self.baidudata2 = basicdata['baiduapi']['APIKey'] 
        self.baidudata3 = basicdata['baiduapi']['SecretKey'] 
        self.txdata1 = basicdata['tencentapi']['SecretId'] 
        self.txdata2 = basicdata['tencentapi']['SecretKey'] 
        self.caiyundata1 = basicdata['caiyunapi']['token'] 
        self.mathpixdata1 = basicdata['mathpixapi']['AppID'] 
        self.mathpixdata2 = basicdata['mathpixapi']['AppKey'] 
        self.bdfydata1 = basicdata['bdfyapi']['AppID']
        self.bdfydata2 = basicdata['bdfyapi']['AppKey']
        self.mergedata1 = int(basicdata['merge'])
        self.baidu1var = tk.StringVar()
        self.baidu2var = tk.StringVar()
        self.baidu3var = tk.StringVar()
        self.tx1var = tk.StringVar()
        self.tx2var = tk.StringVar()
        self.caiyun1var = tk.StringVar()
        self.mathpix1var = tk.StringVar()
        self.mathpix2var = tk.StringVar()
        self.bdfy1var = tk.StringVar()
        self.bdfy2var = tk.StringVar()
        self.baidu1var.set(self.baidudata1)
        self.baidu2var.set(self.baidudata2)
        self.baidu3var.set(self.baidudata3)
        self.tx1var.set(self.txdata1)
        self.tx2var.set(self.txdata2)
        self.caiyun1var.set(self.caiyundata1)
        self.mathpix1var.set(self.mathpixdata1)
        self.mathpix2var.set(self.mathpixdata2)
        self.bdfy1var.set(self.bdfydata1)
        self.bdfy2var.set(self.bdfydata2)
        #窗体
        self.root = tk.Frame(self.master,width=500,height=1500,)
        self.root.pack(fill=BOTH,expand=True)
        self.canvas = tk.Canvas(self.root,width=500,height=1500,scrollregion=(0,0,0,1500))
        self.scrbar = tk.Scrollbar(self.root,orient=VERTICAL)
        self.scrbar.pack(side=RIGHT,fill=Y)
        self.scrbar.configure(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrbar.set)
        self.canvas.pack(side=LEFT,fill=BOTH,expand=True)
        self.frame = tk.Frame(self.canvas,width=500,height=1500)
        self.baiduapi = tk.Frame(self.frame,width=500,height=300,)
        self.baiduapi.pack_propagate(0)
        self.baiduapi.pack()
        self.tencentapi = tk.Frame(self.frame,width=500,height=300)
        self.tencentapi.pack_propagate(0)
        self.tencentapi.pack()
        self.caiyunapi = tk.Frame(self.frame,width=500,height=300) 
        self.caiyunapi.pack_propagate(0)
        self.caiyunapi.pack()
        self.mathpixapi = tk.Frame(self.frame,width=500,height=300)
        self.mathpixapi.pack_propagate(0)
        self.mathpixapi.pack()
        self.setbutton = tk.Frame(self.frame,width=500,height=300)
        self.setbutton.pack_propagate(0)
        self.setbutton.pack()
        self.canvas.create_window((250,750),window=self.frame)
        #组件
        tk.Label(self.baiduapi,text='百度API：',font=('仿宋',15),width=15,height=3).place(x=165,y=25)
        tk.Label(self.baiduapi,text='APP ID：',font=('仿宋',12),width=15,height=3).place(x=20,y=100)
        self.baidu1 = tk.Entry(self.baiduapi,width=36,textvariable=self.baidu1var)
        self.baidu1.place(x=135,y=122)
        tk.Label(self.baiduapi,text='API Key：',font=('仿宋',12),width=15,height=3).place(x=20,y=150)
        self.baidu2 = tk.Entry(self.baiduapi,width=36,textvariable=self.baidu2var)
        self.baidu2.place(x=135,y=167)
        tk.Label(self.baiduapi,text='Secret Key：',font=('仿宋',12),width=15,height=3).place(x=20,y=200)
        self.baidu3 = tk.Entry(self.baiduapi,width=36,textvariable=self.baidu3var)
        self.baidu3.place(x=135,y=217)

        tk.Label(self.tencentapi,text='腾讯API：',font=('仿宋',15),width=15,height=3).place(x=165,y=25)
        tk.Label(self.tencentapi,text='SecretId：',font=('仿宋',12),width=15,height=3).place(x=20,y=120)
        self.tencent1 = tk.Entry(self.tencentapi,width=36,textvariable=self.tx1var)
        self.tencent1.place(x=135,y=137)
        tk.Label(self.tencentapi,text='SecretKey：',font=('仿宋',12),width=15,height=3).place(x=20,y=180)
        self.tencent2 = tk.Entry(self.tencentapi,width=36,textvariable=self.tx2var)
        self.tencent2.place(x=135,y=197)

        tk.Label(self.caiyunapi,text='彩云小译：',font=('仿宋',15),width=15,height=3).place(x=165,y=25)
        tk.Label(self.caiyunapi,text='token：',font=('仿宋',12),width=15,height=3).place(x=20,y=120)
        self.caiyun1 = tk.Entry(self.caiyunapi,width=36,textvariable=self.caiyun1var)
        self.caiyun1.place(x=135,y=137)

        tk.Label(self.mathpixapi,text='Mathpix API：',font=('仿宋',15),width=15,height=3).place(x=165,y=25)
        tk.Label(self.mathpixapi,text=' App ID：',font=('仿宋',12),width=15,height=3).place(x=20,y=120)
        self.mathpix1 = tk.Entry(self.mathpixapi,width=36,textvariable=self.mathpix1var)
        self.mathpix1.place(x=135,y=137)
        tk.Label(self.mathpixapi,text=' App Key：',font=('仿宋',12),width=15,height=3).place(x=20,y=180)
        self.mathpix2 = tk.Entry(self.mathpixapi,width=36,textvariable=self.mathpix2var)
        self.mathpix2.place(x=135,y=197)

        tk.Label(self.setbutton,text='百度翻译 API：',font=('仿宋',15),width=15,height=3).place(x=165,y=0)
        tk.Label(self.setbutton,text=' App ID：',font=('仿宋',12),width=15,height=3).place(x=20,y=75)
        self.bdfy1 = tk.Entry(self.setbutton,width=36,textvariable=self.bdfy1var)
        self.bdfy1.place(x=135,y=92)
        tk.Label(self.setbutton,text=' App Key：',font=('仿宋',12),width=15,height=3).place(x=20,y=135)
        self.bdfy2 = tk.Entry(self.setbutton,width=36,textvariable=self.bdfy2var)
        self.bdfy2.place(x=135,y=152)

        tk.Label(self.setbutton,text='自动合并:',font=('仿宋',15),width=15,height=3).place(x=7,y=185)
        self.mergeconbobox = ttk.Combobox(self.setbutton,width=5,state='readonly',justify='center')
        self.mergeconbobox['value'] = ('NO','YES')
        self.mergeconbobox.current(self.mergedata1)
        self.mergeconbobox.bind("<<ComboboxSelected>>",self.mergesetting)
        self.mergeconbobox.place(x=50,y=245)

        tk.Button(self.setbutton,text='保存设置',font=('仿宋',15),width=10,height=3,relief='groove',bg='Azure',activebackground='Azure',command=self.getkey).place(x=350,y=200)

    def mergesetting(self,event):
        mergeopenation =  ('NO','YES')
        mergeindex = mergeopenation.index(self.mergeconbobox.get())
        with open('apikey.json', 'r') as f:
            merge_data = json.load(f)
        merge_data['merge'] = str(mergeindex)
        with open('apikey.json', 'w') as f:
            json.dump(merge_data, f)
        

    def getkey(self):
        with open('apikey.json', 'r') as f:
            newdata = json.load(f)
        newdata['baiduapi']['APPID'] = str(self.baidu1var.get())
        newdata['baiduapi']['APIKey'] = str(self.baidu2var.get())
        newdata['baiduapi']['SecretKey'] = str(self.baidu3var.get())

        newdata['tencentapi']['SecretId'] = str(self.tx1var.get())
        newdata['tencentapi']['SecretKey'] = str(self.tx2var.get())

        newdata['caiyunapi']['token'] = str(self.caiyun1var.get())

        newdata['mathpixapi']['AppID'] = str(self.mathpix1var.get())
        newdata['mathpixapi']['AppKey'] = str(self.mathpix2var.get())

        newdata['bdfyapi']['AppID'] = str(self.bdfy1var.get())
        newdata['bdfyapi']['AppKey'] = str(self.bdfy2var.get())
        with open('apikey.json', 'w') as f:
            json.dump(newdata, f)



