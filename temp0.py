a = [0, 0, 0, 0, 1, 1]
a_real = 0
for i, j in enumerate(a[::-1]):
    a_real += (2**i)*j

print(a_real)
