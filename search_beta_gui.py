#!/usr/bin/python3
import re, os
import string
import sys
import os.path
import glob
from collections import Counter
from os import listdir
from tkinter import *
#root = tk.Tk()
#path = input("Enter a name of path: ")
#from tkinter import *
def show_entry_fields():
   print("Path: %s\nKeyword: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Path:").grid(row=0)
Label(master, text="Keyword:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.insert(0,"")
path = e1.get()
e2.insert(0,"")
keyword = e2.get()
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def find ():
    root = glob.iglob('**/*.sh', recursive=True)
    for file in root:
        text = open(file, "r")
        for line in text:
            if re.match("(.*)("+ re.escape(keyword) + r")(.*)", line):
                num_keyword = 0
                num_keyword = num_keyword + 1
            msg = .Message(master, text = "result find")
    print ("The numbers of occurences find are:", num_keyword)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Start', command=find).grid(row=3, column=1, sticky=W, pady=4)


#print ("The numbers of occurences find are:", num_keyword)

mainloop( )