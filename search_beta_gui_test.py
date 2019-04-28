#!/usr/bin/python3
import re, os
import string
import sys
import os.path
import glob
from collections import Counter
from os import listdir
import tkinter
from tkinter import *
import tkinter.messagebox
num_keyword = 0
master = Tk()
Label(master, text="Path:").grid(row=0)
Label(master, text="Keyword:").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(0,"")
e2.insert(0,"")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def find ():
    paths = e1.get()
    keyword = e2.get()
    num_keyword = 0
    root = glob.iglob(os.path.join(paths + '*/*.txt'))
    for file in root:
        text = open(file, "r")
        for line in text:
            if re.match("(.*)("+ re.escape(keyword) + r")(.*)", line):
               num_keyword +=1
    tkinter.messagebox.showinfo("Result", "The numbers of occurences find are:", num_keyword)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Start', command=find).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )