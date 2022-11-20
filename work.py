#Opening Comments
#Title: Near Miss Calculator based on Fermets' Theorem
#Name of file: work.py
#List of external files: NA
#List of external files created by program: Nil
#Name:
#Email Address:
#Course and Section no:
#Date of submission
#Explanation: The program is indented to find the near misses in the equation x^n+y^n = z^n

# x^n + y^n = z^n Finding the near misses
def allWork():
    check = 1

    #The starting constraint check for the value of n(2<n<12)
    while check>0:
        n = int(input("Input the value of n: "))
        if 2 < n < 12:
            check -= 1
        else:
            print("The value of n must follow the condition: 2 < n < 12, Please input again!")

    check = 1
    #The starting constraint check for the value of k(k>10)
    while check>0:
        k = int(input("Input the value of k: "))
        if k > 10:
            check -= 1
        else:
            print("The value of k must be greater than 10, Please input again!")

    #starting lists to check all values of x,y and z
    xList = [i for i in range(10,(k + 1))]
    yList = [i for i in range(10,(k + 1))]
    zList = [i for i in range(1,(k+k+1))]

    #A combination list containing both x and y values
    xyList = []
    for i in range(len(xList)):
        for j in yList:
            xyList.append([xList[i], j])

    #The list containing all possible values of x^n+y^n
    nList = []
    for i in xyList:
        nList.append(i[0]**n + i[1]**n)

    #The list containing values of z^n
    znList = []
    for i in zList:
        znList.append(i**n)

    #The function finds the nearest value between any 2 given values
    def nearest_val(inp_l, val):
        diff = lambda inp_l : abs(inp_l - val)
        res = min(inp_l, key = diff)
        return res

    #this funciton returns a list containing the nearest values between the x^n+y^n and z^n
    closeVal = []
    for i in nList:
        x = nearest_val(znList, i)
        closeVal.append(x)

    #This is a combination list containing the sum and the closest value
    combList = []
    for i in range(len(nList)):
        combList.append([nList[i],closeVal[i]])

    #The list contains all the misses that has occured.
    missList = []
    for i in combList:
        missList.append(abs(i[0]-i[1]))
    print("Minimum miss is: ",min(missList))

    #This list consists of all the relative misses
    divList = []
    for i in range(len(nList)):
        divList.append(missList[i]/nList[i])

    m = min(divList)
    print("Minimum relative miss is: ",m)

    indexList = []
    for i in range(len(divList)):
        if divList[i] == m:
            indexList.append(i)

    #Final values are printed
    for i in indexList:
        print(f"The values are {xyList[i]}")
    
    u = input("")

if __name__ == "__main__":
    allWork()
