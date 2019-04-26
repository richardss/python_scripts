#!/usr/bin/python3
import re, os
import string
import sys
import os.path
import glob
from collections import Counter
from os import listdir
path = input("Enter a name of path: ")
keyword = input("Enter a keyword: ")
num_keyword = 0
root = glob.iglob('**/*.sh', recursive=True)
for file in root:
    text = open(file, "r")
    for line in text:
        if re.match("(.*)("+ re.escape(keyword) + r")(.*)", line):
            num_keyword = num_keyword + 1
            print (num_keyword, "result find")

print ("The numbers of occurences find are:", num_keyword)