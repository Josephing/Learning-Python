# 作者：zhrq95，仅供学习交流，转载请注明出处

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

# 将 txt 文件的内容转为 ASCII 编码
a = list(str(input))
a.pop(0)
a.pop(0)
a.pop(len(a)-1)
a.pop(len(a)-1)
a = list(map(ord,a))

# 产生随机密匙 key
key = random.randint(1,987654321)

# 保存密匙到本地
keyfile = open('Random Key.txt', 'w')
keyfile.write(str(key))
keyfile.close( )

# 加密
for i in range(0, len(a)):
    a[i] = a[i] ^ key

# 保存密文到本地
encryptionfile = open('Ciphertext.txt', 'w')
encryptionfile.write(str(a))
encryptionfile.close( )