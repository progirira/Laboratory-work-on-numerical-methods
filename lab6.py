import math

import numpy as np
import matplotlib.pyplot as plt

N1 = 10
N2 = 20
epsilon = pow(10, -5)


def exact_solution(step): # Точное решение
    xs = np.arange(0, 1.0, step)
    ys = []
    for x in xs:
        ys.append(math.exp(-x) + math.exp(x) + 4.8 * pow(x, 2) - 4.8 * x - 2)
    return xs, ys


def z_x(x: float, y: float):
    return y + 11.6 + 4.8 * x * (1 - x)

def Koshi(z0, n): # Метод Коши
    ys = [0]
    zs = [z0]
    h = 1/n
    for i in range(1, n):
        x_n = i * h
        y_half = ys[i-1] + h / 2 * zs[i-1]
        z_half = zs[i-1] + h / 2 * z_x(x_n, ys[i-1])

        y_n = ys[i-1] + h * z_half
        x_half = x_n + h / 2
        z_n = zs[i-1] + h * z_x(x_half, y_half)
        ys.append(y_n)
        zs.append(z_n)
    return ys, zs


def shooting(n): # Метод стрельбы
    mu_prev = 100
    mu_cur = 0
    while abs(mu_cur - mu_prev) >= epsilon:
        ys, zs = Koshi(mu_cur, n)
        fi = ys[-1] + zs[-1] - 2 * np.exp(1) - 2.8
        fi_dev = np.exp(1)
        mu_cur, mu_prev = mu_cur - fi / fi_dev, mu_cur
    return ys

def progonka(n): # Метод прогонки
    step = 1 / n
    lambdas = [0]
    mus = [0]

    for i in range(1, n + 1):
        A = 2 + pow(step, 2)
        x = i * step
        B = pow(step, 2) * (11.6 + 4.8 * x * (1 - x))
        lambdas.append(1 / (A - lambdas[-1]))
        mus.append((mus[-1] - B) / (A - lambdas[-1]))
    value = mus[-1]
    ys = []
    for i in range(n, 0, -1):
        value = lambdas[i - 1] * value + mus[i - 1]
        ys.append(value)
    return list(reversed(ys))


if __name__ == '__main__':
    for n in [N1, N2]:
        legend = []
        legend.append("Точное решение")
        xs, ys = exact_solution(1 / n)
        plt.plot(xs, ys, label=f"Точное решение", color='blue')
        legend.append("Метод стрельбы")
        shooting_ys = shooting(n)
        plt.plot(xs, shooting_ys, label=f"Метод стрельбы", color='green')
        legend.append("Метод прогонки")
        progonka_ys = progonka(n)
        plt.plot(xs, progonka_ys, label=f"Метод прогонки", color='red')

        plt.legend(legend)
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.show()
