import tkinter
from tkinter import *
e = [] # STORES THE OBJECTS OF 81 ENTRY FIELDS OF LAYOUT

def create(frame): #CREATES THE SUDOKU 9X9 LAYOUT
    global e
    e.clear()
    for r in range(10, 19):
        for c in range(3, 12):
            if r in range(10, 13) and c in range(6, 9):
                l = Entry(frame, width='3', font=('Times New Roman', 25), bg="gray78",justify='center')
                l.grid(row=r, column=c)
                e.append(l)
            elif r in range(13, 16) and c in range(3, 6):
                l = Entry(frame, width='3', font=('Times New Roman', 25), bg="gray78",justify='center')
                l.grid(row=r, column=c)
                e.append(l)
            elif r in range(13, 16) and c in range(9, 12):
                l = Entry(frame, width='3', font=('Times New Roman', 25), bg="gray78",justify='center')
                l.grid(row=r, column=c)
                e.append(l)
            elif r in range(16, 19) and c in range(6, 9):
                l = Entry(frame, width='3', font=('Times New Roman', 25), bg="gray78",justify='center')
                l.grid(row=r, column=c)
                e.append(l)
            else:
                l = Entry(frame, width='3', font=('Times New Roman', 25), borderwidth='2', bg='white smoke',justify='center')
                l.grid(row=r,column=c)
                e.append(l)







