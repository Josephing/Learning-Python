import re 

f= open('d:\\find.txt','rb')
findtxt = '<strong  usercard='
lnfindtxt = len(findtxt)
txt = f.readlines()
txt = str(txt)
pos1 = txt.find(findtxt)
pos2 = txt.find(findtxt, pos1+1)
pos3 = txt.find(findtxt, pos2+1)
pos4 = txt.find(findtxt, pos3+1)
pos5 = txt.find(findtxt, pos4+1)
pos6 = txt.find(findtxt, pos5+1)
pos7 = txt.find(findtxt, pos6+1)
pos8 = txt.find(findtxt, pos7+1)
pos9 = txt.find(findtxt, pos8+1)
pos10 = txt.find(findtxt, pos9+1)

print  txt[pos1+6+lnfindtxt:pos1+16+lnfindtxt]
print  txt[pos2+6+lnfindtxt:pos2+16+lnfindtxt]
print  txt[pos3+6+lnfindtxt:pos3+16+lnfindtxt]
print  txt[pos4+6+lnfindtxt:pos4+16+lnfindtxt]
print  txt[pos5+6+lnfindtxt:pos5+16+lnfindtxt]
print  txt[pos6+6+lnfindtxt:pos6+16+lnfindtxt]
print  txt[pos7+6+lnfindtxt:pos7+16+lnfindtxt]
print  txt[pos8+6+lnfindtxt:pos8+16+lnfindtxt]
print  txt[pos9+6+lnfindtxt:pos9+16+lnfindtxt]
print  txt[pos10+6+lnfindtxt:pos10+16+lnfindtxt]

f.close()