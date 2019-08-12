def prog4(num):
    s = lambda num: {num: (num*num) for num in range(1, num + 1)}
    return s(num)
print(prog4(8))
