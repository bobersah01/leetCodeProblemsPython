#04.03.2023 ENTRY DATE:
#LEETCODE PROBLEMS ANSWERS: LEETCODE 75/PROGRAMMING SKILLS (COMPLICATED)
#ANSWERED PROBLEMS:
#1480(lc75),1523(psd1),1491(psd1),1281(psd2),191(psd2),392(lc75),206(lc75),1822(psd4),876(lc75),121(lc75),1672(psd6),1(t100lq),21(t100lq,lc75),1232(psd5)

#1480. Running Sum of 1d Array:
#--------------------------------------------------------------------------------------------------------------------
"""
userList = list()
while (True):
    takenNumber = str(input("Please enter a number: "))
    if (takenNumber == "Q" or takenNumber == "q"):
        #print("You must not append a list much more element!")
        break
    userList.append(int(takenNumber))
print("Entered numbers in a list: {}\n--------------------------------------------------\n".format(userList))
totalList = list()
totalList.append(userList[0])
explanation = userList[0]
userList.pop(0)
for number in userList:
    explanation += number
    totalList.append(explanation)
print("Total List: {}".format(totalList))
"""
#-----------------------------------------------------------------------------------------------------------------------
#1523. Count Odd Numbers in an Interval Range:
#-----------------------------------------------------------------------------------------------------------------------
"""
while (True):
    firstInput = int(input("Please enter the low number: "))
    secondInput = int(input("Please enter the high number: "))
    if ((firstInput >= 0 and secondInput >= 0) and (firstInput <= secondInput) and (secondInput <= 10**9)):
        break
totalList = list()
for element in range(firstInput, secondInput+1):
    totalList.append(element)
print("Numbers between {} and {}: {}".format(firstInput,secondInput,totalList))
oddList = list()
for elements in totalList:
    if (elements % 2 == 1):
        oddList.append(elements)
print("Odd numbers between {} and {}: {}".format(firstInput,secondInput,oddList))
i = 0
for element in oddList:
    print("Index: {} OddNumber: {}".format(i,element))
    i += 1
print("The number of odd numbers in the list between integers of {} and {}: {}".format(firstInput,secondInput,len(oddList)))
"""
#-----------------------------------------------------------------------------------------------------------------------
#1491. Average Salary Excluding the Minimum and Maximum Salary:
#-----------------------------------------------------------------------------------------------------------------------
"""
salaryList = list()
while (True):
    salary = float(input("Please enter a salary: "))
    if (salary >= 1000 and salary <= 1000000):
        salaryList.append(salary)
    if (len(salaryList) >= 3 and (len(salaryList) <= 100)):
        if (salary == 0):
            print("You do not enter another number. Exiting from the application.")
            break
print("Entered salary list: {}".format(salaryList)) #It is working right now.
i = 0
while (i < len(salaryList)):
    if ((salaryList[i] == max(salaryList) or (salaryList[i] == min(salaryList)))):
        salaryList.remove(salaryList[i])
    i += 1
print("Entered salary list without maximum and minimum numbers: {}".format(salaryList))
totalSalary = 0
for element in salaryList:
    totalSalary += element
print("Average salary excluding the minimum and maximum salary: {}".format(totalSalary/len(salaryList)))
"""
#-----------------------------------------------------------------------------------------------------------------------
#1281. Subtract the Product and Sum of Digits of an Integer
#-----------------------------------------------------------------------------------------------------------------------
"""
integer = int(input("Please enter a number: "))
productOfDigits = 1
sumOfDigits = 0
if (integer >= 1 and integer <= 100000):
    for number in str(integer):
        productOfDigits = productOfDigits * int(number)
        sumOfDigits += int(number)
    print("Result: Product of Digits {} - Sum of Digits {}: {}".format(productOfDigits, sumOfDigits, productOfDigits-sumOfDigits))
else:
    print("Entered number is not matched with constraints!".format(integer))
"""
#-----------------------------------------------------------------------------------------------------------------------
#191. Number of 1 Bits:
#-----------------------------------------------------------------------------------------------------------------------
"""
binaryString = str(input("Please enter your binary string number: "))
if (len(binaryString) == 32):
    numbersOfOne = binaryString.count("1")
    print("Total numbers of 1: {}".format(numbersOfOne))
else:
    print("Your binary string has {} bit. Please enter 32 bit binary string number.".format(len(binaryString)))
"""
#-----------------------------------------------------------------------------------------------------------------------
#392. Is subsequence:
#-----------------------------------------------------------------------------------------------------------------------
"""
firstString = str(input("Please enter the first string: "))
secondString = str(input("Please enter the second string: "))
while (True):
    if ((len(firstString) >= 0 and len(firstString) <= 100) and (len(secondString) >= 0 and len(secondString) <= 10000 )):
        firstList = [character for character in firstString]
        indexList = list()
        i = 0
        total = 0
        while (i < len(firstList)):
            if (firstList[i] in secondString):
                total += 1
            i += 1
        ii = 0
        if (total == len(firstString)):
            for character in firstList:
                if (firstList[ii] in secondString):
                    indexList.append(secondString.index(character))
                    ii += 1
            iii = 0
            while (iii < len(indexList)-1):
                if (indexList[iii] < indexList[iii + 1]):
                    iii += 1
                break
            print(True)
            break
        else:
            print(False)
            break
    else:
        print("Your strings do not match with constraints.")
        break
"""
#-----------------------------------------------------------------------------------------------------------------------
#206. Reverse Linked List:
#-----------------------------------------------------------------------------------------------------------------------
"""
firstList = list()
while (True):
    firstInteger = str(input("Please enter a number: "))
    if (firstInteger == "q" or firstInteger == "Q"):
        print("Exiting from the program\nList is available: {}".format(firstList))
        break
    else:
        if (int(firstInteger) >= -5000 and int(firstInteger) <= 5000):
            firstList.append(int(firstInteger))
            if (len(firstList)  > 5000):
                print("You are not add any element to the list so that the number of the list is 5000")
                break
reverseList = list()
for element in firstList[::-1]:
    reverseList.append(element)
print("Normal List: {}".format(firstList))
print("Reverse List: {}".format(reverseList))
"""
#-----------------------------------------------------------------------------------------------------------------------
#1822. Sign of the Product of an Array:
#-----------------------------------------------------------------------------------------------------------------------
"""
numberList = list()
def addingList(numberList):
    #numberList = list()
    while (True):
        integer = str(input("Please enter a number: "))
        if (integer == "q" or integer == "Q"):
            print("You can not add any element to the list.\nAvailable List: {}".format(numberList))
            break
        else:
            if (int(integer) >= -100 and int(integer) <= 100):
                numberList.append(int(integer))
                print("{} added to the list".format(int(integer)))
                if (len(numberList) == 1000):
                    print("Total number of the list reached 1000 so that you are not supposed to add to the list any number")
                    break
def showingSign():
    addingList(numberList)
    multiplication = 1
    for number in numberList:
        multiplication *= number
    if (multiplication == 0):
        print("The sign of the multiplication: {}".format(0))
    elif (multiplication >  0):
        print("The sign of the multiplication: {}".format(1))
    else:
        print("The sign of the multiplication: {}".format(-1))
(showingSign())
"""
#-----------------------------------------------------------------------------------------------------------------------
#876. Middle of the Linked List:
#-----------------------------------------------------------------------------------------------------------------------
"""
firstList = list()
while (True):
    integer = int(input("Please enter a number: "))
    if (integer == 0):
        print("Available List: {}".format(firstList))
        break
    else:
        if (integer >= 1 and integer <= 100):
            firstList.append((integer))
            print("{} added to the list".format((integer)))
            if (len(firstList) == 100):
                print("Available list: {}".format(firstList))
                break
lengthOfList = len(firstList)
newList = list()
if (lengthOfList % 2 == 1):
    #middleIndex = (lengthOfList-1)/2
    i = (lengthOfList-1)/2
    while (i < lengthOfList):
        newList.append(firstList[int(i)])
        i += 1
elif (lengthOfList % 2 == 0):
    #middleIndex = (((len(firstList)-1)//2)+1)
    i = (((lengthOfList-1)//2)+1)
    while (i < lengthOfList):
        newList.append(firstList[int(i)])
        i += 1
print("New List: {}".format(newList))
"""
#-----------------------------------------------------------------------------------------------------------------------
#121. Best Time to Buy and Sell Stock: !!!
#-----------------------------------------------------------------------------------------------------------------------
"""
firstList = list()
while (True):
    integer = int(input("Please enter a number: "))
    if (integer == -1):
        print("Available List: {}".format(firstList))
        break
    else:
        if (integer >= 0 and integer <= 10000):
            firstList.append((integer))
            print("{} added to the list".format((integer)))
            if (len(firstList) == 100):
                print("Available list: {}".format(firstList))
                break
maximizeList = list()
a = 0
while (a < len(firstList)):
    for i in firstList[a:]:
        for j in firstList[a+1:]:
            maximizeList.append(j-i)
        a += 1
print("Profit List: {}".format(maximizeList))
if (max(maximizeList) < 0):
    print("There is no maximum profit: {}".format(0))

else:
    print("Maximum profit within the days can be called as: {}".format(max(maximizeList)))
"""
#-----------------------------------------------------------------------------------------------------------------------
#1672: Richest Customer Wealth: !!! IMPORTANT
#-----------------------------------------------------------------------------------------------------------------------
"""
moneyList = list()
allInOneList = list()
def allInOne(moneyBank):
    #allInOneList = list()
    for firstList in moneyBank:
        for linkedList in firstList:
            allInOneList.append(linkedList)
def controllingMatrix(moneyBank):
    firstCondition = (len(moneyBank) <= 50)
    secondCondition = (len(moneyBank[0]) >= 1)
    #thirdCondition = (True for firstList in moneyBank for linkedList in firstList if (linkedList >= 1 and linkedList <= 100)) #there is an error.
    allInOne(moneyBank)
    thirdCondition = ((min(allInOneList) <= 100 and min(allInOneList) >= 1) and (max(allInOneList) <= 100 and max(allInOneList) >= 1))"""
    
"""for firstList in moneyBank:
        for linkedList in firstList:
            if (linkedList >= 1 and linkedList <= 100):
                return True"""
"""            
    if ((firstCondition and secondCondition) and thirdCondition):
        showingRichest(moneyBank)
    else:
        print("Values that you entered, are not supported. Please try again later.")
def evaluateRichestCustomer(moneyBank):
    #total = 0
    #moneyBank = [[2,8,7],[7,1,3],[1,9,5]]
    #moneyList = list()
    for account in moneyBank:
        total = 0
        for money in account:
            total+=money
        moneyList.append(total)
def showingRichest(moneyBank):
    evaluateRichestCustomer(moneyBank)
    print("The Reachest Customer: {} money in the bank".format(max(moneyList)))
    moneyList.clear()
firstMatrix = [[1,2,3],[3,2,1]]
secondMatrix = [[1,5],[7,3],[3,5]]
thirdMatrix = [[1,21,14],[4,5,6]]
fourthMatrix = [[1,200,10], [3,2,1]]
print("For the first matrix:")
controllingMatrix(firstMatrix)
print("For the second matrix:")
controllingMatrix(secondMatrix)
print("For the third matrix: ")
controllingMatrix(thirdMatrix)
print("For the fourth matrix: ")
controllingMatrix(fourthMatrix)
"""
#-----------------------------------------------------------------------------------------------------------------------
#1: Two Sum:
#-----------------------------------------------------------------------------------------------------------------------
"""
firstList = list()
while (True):
    targetInteger = int(input("Please enter the target: "))
    if (targetInteger >= -10 ** 9 and targetInteger <= 10 ** 9):
        print("Available Target: {}".format(targetInteger))
        break
def determiningList():
    while (True):
        integer = str(input("Please enter a number: "))
        if (integer == "q" or integer == "Q"):
            print("Available List: {}".format(firstList))
            break
        else:
            if (int(integer) >= -10**9 and int(integer) <= 10**9):
                firstList.append(int(integer))
                print("{} added to the list".format((integer)))
                if (len(firstList) == 10**4+1):
                    print("Available list: {}".format(firstList))
                    break
def findingTarget(firstList):
    determiningList()
    targetIndex = list()
    a = 0
    while (a < len(firstList)):
        for i in firstList[a:]:
            for j in firstList[a+1:]:
                if ((i + j) == targetInteger):
                    targetIndex.append(firstList.index(i))
                    targetIndex.append(firstList.index(j))
                    break
            a += 1
    print("Index numbers of the firstList whose summations equal to the target: {}".format(targetIndex))
findingTarget(firstList)
"""
#-----------------------------------------------------------------------------------------------------------------------
#21. Merge Two Sorted Lists:
#-----------------------------------------------------------------------------------------------------------------------
"""
firstList = list()
secondList = list()
def determineBothList():
    #for the first list
    while(True):
        firstInteger = int(input("Please enter a number for the firstList: "))
        if (firstInteger == -101):
            print("You do not append any element to the list.\nAvailable List: {}".format(firstList))
            break
        else:
            if ((firstInteger >= -100 and firstInteger <= 100)):
                firstList.append(firstInteger)
                print("{} added to the list.".format(firstInteger))
                if(len(firstList) == 51):
                    print("Available List: {}".format(firstList))
                    break
    #for the second list
    while(True):
        secondInteger = int(input("Please enter a number for the secondList: "))
        if (secondInteger == -101):
            print("You do not append any element to the list.\nAvailable list: {}".format(secondList))
            break
        else:
            if ((secondInteger >= -100 and secondInteger <= 100)):
                secondList.append(secondInteger)
                print("{} added to the list.".format(secondInteger))
                if (len(secondList) == 51):
                    print("Available list: {}".format(secondList))
                    break
def sortingAlgorithm():
    determineBothList()
    totalList = list()
    firstSortedList = sorted(firstList, reverse = False)
    secondSortedList = sorted(secondList, reverse = False)
    i = 0
    while (True):
        if (len(firstList) == len(secondList)):
            if (i == len(firstList)):
                break
            totalList.append(firstSortedList[i])
            totalList.append(secondSortedList[i])
            i += 1
        elif (len(firstList) < len(secondList)):
            if (i < len(firstList)):
                totalList.append(firstSortedList[i])
                totalList.append(secondSortedList[i])
                i += 1
            else:
                if (i == len(secondList)):
                    break
                totalList.append(secondSortedList[i])
                i += 1
        elif (len(secondList) < len(firstList)):
            if (i < len(secondList)):
                totalList.append(firstSortedList[i])
                totalList.append(secondSortedList[i])
                i += 1
            else:
                if (i == len(firstList)):
                    break
                totalList.append(firstSortedList[i])
                i += 1
    print("Sorted List: {}".format(totalList))
sortingAlgorithm()
"""
#-----------------------------------------------------------------------------------------------------------------------
#1232. Check If It Is a Straight Line:
#-----------------------------------------------------------------------------------------------------------------------
"""
coordinates = [[11,12],[12,13],[13,14],[14,15]]
lengthOfCoordinates = len(coordinates)
trueList = list()
secondTrueList = list()
i = 0
while i < lengthOfCoordinates:
    if (len(coordinates[i]) == 2):
        trueList.append("True")
    i += 1
secondCondition = (trueList.count("True") == lengthOfCoordinates)
firstCondition = (lengthOfCoordinates >= 2 and lengthOfCoordinates <= 1000)
counter = 0
while (counter < lengthOfCoordinates):
    if ((coordinates[counter][0] >= -10000 and coordinates[counter][0] <= 10000) and (coordinates[counter][1] >= -10000 and coordinates[counter][1] <= 10000)):
        if (coordinates[counter][1] - coordinates[counter][0]):
            secondTrueList.append("True")
    counter += 1
thirdCondition = (secondTrueList.count("True") == lengthOfCoordinates)
if ((firstCondition and secondCondition) and thirdCondition):
    ii = 0
    totalCounter = 0
    while (ii < lengthOfCoordinates-1):
        if (coordinates[ii][1] == coordinates[ii+1][0]):
            totalCounter += 1
        ii += 1
    if totalCounter == lengthOfCoordinates-1:
        print("True")
    else:
        print("False")
else:
    print("False")
"""
#-----------------------------------------------------------------------------------------------------------------------

