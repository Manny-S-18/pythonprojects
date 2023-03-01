"""

The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def squaresum(limit):
    natnum = []
    natnumsq = []
    for x in range(1,limit+1):
        natnum.append(x)

    for i in natnum:
        natnumsq.append(i**2)

    print(sum(natnumsq))

def sumsquare(limit):
    natnum = []
    for x in range(1,limit+1):
        natnum.append(x)

    a = sum(natnum)

    print(a**2)

def difference(a,b):
    c = a - b
    print(c)


difference(25502500,338350)

#25502500-338350
