# -*- coding:utf8 -*-
import json
import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.constants import BOTH, CENTER, E, LEFT, NE, NW, RIGHT, W,  X, Y
import apikeysetting as aks
import frame_one
import frame_two
import frame_three
import frame_qr
import os
#初始化配置文件
aks.initializejson()
#用于存放表格的文件夹
if not ('Tables') in os.listdir():
    os.mkdir("./Tables/")
#读取配置
with open('api.json', 'r') as f:
    data = json.load(f)
text_value = int(data['text'])
translation_value = int(data['translation'])
table_value = int(data['table'])
math_value = int(data['math'])
#初始化窗口
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
win.iconbitmap('.\\logo.ico')
#自定义样式
style = ttk.Style()
style.theme_create( "MyStyle", parent="xpnative", settings={"TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0] } },"TNotebook.Tab": {"configure": {"padding": [79, 10],"font" : ('URW Gothic L', '11')},}})
style.theme_use("MyStyle")

#初始化四个选项卡
notebook = ttk.Notebook(win)
frameOne = tk.Frame()
frameTwo = tk.Frame()
frameThree = tk.Frame(bg='Ivory')
frameFour = tk.Frame()

notebook.add(frameOne, text='文字')
notebook.add(frameTwo, text='表格')
notebook.add(frameThree, text='公式')
notebook.add(frameFour, text='二维码')
notebook.pack(fill=tk.BOTH, expand=True)
#文本
frame_one.Frameoneset(frameOne,text_value,translation_value,win)
#表格
frame_two.Frametwoset(frameTwo,table_value,win)
#公式
frame_three.Framethreeset(frameThree,math_value,win)
#二维码
frameqr = tk.Frame(frameFour,width=800,height=225,bg='Azure')
frameqr.pack(fill=X)
frame_qr.Frameqrset(frameqr,win)

#about
framesetting = tk.Frame(frameFour,width=800,height=200,)
framesetting.pack(fill=BOTH,expand=True)

framesetleft = tk.Frame(framesetting,width=400,height=200,)
framesetleft.pack(side=LEFT,fill=BOTH,expand=True)
framesetright = tk.Frame(framesetting,width=400,height=200,)
framesetright.pack(side=RIGHT,fill=BOTH,expand=True)

ocrlable = tk.Label(framesetleft,text='项目地址：',font=('仿宋', 15), width=10, height=2)
ocrlable.pack(padx=15,pady=15,anchor=NW)
github = tk.Label(framesetleft,text='Github: https://github.com/lstoryzx/LYOCR',width=50,height=2)
github.pack(anchor=NW,padx=5,pady=10)    

gitee = tk.Label(framesetleft,text='Gitee: https://gitee.com/lstoryzx/lyocr',width=50,height=2)
gitee.pack(anchor=NW,padx=5,pady=10)    

def apisetting():
    api_set = tk.Toplevel()
    api_set.title('API设置')
    api_set.geometry('500x400')
    api_set.resizable(0, 0)
    api_set.iconbitmap('.\\logo.ico')
    aks.Apiset(api_set)

apibutton = tk.Button(framesetright,text='API设置',font=('仿宋', 15), width=15, height=3,relief='groove',bg='Azure',activebackground='Azure',command=apisetting)
apibutton.pack(padx=20,pady=100)

win.mainloop()
