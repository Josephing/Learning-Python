class myClass:
    avariable = 0
    def __init__(self):
        self.myName = 'A New Instance'
    def changeName(self, newName):
        self.myName = newName

zhrq95 = myClass()

print(zhrq95.avariable)
zhrq95.avariable = 10
print(zhrq95.avariable)

print(zhrq95.myName)

zhrq95.changeName('zhrq95')
print(zhrq95.myName)