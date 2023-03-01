"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million

"""
def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for i in range(2, n):
        if sieve[i]:
            sum += i
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum

print(sumPrimes(2000000))
