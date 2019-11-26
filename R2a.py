class BMI:
    def __init__(self,myWeight, myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight / (self.myHeight * self.myHeight)
        return currentBMI

#testing
person = BMI (60, 1.5,"John")
print(person.myName,'BMI is',round(person.calBMI(),2))

