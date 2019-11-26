class BMI:
    def __init__(self,myWeight, myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight / (self.myHeight * self.myHeight)
        return currentBMI
with open('C:/Users\T05-17\Desktop\Listofnames.txt') as f:
    myArray = f.readlines()
print(myArray)

totalBMI = 0
noOfNames = 0

for lines in myArray:
    namelist = lines.split()
    name = namelist[0]
    height = float(namelist[1])
    weight = int(namelist[2])
    print(name, height,weight)
    currentBMI = person.calBMI
    totalBMI +=currentBMI
    noOfNames +=1
    averageBMI= totalBMI / noOfNames