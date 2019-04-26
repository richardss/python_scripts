#!/usr/bin/env python
import re, os
import string
import sys
from os import listdir

path = input("Enter a name of path: ")
keyword = input("Enter a keyword: ")
#filename = 
#file = open(filename, "r")
root = os.listdir(path)

for file in root:
    file = os.path.join(path, file)
    text = open(file, "r")
    for line in text:
        if re.match("(.*)("+ re.escape(keyword) + r")(.*)", line):
            print (line),
