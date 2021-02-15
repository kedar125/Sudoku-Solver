import tkinter
from tkinter import *
from second import e
from useless import out
from tkinter import messagebox
import numpy as np
import copy

#GLOBALLY DECLARE GRID ON WHICH OPERATIONS ARE PERFORMED FOR FINDING ANSWERS OF SUDOKU
gridn = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def setinitial(): # SETS THE GLOBAL GRID TO INTITAL STATE, WITH ALL ELEMENTS AS ZERO
    global gridn
    for i in range(0,9):
        for j in range(0,9):
            gridn[i][j]=0


def inputa(frame): # TAKES INPUT FROM THE SUDOKU LAYOUT(USER INPUT) & CHECKS CORRECTNESS
    global gridn, e
    setinitial()
    key=0
    k=0
    for i in range(0,9):
        for j in range(0,9):
            if e[k].get()=='':
                pass
            else:
                try:
                    if int(e[k].get(), 10) in range(1,10):
                        gridn[i][j]=(int(e[k].get(),10))
                    else:
                        messagebox.showinfo("Error!!", "Invalid Inputs")
                        key = 1
                        break
                except ValueError as w:
                    messagebox.showinfo("Error!!", "Invalid Inputs")
                    key = 1
                    break
            k+=1

        if key==1:
            break

    if key==0:

        l=out(gridn) # TO CHECK WHETHER THE INPUTS ARE PROPERLY ENTERED
        if l==-1:
            messagebox.showinfo("Error!!", "Invalid Inputs")
        else:
            solve()

def possible(y, x, n):# CHECK IF WE CAN PUT A NUMBER, y-verical , x-horizontal
    global gridn
    for i in range(0, 9):
        if gridn[y][i] == n:
            return False
    for i in range(0, 9):
        if gridn[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if gridn[y0 + i][x0 + j] == n:
                return False
    return True


def solve(): # TRYING DIFFERENT COMBINATIONS TO GET ANSWER(USES BACKTRACKING)
    global gridn, e

    try:
        for y in range(9):
            for x in range(9):
                if gridn[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n):
                            gridn[y][x] = n
                            solve()
                            gridn[y][x] = 0
                    return
        output()

    except Exception as t:
        messagebox.showinfo("Error!!", "Invalid Inputs")


def output(): # TO SHOW THE OUTPUT ON SUDOKU LAYOUT/SCREEN
    global gridn
    k = 0
    for i in range(0, 9):
        for j in range(0, 9):
            e[k].delete(0, END)
            e[k].insert(INSERT, str(gridn[i][j]))
            k += 1




