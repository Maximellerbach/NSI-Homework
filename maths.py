import math
import matplotlib.pyplot as plt

A = 1
b = math.pi/2
c = math.pi/2


def iterate(t, A, b, c):
    return A * math.cos(b*t + c)


if __name__ == '__main__':

    ys = []
    xs = []

    for i in range(0, 180*4):
        ys.append(iterate(i/180, A, b, c))
        xs.append(i/180)

    plt.plot(xs, ys)
    plt.show()
