import tkinter as tk
import numpy as np
import cv2

def translation(dx,dy):
    arr=[[1,0,dx],[0,1,dy],[0,0,1]]

def RightMPLA(x1_int , y1_int , x2_int , y2_int):
    img = np.zeros((500,500,3),np.uint8)
    dx = x2_int-x1_int
    dy = y2_int-y1_int

    if dy>=0 :
        if dx>=dy:
            d = dy*2-dx
            dE = dy*2
            dNE = (dy-dx)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while x < x2_int:
                if d<=0:
                    d=d+dE
                    x=x+1
                else:
                    d = d+dNE
                    x=x+1
                    y=y+1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

        else:
            d = dx*2-dy
            dN = dx*2
            dNE = (dx-dy)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while y<y2_int:
                if d<=0:
                    d=d+dN
                    y=y+1
                else:
                    d=d+dNE
                    x=x+1
                    y=y+1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

    else:
        dy = -1*dy
        if dx>=dy:
            d = dy*2-dx;
            dE = dy*2;
            dSE = (dy-dx)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while x<x2_int:
                if d<=0:
                    d=d+dE
                    x=x+1
                else:
                    d=d+dSE
                    x=x+1
                    y=y-1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

        else:
            d = dx*2-dy;
            dS = dx*2;
            dSE = (dx-dy)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while y>y2_int:
                if d<=0:
                    d=d+dS
                    y=y-1
                else:
                    d=d+dSE
                    x=x+1
                    y=y-1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
    cv2.imshow("img",img)


def LeftMPLA(x1_int , y1_int , x2_int , y2_int):
    img = np.zeros((500,500,3),np.uint8)
    dx = x2_int-x1_int
    dy = y2_int-y1_int

    dx=-1*dx

    if dy<=0 :
        dy=-1*dy
        if dx>=dy:
            d = dy*2-dx
            dW = dy*2
            dSW = (dy-dx)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while x > x2_int:
                if d<0:
                    d=d+dW
                    x=x-1
                else:
                    d = d+dSW
                    x=x-1
                    y=y-1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

        else:
            d = dx*2-dy
            dS = dx*2
            dSW = (dx-dy)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while y>y2_int:
                if d<0:
                    d=d+dS
                    y=y-1
                else:
                    d=d+dSW
                    x=x-1
                    y=y-1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

    else:

        if dx>=dy:
            d = dy*2-dx;
            dW = dy*2;
            dNW = (dy-dx)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while x>x2_int:
                if d<0:
                    d=d+dW
                    x=x-1
                else:
                    d=d+dNW
                    x=x-1
                    y=y+1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)

        else:
            d = dx*2-dy;
            dN = dx*2;
            dNW = (dx-dy)*2
            x=x1_int
            y=y1_int
            img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
            while y<y2_int:
                if d<0:
                    d=d+dN
                    y=y+1
                else:
                    d=d+dNW
                    x=x-1
                    y=y+1
                img = cv2.line(img,(x,y),(x,y),(255,0,0),5)
    cv2.imshow("img",img)
def click() :
    x1_int = int(x1.get())
    y1_int = int(y1.get())
    x2_int = int(x2.get())
    y2_int = int(y2.get())
    dx_int = int(Translation_dx.get())
    dy_int = int(Translation_dy.get())

    if x2_int-x1_int>=0 and dx_int==0 and dy_int==0:
        RightMPLA(x1_int,y1_int,x2_int,y2_int)
    elif x2_int-x1_int>=0 and (dx_int!=0 or dy_int!=0):
        RightMPLA(x1_int+dx_int,y1_int+dy_int,x2_int+dx_int,y2_int+dy_int)
    elif x2_int-x1_int<0 and dx_int==0 and dy_int==0:
        LeftMPLA(x1_int,y1_int,x2_int,y2_int)
    elif x2_int-x1_int<0 and (dx_int!=0 or dy_int!=0):
        LeftMPLA(x1_int+dx_int,y1_int+dy_int,x2_int+dx_int,y2_int+dy_int)











window = tk.Tk()

x1 = tk.StringVar()
x2 = tk.StringVar()
y1 = tk.StringVar()
y2 = tk.StringVar()
Translation_dx = tk.StringVar()
Translation_dy = tk.StringVar()

window.title("21812082 컴퓨터공학과 박민기 MidPoint_Algorithm 과제")
window.geometry("640x400+100+100")


lab1 = tk.Label(window , text= "첫번째 X좌표와 Y좌표를 입력하시오").grid(column=1,row=1)
lab_tmp1 = tk.Label(window , text= "X좌표").grid(column=2,row=1)
input_x1 = tk.Entry(window, width = 10 , textvariable=x1).grid(column=3 , row = 1)
lab_tmp2 = tk.Label(window , text= "Y좌표").grid(column=4,row=1)
input_y1 = tk.Entry(window,width = 10,textvariable=y1).grid(column=5,row=1)

lab2 = tk.Label(window , text="두번째 X좌표와 Y좌표를 입력하시오").grid(column=1,row = 2)
lab_tmp3 = tk.Label(window , text= "X좌표").grid(column=2,row=2)
input_x2 = tk.Entry(window, width = 10,textvariable=x2).grid(column=3 , row = 2)
lab_tmp4 = tk.Label(window , text= "Y좌표",).grid(column=4,row=2)
input_y2 = tk.Entry(window,width = 10,textvariable=y2).grid(column=5,row = 2)

lab2 = tk.Label(window , text="Translation 변환을 위한 dx , dy를 입력하시오").grid(column=1,row = 3)
lab_tmp3 = tk.Label(window , text= "X좌표 변화량").grid(column=2,row=3)
input_x2 = tk.Entry(window, width = 10,textvariable=Translation_dx).grid(column=3 , row = 3)
lab_tmp4 = tk.Label(window , text= "Y좌표 변화량",).grid(column=4,row=3)
input_y2 = tk.Entry(window,width = 10,textvariable=Translation_dy).grid(column=5,row = 3)

execute_button = tk.Button(window , text="선 그리기" , command=click).grid(column=400,row=3)


window.mainloop()
