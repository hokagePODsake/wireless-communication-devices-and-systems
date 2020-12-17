import random
from matplotlib import pyplot as plt
import numpy as np


def find_c(msg, g, r):
    m = msg << r
    if len(bin(m)) < len(bin(g)):
        return m
    temp_g = g << (len(bin(m)) - len(bin(g)))
    remainder = m ^ temp_g
    while len(bin(remainder)) >= len(bin(g)):
        temp_g = g << (len(bin(remainder)) - len(bin(g)))
        remainder = remainder ^ temp_g
    return remainder


def gen_e(p, l, r):
    a = []
    lenght = l + r
    while len(a) < lenght:
        x = random.uniform(0, 1.0)
        if x <= p:
            temp_x = 1
            a.append(temp_x)
        else:
            temp_x = 0
            a.append(temp_x)
    my_string = ''
    for i in a:
        my_string += str(i)
    return int(my_string, 2)


def calc_syndrome(b, g):
    if len(bin(b)) < len(bin(g)):
        return b
    temp_g = g << (len(bin(b)) - len(bin(g)))
    remainder = b ^ temp_g
    while len(bin(remainder)) >= len(bin(g)):
        temp_g = g << (len(bin(remainder)) - len(bin(g)))
        remainder = remainder ^ temp_g
    return remainder

def code_words():
    g = input("Enter your g(x): ")
    g = int(g, 2)  # g(x)
    k = int(input("Enter you k: "))
    p = 0.1
    r = len(bin(g)) - 3  # степень многочлена
    words_before = []
    words = []
    for m in range(0, 2 ** k, 1):
        msg = m
        c = find_c(msg, g, r)
        a = (msg << r) + c
        print('m :{}'.format(bin(msg)))
        print('a(x) :{}'.format(bin(a)))
        print('g(x) :{}'.format(bin(g)))
        print('с(x) :{}'.format(bin(c)))
        print('r :{}\n'.format(r))
        words.append(bin(a))
        words_before.append(bin(msg))
    print(words)
    print(words_before)

def main():
    #code_words()
    g = input("Enter your g(x): ")
    g = int(g, 2)  # g(x)
    l = int(input("Enter you l: "))
    r = len(bin(g)) - 3  # степень многочлена
    eps = input("Enter the accuracy(eps) with which you would like to get the result: ")  # точность
    eps = float(eps)
    Ne = 0
    N = 9 // (4 * (eps ** 2))  # количество раз повторения процедуры
    i = 0
    p_array = np.arange(0, 1.01, 0.01)
    Pe_array_1 = []
    Pe_array_2 = []
    Pe_array_3 = []
    for p in p_array:
        i = 0
        Ne = 0
        while i < N:
            msg = random.getrandbits(l)  # наше сообщение
            c = find_c(msg, g, r)
            a = (msg << r) + c
            e = gen_e(p, l, r)
            b = a ^ e
            s = calc_syndrome(b, g)
            if s == 0 and e != 0:
                Ne += 1
            i += 1
        Pe = Ne / N
        Pe_array_1.append(Pe)


    l = 2
    for p in p_array:
        i = 0
        Ne = 0
        while i < N:
            msg = random.getrandbits(l)  # наше сообщение
            c = find_c(msg, g, r)
            a = (msg << r) + c
            e = gen_e(p, l, r)
            b = a ^ e
            s = calc_syndrome(b, g)
            if s == 0 and e != 0:
                Ne += 1
            i += 1
        Pe = Ne / N
        Pe_array_2.append(Pe)



    l = 4
    for p in p_array:
        i = 0
        Ne = 0
        while i < N:
            msg = random.getrandbits(l)  # наше сообщение
            c = find_c(msg, g, r)
            a = (msg << r) + c
            e = gen_e(p, l, r)
            b = a ^ e
            s = calc_syndrome(b, g)
            if s == 0 and e != 0:
                Ne += 1
            i += 1
        Pe = Ne / N
        Pe_array_3.append(Pe)

    # Вывод графиков
    _, ax = plt.subplots()
    ax.plot(p_array, Pe_array_1, '-')
    ax.plot(p_array, Pe_array_2, '--')
    ax.plot(p_array, Pe_array_3, ':')
    plt.show()


if __name__ == '__main__':
    main()
