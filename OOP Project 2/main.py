class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        self.real = other.real
        self.imag = other.imag

    def __add__(self, other):
        (real, imag) = (0, 0)
        real = self.real + other.real
        imag = self.imag + other.imag
        return complex(real, imag)

    def __mul__(self, other):
        (real, imag) = (0, 0)
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return complex(real, imag)

class polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def degree(self):
        return len(self.coeffs) - 1

    def __eq__(self, other):
        self.coeffs = other.coeffs

    def __add__(self, other):
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)

        coeffs1 = [0] * (len(coeffs2) - len(coeffs1)) + coeffs1
        coeffs = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]

        return polynomial(coeffs)

    def __mul__(self, other):
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        coeffs = [complex(0, 0) for i in range(self.degree() + other.degree() + 1)]
        for i in range(len(coeffs1)):
            for j in range(len(coeffs2)):
                coeffs[i + j] = coeffs[i + j] + coeffs1[i] * coeffs2[j]

        return polynomial(coeffs)

    def print(self):
        degree = self.degree()
        for i in range(len(self.coeffs)):
            if i > 0:
                print(" + ", end='')
            print("(", end='', sep='')
            if self.coeffs[i].real != 0:
                print(self.coeffs[i].real, end='', sep='')
            if self.coeffs[i].imag > 0:
                print("+", end='', sep='')
            if self.coeffs[i].imag == 0:
                print(")", end='')
            else:
                print(self.coeffs[i].imag, "*i)*x^", degree - i, end='', sep='')

class matrix:
    def __init__(self, other):
        self.vec = []
        self.vec.append([other])
        self.n = 1

    def increase(self, other):
        for i in range(self.n):
            self.vec[i].append(other)
        self.vec.append([other for i in range(self.n+1)])
        self.n = self.n + 1
        print("\n")

    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                self.vec[i][j].print()
                print(end="     ")
            print()


coeffs = [complex(2, -3), complex(1, 6), complex(0, -4)]
x = polynomial(coeffs)
"""y = polynomial(coeffs)
z = x * y
z.print()"""

M = matrix(x)
M.print()
x = x*x
M.increase(x)
M.print()
x = x+x
M.increase(x)
M.print()