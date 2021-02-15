import tkinter
from tkinter import *
from sudoku import inputa
from second import e,create
import copy

#EASY QUESTIONS
gride1 =    [[6, 0, 0, 1, 0, 0, 0, 0, 2],
             [8, 0, 1, 0, 9, 0, 0, 0, 0],
             [0, 7, 5, 0, 8, 4, 0, 0, 0],
             [4, 3, 0, 0, 2, 0, 5, 6, 1],
             [5, 1, 8, 7, 0, 0, 4, 0, 9],
             [0, 9, 6, 4, 1, 0, 3, 0, 0],
             [0, 0, 0, 0, 7, 0, 0, 0, 0],
             [0, 6, 0, 0, 3, 1, 0, 5, 0],
             [7, 0, 2, 5, 4, 0, 6, 0, 3]]

gride2 =    [[0, 0, 1, 9, 8, 4, 7, 6, 0],
             [6, 0, 0, 0, 5, 7, 0, 0, 0],
             [8, 0, 7, 0, 1, 0, 0, 0, 0],
             [9, 6, 0, 3, 0, 8, 1, 0, 5],
             [1, 8, 5, 0, 2, 0, 0, 7, 3],
             [3, 0, 0, 0, 0, 0, 2, 0, 8],
             [2, 1, 0, 0, 0, 0, 0, 3, 6],
             [0, 0, 0, 1, 0, 0, 0, 0, 4],
             [0, 9, 6, 0, 0, 2, 5, 1, 0]]

gride3 =    [[0, 0, 0, 6, 0, 0, 1, 0, 7],
             [6, 8, 0, 9, 5, 1, 3, 0, 0],
             [0, 0, 3, 0, 0, 2, 5, 6, 8],
             [0, 4, 0, 8, 1, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 8, 5, 0],
             [0, 9, 0, 0, 6, 5, 0, 7, 3],
             [4, 0, 9, 0, 0, 3, 0, 8, 5],
             [1, 6, 2, 0, 0, 9, 0, 3, 0],
             [5, 0, 0, 7, 0, 6, 0, 0, 0]]

#MEDIUM QUESTIONS
gridm1=     [[0, 0, 0, 4, 0, 0, 2, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 1, 8],
            [5, 0, 6, 9, 0, 0, 0, 3, 0],
            [0, 6, 9, 0, 0, 0, 3, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 2, 1],
            [8, 0, 0, 1, 5, 7, 6, 0, 9],
            [0, 0, 0, 0, 3, 0, 9, 6, 0],
            [9, 0, 0, 6, 0, 2, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 2]]

gridm2=     [[0, 0, 0, 0, 0, 0, 6, 0, 9],
            [1, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 5, 3, 0, 6, 8, 2, 1],
            [0, 0, 4, 6, 7, 0, 0, 5, 0],
            [0, 0, 7, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 5, 4, 0, 0, 0, 0],
            [3, 7, 0, 4, 0, 5, 2, 0, 6],
            [0, 0, 0, 0, 0, 0, 5, 1, 0],
            [0, 6, 0, 0, 2, 0, 0, 3, 7]]

gridm3=     [[2, 5, 0, 0, 0, 3, 0, 9, 1],
            [3, 0, 9, 0, 0, 0, 7, 2, 0],
            [0, 0, 1, 0, 0, 6, 3, 0, 0],
            [0, 0, 0, 0, 6, 8, 0, 0, 3],
            [0, 1, 0, 0, 4, 0, 0, 0, 0],
            [6, 0, 3, 0, 0, 0, 0, 5, 0],
            [1, 3, 2, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 4, 0, 6, 0],
            [7, 6, 4, 0, 1, 0, 0, 0, 0]]

#HARD QUESTIONS
gridh1=     [[5, 8, 6, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 1, 6, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 0, 0, 0],
            [9, 0, 2, 0, 1, 0, 3, 0, 5],
            [0, 0, 5, 0, 9, 0, 0, 0, 0],
            [0, 9, 0, 0, 4, 0, 0, 0, 8],
            [0, 0, 3, 5, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 2, 0, 4, 7, 0]]

gridh2=     [[0, 0, 7, 0, 0, 0, 3, 0, 2],
            [2, 0, 0, 0, 0, 5, 0, 1, 0],
            [0, 0, 0, 8, 0, 1, 4, 0, 0],
            [0, 1, 0, 0, 9, 6, 0, 0, 8],
            [7, 6, 0, 0, 0, 0, 0, 4, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 3, 0, 0, 0],
            [8, 0, 1, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 0, 6, 3]]

gridh3=     [[0, 0, 4, 8, 6, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 9, 0],
            [8, 0, 0, 0, 0, 9, 0, 6, 0],
            [5, 0, 0, 2, 0, 6, 0, 0, 1],
            [0, 2, 7, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 4, 3, 0, 0, 6],
            [0, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 1, 5]]

#GLOBAL GRID TO PUT THE PARTICULAR QUESTION ONTO LAYOUT(SCREEN)
grid1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]



def dest(f): # DESTROYS FRAME
    f.destroy()

def go(frame,window): # DESTROYS WINDOW, FRAME
    dest(frame)
    window.destroy()

def qdisplay(window, previousf, v, q, difficulty): # DISPLAYS THE CHOSEN QUESTION IN SUDOKU LAYOUT
    dest(previousf)

    global grid1, gride1, gride2, gride3, gridm1, gridm2, gridm3, gridh1, gridh2, gridh3

    if v==1 and q==1:
        grid1 = copy.deepcopy(gride1)
    elif v==1 and q==2:
        grid1= copy.deepcopy(gride2)
    elif v==1 and q==3:
        grid1= copy.deepcopy(gride3)
    elif v==2 and q==1:
        grid1= copy.deepcopy(gridm1)
    elif v==2 and q==2:
        grid1= copy.deepcopy(gridm2)
    elif v==2 and q==3:
        grid1= copy.deepcopy(gridm3)
    elif v==3 and q==1:
        grid1= copy.deepcopy(gridh1)
    elif v==3 and q==2:
        grid1= copy.deepcopy(gridh2)
    elif v==3 and q==3:
        grid1= copy.deepcopy(gridh3)

    window.geometry('750x770')
    frameq = LabelFrame(window, text="Sudoku", padx=100, pady=80, fg="green")
    frameq.grid(padx=30, pady=10)

    create(frameq)
    k=0
    for i in range (0,9):
        for j in range (0,9):
            e[k].delete(0,END)
            if grid1[i][j]!=0:
                e[k].insert(INSERT,str(grid1[i][j]))
            k += 1

    lque = Label(frameq, text="To check the right answer click Solve!!", fg="red")
    lque.grid(row=2, column=0, rowspan=2, columnspan=55, padx=20, pady=30)
    lque['font'] = 15

    bque= Button(frameq, text="SOLVE", command=lambda: inputa(frameq), bg="yellow", fg="black",width=7)
    bque.grid(padx=10, pady=20, row=25, column=6, columnspan=3)
    bque['font'] = 15

    bque = Button(frameq, text="BACK", command=lambda: difficulty(frameq, v), bg="yellow", fg="black",width=7)
    bque.grid(padx=10, pady=20, row=25, column=3, columnspan=3)
    bque['font'] = 15

    bque = Button(frameq, text="EXIT", command=lambda: go(frameq,window), bg="yellow", fg="red",width=7)
    bque.grid(padx=10, pady=20, row=25, column=9, columnspan=3)
    bque['font'] = 15

    frameq.pack(padx=10, pady=10)

