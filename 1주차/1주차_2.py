if T % 10 == 0:
    a = T // 300
    b = T-300*a // 60
    c = T-300*a-60*b // 10
    x = str(a) + ' ' + str(b) + ' ' + str(c)
else:
    x = -1

print(x)
