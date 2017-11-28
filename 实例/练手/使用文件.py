afile = open('a.txt', 'w')
afile.write('abc')
afile.close()

bfile = open('a.txt', 'r')
print(bfile.read())
bfile.close()