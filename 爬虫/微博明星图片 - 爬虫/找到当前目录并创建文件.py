# -*- coding: utf-8 -*-
import os, sys

os.getcwd()
dirpath = os.path.abspath(os.path.dirname(__file__)) 
os.chdir(dirpath)

fp_raw = open("1.txt","w+")
fp_raw.write("html")
fp_raw.close()
   

