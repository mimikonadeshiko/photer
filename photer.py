import tkinter
from tkinter import colorchooser,filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os
import sys

tki = tkinter.Tk()
tki.geometry('400x300')
tki.title('photer')
fle = 0
def photofle():
    txt1.delete(0, tkinter.END)
    typ=[('', '*')]
    dir = ''
    global fle
    fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 
    print (fle)
    img = Image.open(fle)
    fleconfig = img.size,img.format
    txt1.insert(tkinter.END,fleconfig)
    



def guresuke():
    global fle
    img = Image.open(fle)
    new_img = img.convert('L')
    if os.path.isfile(fle + "new.png"):
        print ("許可済")
        ret = messagebox.askyesno('確認', 'すでに同じ名前のファイルがあります処理を続行しますか?')
        if ret == True:
            new_img.save(fle + "new.png")

    else:
        print ("未許可")
def mozaiku():
    resize1 = 1
    mozaleve = rdo_var.get()
    #print (mozaleve)
    global fle
    if mozaleve == 0:
        resize1 = 8
    elif mozaleve == 1:
        resize1 = 16
    elif mozaleve == 2:
        resize1 = 32
    img = Image.open(fle)
    
    new_img = img.resize((int(img.size[0]/resize1),int(img.size[1]/resize1))).resize((img.size[0], img.size[1]), resample=Image.NEAREST)
    if os.path.isfile(fle + "new.png"):
        print ("許可済")
        ret = messagebox.askyesno('確認', 'すでに同じ名前のファイルがあります処理を続行しますか?')
        if ret == True:
            new_img.save(fle + "new.png")

    else:
        print ("未許可")
def text():
    global fle
    xjiku = txt2.get()
    yjiku = txt3.get()
    print (xjiku)
    print (yjiku)
    size012 = var.get()
    if size012 == 0:
        size = 16
    elif size012 == 1:
        size = 32
    elif size012 == 2:
        size = 64
            
    color = colorchooser.askcolor()
    intext = txt.get()
    img = Image.open(fle)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('SourceHanSansJP-Bold', size)
    draw.text((int(xjiku), int(yjiku)),intext,color[0], font=font)
    if os.path.isfile(fle + "new.png"):
        print ("許可済")
        ret = messagebox.askyesno('確認', 'すでに同じ名前のファイルがあります処理を続行しますか?')
        if ret == True:
            img.save(fle + "new.png")

    else:
        print ("未許可")
def purebyu():
    # 画面作成
    window = tkinter.Tk()
    window.title("プレビュー")
    img = Image.open(fle)

    # キャンバス作成
    canvas = tkinter.Canvas(window, bg="#ffffff", height=200, width=200)
    img = tkinter.PhotoImage(file=fle + "new.png", width=1920, height=1080, master=window)
    canvas.create_image(30, 30, image=img, anchor=tkinter.NW )
    # キャンバス表示
    canvas.place(x=0, y=0)
    window.mainloop()
 

btn = tkinter.Button(tki, text='参照', command=photofle)
btn.place(x=40, y=30)
btn1 = tkinter.Button(tki, text='モノクロ', command=guresuke)
btn1.place(x=70, y=30)
btn2 = tkinter.Button(tki, text='モザイク', command=mozaiku)
btn2.place(x=120, y=30)
btn3 = tkinter.Button(tki, text='文字入れ', command=text)
btn3.place(x=200, y=30)
btn4 = tkinter.Button(tki, text='プレビュー', command=purebyu)
btn4.place(x=320, y=280)
txt1 = tkinter.Entry(width=20)
txt1.place(x=100, y=5)
txt2 = tkinter.Entry(width=5)
txt2.place(x=250, y=60)
txt2.insert(tkinter.END,"X軸")
txt3 = tkinter.Entry(width=5)
txt3.place(x=340, y=60) 
txt3.insert(tkinter.END,"Y軸")

var = tkinter.IntVar()

rdo1 = tkinter.Radiobutton(tki, value=0, variable=var, text='16')
rdo1.place(x=200, y=55)

rdo2 = tkinter.Radiobutton(tki, value=1, variable=var, text='32')
rdo2.place(x=200, y=75)

rdo3 = tkinter.Radiobutton(tki, value=2, variable=var, text='64')
rdo3.place(x=200, y=95)
# ラベル
lbl = tkinter.Label(text='入れる文字')
lbl.place(x=20, y=130)

# テキストボックス
txt = tkinter.Entry(width=20)
txt.place(x=90, y=130)

# ラジオボタンのラベルをリスト化する
rdo_txt = ['1モザイク8px','1モザイク16px','1モザイク32px']
# ラジオボタンの状態
rdo_var = tkinter.IntVar()

# ラジオボタンを動的に作成して配置
for i in range(len(rdo_txt)):
    rdo = tkinter.Radiobutton(tki, value=i, variable=rdo_var, text=rdo_txt[i]) 
    rdo.place(x=60, y=50 + (i * 24))


tki.mainloop()