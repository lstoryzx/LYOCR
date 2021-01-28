# -*- coding:utf8 -*-
import tkinter as tk
from tkinter import ttk 
from tkinter.constants import BOTH, CENTER, E, END, LEFT, NE, NW, RIGHT, W,  X, Y
import json
import baiduocr
import tencentocr
import translationmodel as tranModel
'''
with open('api.json', 'r') as f:
    data = json.load(f)
text_value = int(data['text'])
translation_value = int(data['translation'])

win = tk.Tk()
win.title('落叶OCR')
#让窗口显示再屏幕中间
sw = win.winfo_screenwidth()
#得到屏幕宽度
sh = win.winfo_screenheight()
#得到屏幕高度
ww = 800
wh = 500
x = (sw-ww) / 2
y = (sh-wh) / 2
win.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
win.minsize(800,500)

style = ttk.Style()
style.theme_create( "MyStyle", parent="xpnative", settings={"TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0] } },"TNotebook.Tab": {"configure": {"padding": [79, 10],"font" : ('URW Gothic L', '11')},}})
style.theme_use("MyStyle")

#初始化四个选项卡
notebook = ttk.Notebook(win)
frameOne = tk.Frame()
frameTwo = tk.Frame(bg='Honeydew')
frameThree = tk.Frame(bg='Ivory')
frameFour = tk.Frame()

notebook.add(frameOne, text='文字')
notebook.add(frameTwo, text='表格')
notebook.add(frameThree, text='公式')
notebook.add(frameFour, text='二维码')
notebook.pack(fill=tk.BOTH, expand=True)

######################################################################################
'''
class Frameoneset():
    def __init__(self,frameone,text_value,translation_value,win):
        self.master = frameone
        self.text_value = text_value
        self.translation_value = translation_value
        self.root = win
        self.__UI()

    def __UI(self):
        self.frameOne_button = tk.Frame(self.master,width=800,height=75,bg='Linen')
        self.frameOne_button.pack(fill=X)
        self.frameOne_left = tk.Frame(self.master,width=400,height=300,bg='Linen')
        self.frameOne_left.pack(side=LEFT,fill=BOTH,expand=True)
        self.frameOne_right = tk.Frame(self.master,width=400,height=300,bg='Linen')
        self.frameOne_right.pack(side=RIGHT,fill=BOTH,expand=True)

        self.frameOne_conbobox1 = ttk.Combobox(self.frameOne_button,width=12,state='readonly',justify='center')
        self.frameOne_conbobox1['value'] = ('百度标准版','百度高精度版','腾讯标准版','腾讯手写版','腾讯高精度版','腾讯英文')
        self.frameOne_conbobox1.current(self.text_value)
        self.frameOne_conbobox1.bind("<<ComboboxSelected>>",self.text_ocrsetting)
        self.frameOne_conbobox1.grid(row=0, column=0, padx=32, pady=7,)
        self.frameOne_button2 = tk.Button(self.frameOne_button,width=15,height=2,text='截图识别',relief='groove',bg='Azure',activebackground='Azure',command=self.frameoneocr_button)
        self.frameOne_button2.grid(row=0, column=1, padx=32, pady=7,)
        
        self.frameOne_conbobox3 = ttk.Combobox(self.frameOne_button,width=12,state='readonly',justify='center')
        self.frameOne_conbobox3['value'] = ('百度翻译','腾讯翻译','彩云小译')
        self.frameOne_conbobox3.current(self.translation_value)
        self.frameOne_conbobox3.bind("<<ComboboxSelected>>",self.translation_ocrsetting)
        self.frameOne_conbobox3.grid(row=0, column=2, padx=32, pady=7,)

        self.frameOne_button4 = tk.Button(self.frameOne_button,width=15,height=2,text='翻译',relief='groove',bg='Azure',activebackground='Azure',command=self.trans_button)
        self.frameOne_button4.grid(row=0, column=3, padx=32, pady=7,)

        self.frameOne_ocrtext = tk.Text(self.frameOne_left,width=3,height=3,bd=0)
        self.frameOne_ocrtext.pack(padx=10,pady=10,fill=BOTH,expand=True)
        self.frameOne_translation = tk.Text(self.frameOne_right,width=3,height=3,bd=0,)
        self.frameOne_translation.pack(padx=10,pady=10,fill=BOTH,expand=True)

    def text_ocrsetting(self,event):
        apiopenation =  ('百度标准版','百度高精度版','腾讯标准版','腾讯手写版','腾讯高精度版','腾讯英文')
        api_index = apiopenation.index(self.frameOne_conbobox1.get())
        with open('api.json', 'r') as f:
            data = json.load(f)
        data['text'] = api_index
        with open('api.json', 'w') as f:
            json.dump(data, f)

    def translation_ocrsetting(self,event):
        apiopenation =  ('百度翻译','腾讯翻译','彩云小译')
        api_index = apiopenation.index(self.frameOne_conbobox3.get())
        with open('api.json', 'r') as f:
            data = json.load(f)
        data['translation'] = api_index
        with open('api.json', 'w') as f:
            json.dump(data, f)

    def frameoneocr_button(self):
        with open('apikey.json', 'r') as f:
            mergedata = json.load(f)
        merge = int(mergedata['merge'])
        with open('api.json', 'r') as f:
            data = json.load(f)
        textdata = int(data['text'])
        self.frameOne_ocrtext.delete('1.0','end')
        if merge == 1:
            if textdata == 0:
                self.root.iconify()
                ocrresult = baiduocr.baidubasic1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 1:
                self.root.iconify()
                ocrresult = baiduocr.baidu_hp1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 2:
                self.root.iconify()
                ocrresult = tencentocr.tencentocrbasic1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 3:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_script1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 4:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_hp1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 5:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_eng1()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            else:
                ocrresult = 'error'
                self.frameOne_ocrtext.insert(END,ocrresult)
        if merge == 0:
            if textdata == 0:
                self.root.iconify()
                ocrresult = baiduocr.baidubasic0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 1:
                self.root.iconify()
                ocrresult = baiduocr.baidu_hp0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 2:
                self.root.iconify()
                ocrresult = tencentocr.tencentocrbasic0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 3:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_script0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 4:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_hp0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            elif textdata == 5:
                self.root.iconify()
                ocrresult = tencentocr.tencentocr_eng0()
                self.root.deiconify()
                self.frameOne_ocrtext.insert(END,ocrresult)
            else:
                ocrresult = 'error'
                self.frameOne_ocrtext.insert(END,ocrresult)

    def trans_button(self):
        userstr = str(self.frameOne_ocrtext.get('0.0','end'))
        self.frameOne_translation.delete('1.0','end')
        with open('api.json', 'r') as f:
            transdata = json.load(f)
        translation_data = int(transdata['translation'])
        if translation_data == 0:
            resu = tranModel.baidu_trans(userstr)
            self.frameOne_translation.insert(END,resu)
        elif translation_data == 1:
            resu = tranModel.tencent_trans(userstr)
            self.frameOne_translation.insert(END,resu)
        elif translation_data == 2:
            userstr = userstr[:-1]
            resu = tranModel.caiyun_trans(userstr)
            self.frameOne_translation.insert(END,resu)
        else:
            resu = '错误'
            self.frameOne_translation.insert(END,resu)

#####################################################################################
'''
Frameoneset(frameOne,text_value,translation_value,win)
win.mainloop()
'''