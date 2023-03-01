"""


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def Primes(numIn):
    primes = []

    for num in range(2, numIn+1Ss):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               primes.append(num)
    print(primes)
    print(len(primes))
    print(primes[10000])

Primes(104800)
