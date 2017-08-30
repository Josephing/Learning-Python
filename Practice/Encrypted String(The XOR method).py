def crypt(source,key):
    from itertools import cycle
    result =''
    temp=cycle(key)
    for ch in source:
        result =result + chr(ord(ch)^ord(next(temp)))
    return result
source = 'Python'
key = 'zhrq95'

print('原文：'+ source)
encrypted=crypt(source,key)
print('密文：'+ encrypted)
decrypted=crypt(encrypted,key)
print('解密后：'+ decrypted)