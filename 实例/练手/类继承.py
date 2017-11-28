class Pclass():
    gender = "male"
    def __init__(self, who):
        self.name = who

class Cclass(Pclass):
    def displayInfo(self):
        print(self.name, self.gender)

x = Cclass("Tom")

print(x.name, x.gender, x.displayInfo())

print(dir(x))
