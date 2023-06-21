def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / hcf(a, b)


res = lcm(1, 2)
for i in range(3, 21):
    res = lcm(i, res)

print(res)

