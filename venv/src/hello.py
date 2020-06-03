from pandas import np
import hello as locus
import seaborn as sea
import matplotlib.pyplot as matplot
import numpy as nump
import math



Angles = [2.3561944901925003, 3.9269908169875, 5.4977871437825, 7.0685834705775]
length = 200
x = -31.25
y = 0


def getroots(transet, Gain):
    number = transet[0]
    denumber = transet[1]
    The_Roots = []

    for g in Gain:
        charac_equation = denumber + g * number
        charac_roots = nump.roots(charac_equation)
        charac_roots.sort()
        The_Roots.append(charac_roots)

    The_Roots = nump.vstack(The_Roots)

    return The_Roots


def plotting(The_Roots):
    Real = nump.real(The_Roots)
    Value = nump.imag(The_Roots)

    colors = ['g', 'b', 'c', 'r', 'm']
    f, location = matplot.subplots()

    location.set_xlabel('real')
    location.set_ylabel('imaginary')
    location.axvline(x=0, color='k', lw=1)
    location.grid(True, which='both')
    location.scatter(Real[0, :], Value[0, :], marker='x', color='B')
    location.scatter(Real[-1, :], Value[-1, :], marker='o', color='R')

    treal = Real[1:-1, :]
    tvalue = Value[1:-1, :]
    color_range = range(treal.shape[1])
    asymptoes_lines = asympt()

    for i in range(1, len(asymptoes_lines)):
        matplot.plot([asymptoes_lines[0][0], asymptoes_lines[i][0]], [asymptoes_lines[0][1], asymptoes_lines[i][1]],
                     asymptoes_lines[i][2], linestyle='--', dashes=(8, 8))
    matplot.plot(-9.1501, 0, 'o', color='R', label='Break point')
    matplot.plot(0, 22.803508501, 'x', color='B', label='Imaginary')
    matplot.plot(0, -22.803508501, 'x', color='B', label='Imaginary')
    matplot.legend()

    for r, i, j in zip(treal.T, tvalue.T, color_range):
        location.plot(r, i, color=colors[j])

    return f, location


def transferFunc(number, denumber):
    number = nump.array(number, dtype=nump.float64)
    denumber = nump.array(denumber, dtype=nump.float64)
    size = len(denumber) - len(number)
    t = nump.zeros(size)
    number = nump.concatenate((t, number))
    result = nump.vstack((number, denumber))
    return result


def asympt():
    asym = [[x, y]]
    for i in range(0, 4):
        c = 'g'
        if i % 2 == 1:
            c = 'k'
        asym += [[x + length * math.cos(Angles[i]), length * math.sin(Angles[i]), c]]
    return asym


if __name__ == '__main__':
    num = [1]
    denum = [1, 125, 5100, 65000, 0]

    answer = locus.transferFunc(num, denum)
    g = np.linspace(0.0, 999999999, num=50000)
    roots = locus.getroots(answer, g)

    fig, ax = locus.plotting(roots)
    locus.matplot.show()