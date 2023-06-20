def SumSquareDifference(num):
    totalSquare, totalSumSquare = 0, 0
    for i in range(1, num + 1):
        totalSquare += i * i

    for i in range(1, num + 1):
        totalSumSquare += i

    return totalSumSquare **2 - totalSquare


print(SumSquareDifference(100))
