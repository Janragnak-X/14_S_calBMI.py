with open('C:/Users\T05-17\Desktop\Listofnames.txt') as f:
    myArray = f.readlines()
print(myArray)
for lines in myArray:
    namelist = lines.split()
    name = namelist[0]
    height = float(namelist[1])
    weight = int(namelist[2])
    print(name, height,weight)
