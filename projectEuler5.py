"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def noRemainder():
    oneToTen = [11, 13, 14, 16, 17, 18, 19, 20]
    allNum = []
    for x in range(200000000,300000000):
        allNum.append(x)

    norem = [i for i in allNum if all(i % j == 0 for j in oneToTen)]


    print(norem)
noRemainder()
