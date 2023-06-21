def EvenFibonacciNumber():
    first, second, total = 1, 2, 0
    while first < 4000000:
        newNum = first + second
        if second % 2 == 0:
            total += second
        first, second = second, newNum

    return total


print(EvenFibonacciNumber())
