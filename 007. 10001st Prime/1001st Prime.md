import math


def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


count = 0  # To count the number of primes encountered so far
numbers = 2  # To keep the numbers increasing
primes = []
while count < 10001:
    if isPrime(numbers):
        primes.append(numbers)
        count += 1
    numbers += 1

print(primes) # All primes
print(primes[-1]) #Final answer i.e 10001st Prime 
