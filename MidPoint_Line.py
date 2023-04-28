import tkinter as tk
import numpy as np
import cv2

def click() :
    x1_int = int(x1.get())
    x2_int = int(x2.get())
    y1_int = int(y1.get())
    y2_int = int(y2.get())

    img = np.zeros((500,500,3),np.uint8)
    img = cv2.line(img,(x1_int,y1_int),(x1_int,y1_int),(255,0,0),10)
    cv2.imshow("img",img)







window = tk.Tk()

x1 = tk.StringVar()
x2 = tk.StringVar()
y1 = tk.StringVar()
y2 = tk.StringVar()

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

execute_button = tk.Button(window , text="선 그리기" , command=click).grid(column=400,row=5)


window.mainloop()
