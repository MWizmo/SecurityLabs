def average():
    opened_keys = [(5, 91), (17, 55), (91, 187)]
    closed_keys = [29, 33, 51]
    nums = [12, 21, 9]  # Куз
    secret_num = 8
    x1 = (nums[0] + secret_num) ** opened_keys[1][0] % opened_keys[1][1]

    y1 = x1 ** closed_keys[1] % opened_keys[1][1]
    x2 = (y1 + nums[1]) ** opened_keys[2][0] % opened_keys[2][1]

    y2 = x2 ** closed_keys[2] % opened_keys[2][1]
    x3 = (y2 + nums[2]) ** opened_keys[0][0] % opened_keys[0][1]

    y3 = x3 ** closed_keys[0] % opened_keys[0][1]
    return (y3 - secret_num) / 3


def xor(a, b, c, d):
    res = bin(int(a, 2) ^ int(b, 2) ^ int(c, 2) ^ int(d, 2))
    res = res[2:]
    diff = 8 - len(res)
    for i in range(0, diff):
        res = '0' + res
    return res


def secretSharingWithGamming():
    secret = ['11001010', '11010011', '11000111']  # куз
    gamma1 = ['11001010', '11001110', '11010010']  # кот
    gamma2 = ['11000010', '11001010', '11010000']  # вкр
    gamma3 = ['11010000', '11001110', '11001100']  # ром
    code = list()
    for i in range(0, 3):
        code.append(xor(secret[i], gamma1[i], gamma2[i], gamma3[i]))
    print('Code: ', code)
    secret2 = list()
    for i in range(0, 3):
        secret2.append(xor(code[i], gamma1[i], gamma2[i], gamma3[i]))
    print('Secret2: ', secret2)


def f(x, a1, a2, p, s):
    return (a1 * x * x + a2 * x + s) % p


def Shamir_encoding():
    s = 12
    m = 3
    n = 5
    p = 19
    a1 = 5
    a2 = 7
    shares = list()
    for i in range(0, n):
        shares.append((i + 1, f(i + 1, a1, a2, p, s)))
    return p, shares


def l(x, shares, j):
    res = 1
    multiplier = 1
    for i in range(0, len(shares)):
        if i != j:
            res *= (x - shares[i][0]) / (shares[j][0] - shares[i][0])
            multiplier *= 1 / (shares[j][0] - shares[i][0])
    return res, multiplier


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)


def L(x, shares, p):
    res = 0
    denominators = []
    for i in range(0, len(shares)):
        addend, multiplier = l(x, shares, i)
        res += shares[i][1] * addend
        denominators.append(abs(1 / multiplier))
    b = lcm(denominators[0], lcm(denominators[1], denominators[2]))
    b2 = 1
    for i in range(0, 1000):
        if (b * i) % p == 1:
            b2 = i
            break
    print(b2)
    return res % p


def Shamir_decoding(p, shares):
    # print(l(1, shares, 0))
    pass


def secretSharingAB_encoding():
    s = 12
    p = 13
    d = [17, 20, 23, 29, 37]
    res = 1
    for i in range(0,3):
        res *= d[i]
    # print((res-s)/p)
    r = 15
    s2 = s + r * p
    shares = list()
    for i in range(0, 5):
        shares.append((d[i], s2 % d[i]))
    return p, shares


def secretSharingAB_decoding(p, shares):
    d = shares[0][0] * shares[1][0] * shares[2][0]
    d1 = [d / shares[0][0], d / shares[1][0], d / shares[2][0]]
    d2 = list()
    for i in range(0,100):
        if (i * d1[0]) % shares[0][0] == 1:
            d2.append(i)
            break
    for i in range(0,100):
        if (i * d1[1]) % shares[1][0] == 1:
            d2.append(i)
            break
    for i in range(0,100):
        if (i * d1[2]) % shares[2][0] == 1:
            d2.append(i)
            break
    s = 0
    for i in range(0,3):
        s += (shares[i][1] * d1[i] * d2[i])
    s %= d
    secret = s % p
    print("S' = ", s)
    print('S = ', secret)


print('Average')
print(average())
print('Gamma')
secretSharingWithGamming()
print('Shamir')
p, shares = Shamir_encoding()
print(shares)
print()
print('Asmut_Blum')
p, shares = secretSharingAB_encoding()
print(shares)
secretSharingAB_decoding(p, [shares[0], shares[2], shares[4]])
