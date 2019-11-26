class BMI:
    def __init__(self,myWeight,myHeight,myName):
        self.mw = myWeight
        self.mh = myHeight
        self.mn = myName
    def calBMI(self):
        currentBMI = self.mw/(self.mh*self.mh)
        return currentBMI

#test
person = BMI(65,1.8,'john')
print(person.mn,"bmi is",round(person.calBMI(),2))