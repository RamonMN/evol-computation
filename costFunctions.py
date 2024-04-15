

def deJong5(x1, x2):
    a1 = [-32.0, -16.0, 0.0, 16.0, 32.0]*5
    a2 = [-32.0]*5 + [-16.0]*5 + [0.0]*5 + [16.0]*5 + [32.0]*5
    a = [a1, a2]

    sum = 0.002
    for i in range(1, 26):
        sum += ( 1 / (i + (x1 - a[0][i-1])**6 + (x2 - a[1][i-1])**6) )
    
    return 1.0/sum


def ellipticParaboloid(x1, x2):

    return (10 + (x1-10)**2 + (x2-10)**2)


if __name__ == '__main__':
    pass