#!/usr/bin/python2
from sage.all import *

class Lagrange:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

        self.ps = []
        self.x  = var('x')

    def interpolate(self):
        for x1, y in zip(self.xs, self.ys):
            p_numerator     = y
            p_denominator   = 1

            for x2 in self.xs:
                if x2 == x1:
                    continue

                p_numerator     *= (self.x - x2)
                p_denominator   *= (x1 - x2)

            self.ps.append((p_numerator) / p_denominator)

        g = sum(self.ps)

        f = 0

        for i in g.coefficients():
            f = f + x**i[1] * i[0]

        return f
