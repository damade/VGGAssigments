            #Assignment 1- Calculating number of lower and upper case letters in sentences
'''myInputString = input("What is the string that you want to input: ")
sumLower = 0
sumUpper = 0
for string in myInputString:
    if string.islower():
        sumLower += 1
    elif string.isupper():
        sumUpper += 1
    else:
        continue
print("The number of Upper case characters is ",sumUpper)
print("The number of Lower case characters is ",sumLower)'''


            #Assignment 2- Calculating the maximum number amongst three numbers
'''myList = []
for j in range(3):
    inputNumber = int(input("What is the number "+str(j+1)+" input: "))
    myList += [inputNumber]

lenList = len(myList);
for i in range(0,lenList-1):
    if(myList[i] > myList[i+1]):
        tempPlace = myList[i]
        myList[i] = myList[i+1]
        myList[i+1] = tempPlace
    else:
        continue
highestNumber = myList[len(myList)-1]
print("The Maximum number is ", highestNumber)'''


            #Assignment 3- Checking for Prime number
'''inputNumber = int(input("What is the number: "))
if (inputNumber < 1):
    print("Input a number above 1")
elif (inputNumber == 1):
    print("1 is not A Prime Number")
else:
    for i in range(2,inputNumber):
        if(inputNumber % i == 0):
            boole = False;
            break
        else:
            boole = True
            continue
    if(boole == False):
        print(str(inputNumber) + " is not A Prime Number")
    else:
        print(str(inputNumber) + " is A Prime Number")'''