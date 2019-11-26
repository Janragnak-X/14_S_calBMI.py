#frm a
class BMI:
    def __init__(self,myWeight, myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight / (self.myHeight * self.myHeight)
        return currentBMI
#frm 2b
with open('C:/Users\T05-17\Desktop\Listofnames.txt') as f:
    myArray = f.readlines()
    print(myArray)
totalBMI = 0

for lines in myArray:
    mylist = lines.split()
    name = mylist[0]
    height = float(mylist[1])
    weight = float(mylist[2])
    person = BMI(weight,height,name)
    myBmi = person.calBMI()
    # test
    #print(name, 'has h is',height, 'w is',weight,'bmi:',myBmi)
    totalBMI += myBmi
noOfPerson = len(myArray)
averageBMI = totalBMI/noOfPerson
print("Average bmi is",round(averageBMI,2))

#frm 2c
yourName = input('What is your name?')
yourWeight = float(input('What is your weight in kg?'))
yourHeight = float(input('What is your height in meters.'))
newPerson = BMI(yourWeight,yourHeight,yourName)
newBMI = newPerson.calBMI()
print("Dear",yourName + ", your BMI is",round(newBMI,2))
#2d
newAverageBMI = (totalBMI + newBMI)/(noOfPerson +1)
print("New average BMI is",round(averageBMI,2))