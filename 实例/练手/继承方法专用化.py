class ParClass():
    def setInfo(self, sex='Male'):
        self.gender = sex

class ChiClass(ParClass):
    def setInfo(self, who):
        self.name = who
        ParClass.setInfo(self) # 回调，若没有这句，则 print(x.gender) 报错


x=ChiClass()
x.setInfo('Tom')

print(x.name)
print(x.gender)