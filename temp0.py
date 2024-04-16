import random
a = '00110101'
print(a)

number = []
for bit in a:
    if (random.random() <= 0.1):
        if (bit == '0'):
            number.append('1')
        else:
            number.append('0')
    else:
        number.append(bit)

print("".join(number))
