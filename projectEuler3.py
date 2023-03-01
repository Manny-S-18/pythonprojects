from math import sqrt

def PrimeFactors (n):

	for i in range(2, int(sqrt(n)) + 1):

		while (n % i) == 0:
			Prime_max = i
			n = n / i
	return int(Prime_max)

n = 600851475143
print(PrimeFactors(n))
