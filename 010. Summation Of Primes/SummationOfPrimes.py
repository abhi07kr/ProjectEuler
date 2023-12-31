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
total = 0
while numbers < 2000000:
    if isPrime(numbers):
        total += numbers
        count += 1

    numbers += 1


print(total) #Final ans 
print(count)
