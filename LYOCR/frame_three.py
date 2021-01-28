# -*- coding:utf8 -*-
import tkinter as tk
from tkinter import ttk 
from tkinter.constants import BOTH, CENTER, E, END, LEFT, NE, NW, RIGHT, W,  X, Y
import json
import mathpixocr
import tencentocr
'''
with open('api.json', 'r') as f:
    data = json.load(f)
math_value = int(data['math'])

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
frameTwo = tk.Frame()
frameThree = tk.Frame(bg='Ivory')
frameFour = tk.Frame()

notebook.add(frameOne, text='文字')
notebook.add(frameTwo, text='表格')
notebook.add(frameThree, text='公式')
notebook.add(frameFour, text='二维码')
notebook.pack(fill=tk.BOTH, expand=True)
'''
######################################################################################
class Framethreeset():
    def __init__(self,framethree,math_value,win):
        self.master = framethree
        self.math_value = math_value
        self.root = win
        self.__UI()

    def __UI(self):
        self.framethree_button = tk.Frame(self.master,width=800,height=75,bg='floralwhite')
        self.framethree_button.pack(fill=X)
        self.framethree_button.columnconfigure(0, weight = 1)
        self.framethree_button.columnconfigure(1, weight = 1)
        self.framethree_left = tk.Frame(self.master,width=400,height=300,bg='floralwhite')
        self.framethree_left.pack(side=LEFT,fill=BOTH,expand=True)
        self.framethree_right = tk.Frame(self.master,width=400,height=300,bg='floralwhite')
        self.framethree_right.pack(side=RIGHT,fill=BOTH,expand=True)

        self.framethree_conbobox1 = ttk.Combobox(self.framethree_button,width=10,state='readonly',justify='center')
        self.framethree_conbobox1['value'] = ('Mathpix','腾讯公式识别')
        self.framethree_conbobox1.current(self.math_value)
        self.framethree_conbobox1.bind("<<ComboboxSelected>>",self.math_ocrsetting)
        self.framethree_conbobox1.grid(row=0, column=0, padx=100, pady=15,)
        self.framethree_button2 = tk.Button(self.framethree_button,width=15,height=2,text='截图识别',relief='groove',bg='Azure',activebackground='Azure',command=self.framethreemath_button)
        self.framethree_button2.grid(row=0, column=1, padx=100, pady=10,)

        self.framethree_latextext = tk.Text(self.framethree_left,width=3,height=3,bd=0)
        self.framethree_latextext.pack(padx=10,pady=10,fill=BOTH,expand=True)
        self.framethree_mathmltext = tk.Text(self.framethree_right,width=3,height=3,bd=0,)
        self.framethree_mathmltext.pack(padx=10,pady=10,fill=BOTH,expand=True)

    def math_ocrsetting(self,event):
        mathopenaiton = ('Mathpix','腾讯公式识别')
        math_index = mathopenaiton.index(self.framethree_conbobox1.get())
        with open('api.json', 'r') as f:
            data = json.load(f)
        data['math'] = math_index
        with open('api.json', 'w') as f:
            json.dump(data, f)

    def framethreemath_button(self):
        with open('api.json', 'r') as f:
            mathdata = json.load(f)
        mathocrdata = int(mathdata['math'])
        self.framethree_latextext.delete('1.0','end')
        self.framethree_mathmltext.delete('1.0','end')
        if mathocrdata == 0:
            self.root.iconify()
            ocrresult = mathpixocr.mathtext()
            self.root.deiconify()
            mathmlresu = ocrresult[0]
            latexresu = ocrresult[1]
            self.framethree_latextext.insert(END,latexresu)
            self.framethree_mathmltext.insert(END,mathmlresu)
        elif mathocrdata == 1:
            self.root.iconify()
            ocrresult = tencentocr.tencent_math()
            self.root.deiconify()
            self.framethree_latextext.insert(END,ocrresult)
        else:
            ocrresult = 'error'
            self.framethree_latextext.insert(END,ocrresult)
''''
#####################################################################################

Framethreeset(frameThree,math_value,win)
win.mainloop()
'''