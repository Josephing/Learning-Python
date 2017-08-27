# 作者：zhrq95，仅供学习交流，转载请注明出处

import os, sys
import itertools

# 找到当前路径，方便下面使用相对路径
os.getcwd()
dirpath = os.path.abspath(os.path.dirname(__file__))
os.chdir(dirpath)

# 读取随机密匙
keyfile = open("Random Key.txt","r")
key  = keyfile.readlines()
keyfile.close()
key = int(key[0])

# 读取密文
f = open("Ciphertext.txt","r")
b = f.readlines()
f.close()

b = b[0]
b = b[1:len(b)-1 ]
b = b.split(",")
b=list(map(int,b))

# 开始解密
for i in range(0, len(b)):
    b[i] = b[i] ^ key
    b[i] = chr(b[i])

# 把解密结果写入本地文件    
s = "".join(itertools.chain(*b))
decryptfile = open('Decrypt file.txt', 'w')
decryptfile.write(str(s))
decryptfile.close( )
