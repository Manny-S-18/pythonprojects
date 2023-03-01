"""


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def palindrome():
    for i in range(900,1000):
        for j in range(900,1000):
            n3 = str(i * j)
            n4 = [int(j) for j in n3]
            if len(n4) >= 5:
                if (n4[0] == n4[5]) and (n4[1] == n4[4]) and (n4[2] == n4[3]):
                    print(n4)
                    print(i,j)



    #n4 = [9 ,8, 0, 1]
    #n4 = [9,9,8,0,0,1]
    #n4 = [0,1,2,3,4,-1]
    #n4 = [9,x,x,x,x,9]
    #n4 = [9,0,6,6,0,9]

    # and (n4[1] == n4[4]) and (n4[2] == n4[3])



palindrome()
