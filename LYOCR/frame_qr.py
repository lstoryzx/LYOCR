# -*- coding:utf8 -*-
import tkinter as tk
from tkinter.constants import BOTH, CENTER, E, END, LEFT, NE, NW, RIGHT, W,  X, Y
import tencentocr


'''

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
qeframe = tk.Frame(win,width=800,height=225,)
qeframe.pack(fill=X)
######################################################################################
'''
class Frameqrset():
    def __init__(self,qrframe,win):
        self.master = qrframe
        self.root = win
        self.__UI()
    def __UI(self):
        self.frameqr_button = tk.Frame(self.master,width=200,height=225,)
        self.frameqr_button.pack(side = LEFT,fill=Y)
        self.frameqr_result = tk.Frame(self.master,width=600,height=225,)
        self.frameqr_result.pack(side= RIGHT,fill=BOTH,expand=True)
        self.frameqr_button1 = tk.Button(self.frameqr_button,width=15,height=2,text='截图识别',relief='groove',bg='Azure',activebackground='Azure',command=self.frameqrocr_button,)
        self.frameqr_button1.pack(padx=90, pady=85)
        self.frameqr_result2 = tk.Text(self.frameqr_result,width=3,height=3,bd=0)
        self.frameqr_result2.pack(padx=30,pady=30,fill=BOTH,expand=True)
    def frameqrocr_button(self):
        self.frameqr_result2.delete('1.0','end')
        self.root.iconify()
        ocrresult = tencentocr.tencent_qr()
        self.root.deiconify()
        self.frameqr_result2.insert(END,ocrresult)

#####################################################################################
'''
Frameqrset(qeframe,win)
win.mainloop()
'''