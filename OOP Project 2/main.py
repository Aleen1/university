class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        self.real = other.real
        self.imag = other.imag

    def print(self):
        if self.real != 0:
            print(self.real, end='', sep='')
        if self.imag > 0:
            print("+", self.imag, "*i", end='', sep='')
        elif self.imag < 0:
            print(self.imag, "*i", end='', sep='')

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

        coeffs1 = [complex(0, 0)] * (len(coeffs2) - len(coeffs1)) + coeffs1
        coeffs = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
        return polynomial(coeffs)

    def __mul__(self, other):
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        coeffs = [complex(0, 0) for i in range(self.degree() + other.degree() + 1)]
        for i in range(len(coeffs1)):
            for j in range(len(coeffs2)):
                coeffs[i + j] = coeffs[i + j] + coeffs1[i] * coeffs2[j]
        return polynomial(coeffs)

    def evaluate(self, x):
        result = complex(0, 0)
        degree = self.degree()
        for i in range(degree + 1):
            result.real = result.real + self.coeffs[i].real * x
            result.imag = result.imag + self.coeffs[i].imag * x
        return result

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
    def __init__(self):
        self.vec = []
        self.n = 0

    def initialise(self, other):
        del self.vec[:]
        self.vec.append([other])
        self.n = 1

    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                self.vec[i][j].print()
                print(end="     ")
            print()
        print('\n')

    def increase(self, other):
        for i in range(self.n):
            self.vec[i].append(other)
        self.vec.append([other for i in range(self.n+1)])
        self.n = self.n + 1

    def evaluate(self, x):
        tmp = []
        tmp = [[complex(0, 0) for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                tmp[i][j] = self.vec[i][j].evaluate(x)
        return tmp

    def __eq__(self, other):
        for i in range(self.n):
            for j in range(self.n):
                self.vec[i][j] = other.vec[i][j]

    def __add__(self, other):
        tmp = matrix()
        tmp.vec = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                tmp.vec[i][j] = self.vec[i][j] + other.vec[i][j]
        tmp.n = self.n
        return tmp

    def __mul__(self, other):
        tmp = matrix()
        tmp.vec = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    tmp.vec[i][j] = tmp.vec[i][j] + self.vec[i][k] * other.vec[k][j]
        tmp.n = self.n
        return tmp

matrices = []

def menu():
    print("\nMenu options:")
    print("Option 1: Initialize a new matrix with a single polynomial")
    print("Option 2: Print a matrix")
    print("Option 3: Increase a matrix with a line and a column")
    print("Option 4: Evaluate a matrix in a given point")
    print("Option 5: Add 2 matrices with the same rank")
    print("Option 6: Multimply 2 matrices with the same rank")
    print("\nOption 7: Quit.\n")
    option = input("Select your option: ")

    if option == '1':
        tmp = matrix()
        coeffs = []
        rank = int(input("Read the rank of the polynomial: "))
        print("Read the complex coefficients of the polynomial")
        for i in range(rank+1):
            print("x^", rank-i, end=': ', sep='')
            real = int(input())
            imag = int(input())
            coeffs.append(complex(real, imag))
        tmp.initialise(polynomial(coeffs))
        matrices.append(tmp)

    elif option == '2':
        ind = int(input("Which matrix do you want to be printed? "))
        matrices[ind - 1].print()

    elif option == '3':
        coeffs = []
        ind = int(input("Which matrix do you want to be increased? "))
        rank = int(input("Read the rank of the polynomial: "))
        print("Read the complex coefficients of the polynomial")
        for i in range(rank + 1):
            print("x^", rank - i, end=': ', sep='')
            real = int(input())
            imag = int(input())
            coeffs.append(complex(real, imag))

        matrices[ind - 1].increase(polynomial(coeffs))

    elif option == '4':
        ind = int(input("Which matrix do you want to be evaluated? "))
        x = int(input("In which point do you want the matrix to be evaluated? "))
        result = matrices[ind - 1].evaluate(x)
        N = matrices[ind - 1].n
        for i in range(N):
            for j in range(N):
                result[i][j].print()
                print(end="     ")
            print()
        print('\n')

    elif option == '5':
        ind1 = int(input("Which matrix do you want to be added? "))
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
            return
        ind2 = int(input("Which matrix do you want to be added to the first one? "))
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
            return

        if matrices[ind2 - 1].n != matrices[ind1 - 1].n:
            print("The 2 matrices you selected doesn't have the same rank.")
            return

        matrices[ind1 - 1] = matrices[ind1 - 1] + matrices[ind2 - 1]
        del matrices[ind2 - 1]

    elif option == '6':
        ind1 = int(input("Which matrix do you want to be multiplied? "))
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
            return
        ind2 = int(input("Which matrix do you want to be multiplied with the first one? "))
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
            return

        if matrices[ind2 - 1].n != matrices[ind1 - 1].n:
            print("The 2 matrices you selected doesn't have the same rank.")
            return

        matrices[ind1 - 1] = matrices[ind1 - 1] * matrices[ind2 - 1]
        del matrices[ind2 - 1]

    elif option == '7':
        return

    else:
        print("The option you have selected is incorrect. Try again!")
    menu()

menu()
