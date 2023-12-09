eps = 0.000005
import math

#Начальная функция f
def f(x):
    return 2 * (1 / math.tan(x)) - pow(x, 2)

#Производная начальной функции f
def der_f(x):
    return -2 / (math.sin(x)**2) - 2 * x

def fi_for_simple_iteration(x):
    return math.pi/2 - math.atan((x**2)/2)

#1. Метод половинного деления
def MPD(f=f, a= math.pi/4, b = math.pi/2-0.1):
    n = 0
    while abs(b - a) > eps:
        n += 1
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    return x, n

#2. Метод Ньютона
def Newtons_method(x0 = math.pi/4):
    n = 1
    xn = x0
    xn1 = xn - f(xn) / der_f(xn)
    while abs(xn1-xn) > eps:
        n += 1
        xn = xn1
        xn1 = xn - f(xn) / der_f(xn)
    return xn1, n

#3. Модифицированный Метод Ньютона
def modif_Newtons_method(x0 = math.pi/4):
    n = 1
    xn = x0
    xn1 = xn - f(xn) / der_f(x0)
    while abs(xn1-xn) > eps:
        n += 1
        xn = xn1
        xn1 = xn - f(xn) / der_f(x0)
    return xn1, n


#4. Метод неподвижных хорд
def method_Fixed_chords(x0 = math.pi/4):
    n = 1
    xn = x0
    xn1 = xn - f(xn) / der_f(x0)
    while abs(xn1 - xn) > eps:
        n += 1
        xn = xn1
        xn1 = xn - f(xn) / der_f(x0)
    print(xn1)
    return xn1, n

#5. Метод подвижных хорд
def method_Unfixed_chords(x0 = math.pi/4):
    n = 1
    xn = x0
    xn1 = xn - f(xn) / der_f(xn)
    while abs(xn1 - xn) > eps:
        n += 1
        xn = xn1
        xn1 = xn - f(xn) / der_f(xn)
    print(xn1)
    return xn1, n

#5. Метод простой итерации
def method_Simple_iteration(x0 = math.pi/4):
    n = 1
    xn = x0
    xn1 = fi_for_simple_iteration(xn)
    while abs(xn1 - xn) > eps:
        n += 1
        xn = xn1
        xn1 = fi_for_simple_iteration(xn)
    return xn1, n



def main():
    a = math.pi / 4
    b = math.pi / 2 - 0.1
    print("Значение начальной функции f(pi/4) = " + str(f(a)))
    print("Значение начальной функции f(pi/2-0.1) = " + str(f(b)))

    print("Значение функции fi(pi/4) = " + str(
        fi_for_simple_iteration(a)))
    print("Значение функции fi(pi/2-0.1) = " + str(
        fi_for_simple_iteration(b)))

    x, n = MPD()
    print("Метод половинного деления: x = " + str(x) + ", n = " + str(n))
    x, n = Newtons_method()
    print("Метод Ньютона: x = " + str(x) + ", n = " + str(n))
    x, n = modif_Newtons_method()
    print("Модифицированный Метод Ньютона: x = " + str(x) + ", n = " + str(n))
    x, n = method_Fixed_chords()
    print("Метод неподвижных хорд: x = " + str(x) + ", n = " + str(n))
    x, n = method_Unfixed_chords()
    print("Метод подвижных хорд: x = " + str(x) + ", n = " + str(n))
    x, n = method_Simple_iteration()
    print("Метод простой итерации: x = " + str(x) + ", n = " + str(n))



if __name__ == '__main__':
    main()
