#!/usr/bin/python2
from sage.all import *

class Lagrange:
    def __init__(self, xs, ys, mod=None):
        self.xs     = xs
        self.ys     = ys
        self.mod    = mod

        self.ps     = []
        self.x      = var('x')


    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)


    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m


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

        if mod is not None:
            coeffs = f.coefficients()
            f = 0

            for i in coeffs:
                f_numerator     = i[0].numerator()
                f_denominator   = i[0].denominator()

                f = f + x**i[1] * (int(f_numerator * self.modinv(int(f_denominator), int(self.mod))) % int(self.mod))

        return f
