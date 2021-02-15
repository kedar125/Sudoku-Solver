import tkinter
import tkinter as tk
from tkinter import *
import tkinter.font as font
from second import create
from second import e
from sudoku import inputa
import question
from question import qdisplay

def dest(f): #TO DESTROY FRAME
    f.destroy()

def p1():  #STRATING FRAME/SCREEN

    window.geometry('770x570')

    frame1 = LabelFrame(window, text="Sudoku", padx=150, pady=150, fg="green")

    l1 = Label(frame1, text="WELCOME TO SUDOKU SOLVER!!!", fg="red", padx=40, pady=40, font="Arial", bg="yellow")
    l1.grid(row=0, column=0, padx=10, pady=10)
    l1['font'] = myFont

    b11 = Button(frame1, text="START",command=lambda: p3(frame1), bg="green", fg="pink")
    b11.grid(row=1, column=0)
    b11['font'] = myFont
    b12 = Button(frame1, text="CLOSE",command=lambda: dest(window), bg="orange", fg="brown")
    b12.grid(row=2, column=0, padx=15, pady=5)
    b12['font'] = myFont

    frame1.pack(padx=10, pady=10)

def p3(previousf):  # MENU OPTION FRAME
    dest(previousf)
    window.geometry('570x580')
    frame3 = LabelFrame(window, text="Sudoku", padx=100, pady=80, fg="green")
    frame3.grid(padx=30, pady=10)

    l31 = Label(frame3, text="***  MENU  ***", fg="red", padx=60, pady=20, font="Arial", bg="deep sky blue")
    l31.grid(row=2, column=0, rowspan=2, columnspan=55, padx=20, pady=30)
    l31['font'] = myFont

    b31 = Button(frame3, text="SOLVER", command=lambda: p2(frame3), bg="SpringGreen2", fg="purple3")
    b31.grid(padx=10, pady=20, row=25, column=3, columnspan=4)
    b31['font'] = myFont

    b32 = Button(frame3, text="TRY SOME QUESTIONS",command=lambda: p4(frame3), bg="SpringGreen2", fg="purple3",padx=25)
    b32.grid(padx=10, pady=20, row=26, column=3, columnspan=4)
    b32['font'] = myFont

    b33 = Button(frame3, text="BACK", command=lambda: back(frame3), bg="SpringGreen2", fg="black")
    b33.grid(padx=10, pady=20, row=27, column=3, columnspan=4)
    b33['font'] = myFont

def p2(previousf): # SOLVER FRAME

    dest(previousf)
    window.geometry('750x800')
    frame2 = LabelFrame(window,text="Sudoku", padx=100, pady=80, fg="green")
    frame2.grid(padx=30, pady=10)

    create(frame2)

    l21 = Label(frame2, text="Enter you inputs and then click solve",fg="red")
    l21.grid(row=2,column=0, rowspan=2,columnspan=55,padx=20,pady=30)
    l21['font'] = myFont

    b21 = Button(frame2, text="SOLVE",command=lambda: inputa(frame2), bg="yellow", fg="purple")
    b21.grid(padx=10,pady=20,row=25,column=3,columnspan=4)
    b21['font'] = myFont

    b22 = Button(frame2, text="RESET", command=lambda: reset(frame2), bg="khaki1", fg="black")
    b22.grid(padx=10, pady=20, row=25, column=8,columnspan=4)
    b22['font'] = myFont

    b23 = Button(frame2, text="MENU", command=lambda: p3(frame2), bg="alice blue", fg="blue2")
    b23.grid(padx=10, pady=20, row=26, column=3, columnspan=4)
    b23['font'] = myFont

    b24 = Button(frame2, text="EXIT", command=lambda: dest(window), bg="hot pink", fg="red")
    b24.grid(padx=10, pady=20, row=26, column=8, columnspan=4)
    b24['font'] = myFont

    frame2.pack(padx=10, pady=10)

def p4(previousf): # QUESTION DIFFICULTY CHOICE FRAME
    dest(previousf)

    window.geometry('600x560')
    frame4 = LabelFrame(window, text="Sudoku", padx=100, pady=30, fg="green")
    frame4.grid(padx=30, pady=10)

    l41 = Label(frame4, text="DIFFICULTY LEVEL", fg="gray9",padx=60, pady=20, font="Arial", bg="green yellow")
    l41.grid(row=2, column=4, rowspan=2, columnspan=55, padx=20, pady=30)
    l41['font'] = myFont

    b41 = Button(frame4, text="EASY", command=lambda: difficulty(frame4, 1), bg="peach puff", fg="magenta2",width=20)
    b41.grid(padx=10, pady=20, row=25, column=14, columnspan=10)
    b41['font'] = myFont

    b42 = Button(frame4, text="MEDIUM",command=lambda: difficulty(frame4, 2), bg="AntiqueWhite3", fg="red3",width=20)
    b42.grid(padx=10, pady=20, row=26, column=14, columnspan=10)
    b42['font'] = myFont

    b43 = Button(frame4, text="HARD",command=lambda: difficulty(frame4, 3), bg="cornflower blue", fg="black", width=20)
    b43.grid(padx=10, pady=20, row=27, column=14, columnspan=10)
    b43['font'] = myFont

    b44 = Button(frame4, text="BACK", command=lambda: p3(frame4), bg="DarkOrchid1", fg="cyan", width=12)
    b44.grid(padx=10, pady=20, row=28, column=8, columnspan=10)
    b44['font'] = myFont

    b45 = Button(frame4, text="EXIT", command=lambda: dest(window), bg="DarkOrchid1", fg="red2", width=12)
    b45.grid(padx=10, pady=20, row=28, column=22, columnspan=10)
    b45['font'] = myFont

def difficulty(frame,v): # QUESTION CHOICE FRAME
    dest(frame)

    window.geometry('570x745')
    frame5 = LabelFrame(window, text="Sudoku", padx=100, pady=80, fg="green")
    frame5.grid(padx=30, pady=10)

    if v==1:
        le1 = Label(frame5, text="LEVEL : EASY", fg="blue", padx=60, pady=20, font="Arial", bg="yellow")
        le1.grid(row=0, column=6, rowspan=2, columnspan=55, padx=20, pady=30)
        le1['font'] = myFont
    elif v==2:
        le1 = Label(frame5, text="LEVEL : MEDIUM", fg="green", padx=60, pady=20, font="Arial", bg="yellow")
        le1.grid(row=0, column=6, rowspan=2, columnspan=55, padx=20, pady=30)
        le1['font'] = myFont
    elif v==3:
        le1 = Label(frame5, text="LEVEL : HARD", fg="red", padx=60, pady=20, font="Arial", bg="yellow")
        le1.grid(row=0, column=6, rowspan=2, columnspan=55, padx=20, pady=30)
        le1['font'] = myFont

    le2 = Label(frame5, text="SELECT THE QUESTION", fg="orange")
    le2.grid(row=3, column=6, rowspan=2, columnspan=55, padx=20, pady=30)
    le2['font'] = myFont

    be1 = Button(frame5, text="QUESTION 1", command=lambda: qdisplay(window, frame5, v, 1, difficulty), bg="cyan", fg="deep pink", width=25)
    be1.grid(padx=10, pady=20, row=25, column=11, columnspan=10)
    be1['font'] = myFont

    be2 = Button(frame5, text="QUESTION 2", command=lambda: qdisplay(window, frame5, v, 2, difficulty), bg="deep pink", fg="yellow", width=25)
    be2.grid(padx=10, pady=20, row=26, column=11, columnspan=10)
    be2['font'] = myFont

    be3 = Button(frame5, text="QUESTION 3", command=lambda: qdisplay(window, frame5, v, 3, difficulty), bg="OliveDrab1", fg="blue2", width=25)
    be3.grid(padx=10, pady=20, row=27, column=11, columnspan=10)
    be3['font'] = myFont

    be4 = Button(frame5, text="BACK", command=lambda: p4(frame5), bg="orchid1", fg="black", width=10)
    be4.grid(padx=10, pady=20, row=28, column=5, columnspan=10)
    be4['font'] = myFont

    be5 = Button(frame5, text="EXIT", command=lambda: dest(window), bg="orchid1", fg="red", width=10)
    be5.grid(padx=10, pady=20, row=28, column=18, columnspan=10)
    be5['font'] = myFont

def reset(frame): #RESET THE SUDOKU ENTRIES
    global e
    e.clear()
    p2(frame)

def back(frame): #BACK TO FIRST SCREEN OF WINDOW
    dest(frame)
    p1()

window= Tk()
window.geometry('770x570')
window.title("Sudoku")
myFont = font.Font(size=15)

p1()

window.mainloop()



