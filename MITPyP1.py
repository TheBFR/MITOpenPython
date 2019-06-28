isOdd = []
currentNum = 2
isPrime = []

for i in range(2,10):
    if currentNum%2 == 0:
        currentNum +=1
    else:
        isOdd.append(currentNum)
        currentNum +=1

print(len(isOdd), "is the number of odds in range")
print (isOdd)

for i in range(1,len(isOdd)):
    if (isOdd[i]%i) == 0:
        print (isOdd[i], "This is the current list item")
        print(i, "This is i")
        print (str(isOdd[i]) + " is not a prime number")
    else:
        print (str(isOdd[i]) + " is a prime number")


