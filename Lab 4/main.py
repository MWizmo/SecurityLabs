import numpy as np


def paitet_bit():
    data = ['11001010', ' 11010011', '11000111', '11001000', '11001101']
    for num in data:
        count = 0
        for i in num:
            if i == '1':
                count += 1
        if count % 2:
            print('Data: ', num)
            print('Odd paritet bit: 1')
            print('Even paritet bit: 0')
        else:
            print('Data: ', num)
            print('Odd paritet bit: 0')
            print('Even paritet bit: 1')


def Luhn_algorithm():
    data = [1, 2, 2, 1, 9, 1, 0, 1, 5, 1, 1, 5, 5, 1, 8]  # Кузин Андр
    S1 = 0
    S2 = 0
    for i in range(0, len(data)):
        if i % 2:
            S1 += (data[i] * 2) % 9
        else:
            if i != len(data) - 1:
                S2 += data[i]
    cd = 10 - (S1 + S2) % 10
    new_data = ''
    for i in range(0, len(data)):
        if i % 4 == 0 and i > 0:
            new_data += ' '
        new_data += str(data[i])
    new_data += str(cd)
    return new_data


def EAN_13():
    data = [1, 2, 2, 1, 9, 1, 0, 1, 5, 1, 1, 5]  # Кузин Ан
    S1 = 0
    S2 = 0
    for i in range(0, len(data)):
        if i % 2:
            S1 += data[i] * 3
        elif i != len(data) - 1:
            S2 += data[i]
    cd = 10 - (S1 + S2) % 10
    new_data = ''
    for i in range(0, len(data)):
        if i % 6 == 1:
            new_data += ' '
        new_data += str(data[i])
    new_data += str(cd)
    return new_data


def INN():
    data = [1, 2, 2, 1, 9, 1, 0, 1, 5, 1]  # Кузин А
    n11 = ((7 * data[0] + 2 * data[1] + 4 * data[2] + 10 * data[3] + 3 * data[4] +
    5 * data[5] + 9 * data[6] + 4 * data[7] + 6 * data[8] + 8 * data[9]) % 11) % 10
    n12 = ((3 * data[0] + 7 * data[1] + 2 * data[2] + 4 * data[3] + 10 * data[4] + 3 * data[5] +
           5 * data[6] + 9 * data[7] + 4 * data[8] + 6 * data[9] + 8 * n11) % 11) % 10
    new_data = ''
    for digit in data:
        new_data += str(digit)
    new_data += str(n11)
    new_data += str(n12)
    return new_data


def station_code():
    data = [1, 2, 2, 1, 9]  # Куз
    n6 = (data[0] + 2 * data[1] + 3 * data[2] + 4 * data[3] + 5 * data[4]) % 11
    if n6 < 10:
        print('1 step')
        new_data = ''
        for digit in data:
            new_data += str(digit)
        new_data += str(n6)
        return new_data
    else:
        print('2 steps')
        n6_2 = (3 * data[0] + 4 * data[1] + 5 * data[2] + 6 * data[3] + 7 * data[4]) % 11
        new_data = ''
        for digit in data:
            new_data += str(digit)
        if n6 < 10:
            return new_data + str(n6_2)
        else:
            return new_data + '0'


def to_polynom(string):
    a = list()
    for i in range(2, len(string)):
        a.append(int(string[i]))
    b = np.array(a)
    return b


def checksum():
    input = [12, 21, 9]  # Куз
    for num in input:
        dividend = bin(num) + '0000'
        print('Dividend: ', dividend[2:])
        dividend = to_polynom(dividend)
        divider = np.array([1, 0, 0, 1, 1])
        private = np.polydiv(dividend, divider)[1]
        check_sum = ''
        for i in private:
            if abs(int(i)) != 2:
                check_sum += str(abs(int(i)))
            else:
                check_sum += '0'
        print('Checksum: ', check_sum)
        print(bin(num)[2:] + ' ' + check_sum)
        print(int(bin(num)[2:] + check_sum, 2))


def to4(num):
    if len(num) == 1:
        return '000' + num
    elif len(num) == 2:
        return '00' + num
    elif len(num) == 3:
        return '0' + num
    else:
        return num

def ECC_encoding():
    input = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    data = list()
    j = 0
    for i in range(0, 15):
        if i == 0 or i == 1 or i == 3 or i == 7:
            data.append(0)
        else:
            data.append(input[j])
            j += 1
    matrix = list()
    matrix.append(data)
    for i in range(0, 4):
        empty = list()
        for i in range(0, len(data)):
            empty.append(0)
        matrix.append(empty)
    for i in range(0, len(data)):
        binar = to4(bin(i + 1)[2:])
        for j in range(0, len(binar)):
            matrix[4 - j][i] = int(binar[j])
    r = list()
    for j in range(0, 4):
        rj = 0
        for i in range(0, len(data)):
            rj += matrix[0][i] * matrix[j + 1][i]
        r.append(rj % 2)
    pb = 0
    for i in range(0, len(data)):
        pb += matrix[0][i]
    pb %= 2
    new_data = ''
    for digit in input:
        new_data += str(digit)
    new_data += ' ' + str(r[0]) + str(r[1]) + str(r[2]) + str(r[3]) + str(pb)
    print(new_data)
    return matrix, r, pb


def ECC_decoding(matrix, r, pb):
    import math
    matrix[0][11] = 1
    matrix[0][4] = 0
    for i in range(0, len(r)):
        matrix[0][int(math.pow(2, i)) - 1] = r[i]
    new_pb = 0
    for i in range(0, len(matrix[0])):
        pb += matrix[0][i]
    new_pb %= 2
    print(new_pb)
    s = list()
    for j in range(0, 4):
        sj = 0
        for i in range(0, len(matrix[0])):
            sj += matrix[0][i] * matrix[j + 1][i]
        s.append(sj % 2)
    print(s)


print('Paritet bit')
paitet_bit()
print('Luhn')
print(Luhn_algorithm())
print('EAN-13')
print(EAN_13())
print('INN')
print(INN())
print('Station code')
print(station_code())
print('Control summa')
checksum()
print('ECC')
matrix, r, pb = ECC_encoding()
ECC_decoding(matrix, r, pb)
