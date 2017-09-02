import os, sys
import random

# 找到当前路径，方便下面使用相对路径
os.getcwd()
dirpath = os.path.abspath(os.path.dirname(__file__))
os.chdir(dirpath)

# 打开要加密的 txt 文件
inputfile = open("Clear Text.txt","r")
input = inputfile.readlines()
inputfile.close()
source = str(input)



def crypt(source,key):
    from itertools import cycle
    result =''
    temp=cycle(key)
    for ch in source:
        result =result + chr(ord(ch)^ord(next(temp)))
    return result

key = 'Dong'

print('before'+source)
encrypted=crypt(source,key)
print('afteren:'+encrypted)
decrypted=crypt(encrypted,key)
print('ad:'+decrypted)