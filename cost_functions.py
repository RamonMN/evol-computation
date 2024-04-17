def cost_function(x1_bin, x2_bin):
    x1_inf_lim = -65.536
    x1_sup_lim = 65.536

    x2_inf_lim = -65.536
    x2_sup_lim = 65.536

    # Convert binary into integer value
    x1_int = int(x1_bin, 2)
    x2_int = int(x2_bin, 2)

    # Interpolate integer value inside varible range
    x1 = interpolate(x1_int, len(x1_bin), x1_inf_lim, x1_sup_lim)
    x2 = interpolate(x2_int, len(x2_bin), x2_inf_lim, x2_sup_lim)

    return deJong5(x1, x2)


def deJong5(x1, x2):
    a1 = [-32.0, -16.0, 0.0, 16.0, 32.0]*5
    a2 = [-32.0]*5 + [-16.0]*5 + [0.0]*5 + [16.0]*5 + [32.0]*5
    a = [a1, a2]

    sum = 0.002
    for i in range(1, 26):
        sum += ( 1 / (i + (x1 - a[0][i-1])**6 + (x2 - a[1][i-1])**6) )
    
    return 1.0/sum


def ellipticParaboloid(x1, x2):

    return (10 + (x1)**2 + (x2)**2)


def interpolate(integer_value, size, inf_lim, sup_lim):
    
    precision = (sup_lim - inf_lim)/((2**size) - 1)

    interpolated = inf_lim + integer_value*precision

    return interpolated

if __name__ == '__main__':
    print(deJong5(1.0, 2.0))