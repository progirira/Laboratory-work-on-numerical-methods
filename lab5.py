import numpy as np
import matplotlib.pyplot as plt

N1 = 10
N2 = 20
N3 = 30

x0 = 0.0
y0 = -2.0


def f(x: float, y: float):
    return (2 * y - 1) / (x - 1)


def f_x(x: float, y: float):
    return (-2 * y + 1) / pow(x - 1, 2)


def f_y(x: float):
    return 2 / (x - 1)


def clear_solution(step): # Точное решение
    xs = np.arange(0, 1.0, step)
    ys = [y0]
    for x in xs[1:]:
        ys.append(-5 / 2 * pow(x, 2) + 5 * x - 2)
    return ys


def Eiler_clear(step):   # Эйлера явный
    xs = np.arange(0, 1.0, step)
    ys = [y0]
    for x in xs[1:]:
        ys.append(ys[-1] + step * f(x, ys[-1]))
    return ys


def Taylor_second_order(step):  # Тейлора второго порядка
    xs = np.arange(0, 1.0, step)
    ys = [y0]
    for x in xs[1:]:
        ys.append(ys[-1] + step * f(x, ys[-1]) + pow(step, 2)/2*(f_x(x,
        ys[-1]) + (f_y(x)) * (f(x, ys[-1]))))
    return ys


def Adam_two_steps_clear(step):  # Адамса двухшаговый явный
    xs = np.arange(0, 1.0, step)
    ys = [y0, y0 + step * f(x0, y0) + pow(step, 2)/2*(f_x(x0,
        y0) + (f_y(x0)) * (f(x0, y0)))]

    for index, x in enumerate(xs[2:]):
        index += 2
        ys.append(ys[-1] + (step / 2) * (3*f(xs[index-1], ys[-1]) -
        f(xs[index-2], ys[-2])))
    return ys


def print_for_each_step(func, description):
    legend = []
    for n in [N1, N2, N3]:

        xs = np.arange(0, 1.0, 1 / n)
        ys = func(1 / n)
        plt.plot(xs, ys)

        plt.title(description)

        legend.append("N = " + str(n))

    plt.legend(legend)
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.show()
    return


if __name__ == '__main__':
    xs = np.arange(0, 1.0, 1 / N3)
    ys = clear_solution(1 / N3)
    plt.plot(xs, ys, label="Точное решение")
    plt.title("Точное решение")
    plt.legend(["N = " + str(N3)])
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.show()

    print_for_each_step(Eiler_clear, "Метод Эйлера явный")
    print_for_each_step(Taylor_second_order, "Метод Тейлора второго порядка")
    print_for_each_step(Adam_two_steps_clear, "Метод Адамса двухшаговый явный")

    plt.title("Методы с шагом N = " + str(N3))
    legend = []

    ys = clear_solution(1 / N3)
    plt.plot(xs, ys)
    legend.append("Точное решение")

    ys = Eiler_clear(1 / N3)
    plt.plot(xs, ys)
    legend.append("Метод Эйлера явный")

    ys = Taylor_second_order(1 / N3)
    plt.plot(xs, ys)
    legend.append("Метод Тейлора второго порядка")

    ys = Adam_two_steps_clear(1 / N3)
    plt.plot(xs, ys)
    legend.append("Метод Адамса двухшаговый явный")

    plt.legend(legend)
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.show()


