import math


def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

biggestPrime = 0
for i in range(2, int(math.sqrt(600851475143)) + 1):
    if isPrime(i) and 600851475143%i ==0:
        biggestPrime = max(biggestPrime, i)

print(biggestPrime)