#class for complex numbers
class complex:
    #constructor to initialize the real and the imaginary part of the complex instance
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #function that prints a complex number
    def print(self):
        #if the real part is different than 0, we print it
        #otherwise we don't
        if self.real != 0:
            print(self.real, end='', sep='')
        #if the imaginary part is grater than 0 we print + and the imaginary part
        if self.imag > 0:
            print("+", self.imag, "*i", end='', sep='')
        #if the imaginary part is less than 0 we print only the imaginary part
        elif self.imag < 0:
            print(self.imag, "*i", end='', sep='')

    #overload for the "=" operator between complex numbers
    def __eq__(self, other):
        #assign the real and imaginary part to the instance
        self.real = other.real
        self.imag = other.imag

    #overload for the "+" operator between complex numbers
    def __add__(self, other):
        #temporar variables
        (real, imag) = (0, 0)
        #the temporal real is equal to the previous one plus the one we want to add
        real = self.real + other.real
        #same for imaginary part
        imag = self.imag + other.imag
        #we return a complex instance with temporal real and imaginary parts calculated previously
        return complex(real, imag)

    def __sub__(self, other):
        (real, imag) = (0, 0)
        real = self.real - other.real
        imag = self.imag - other.imag
        return complex(real, imag)

    #overload for the "*" operator between complex numbers
    def __mul__(self, other):
        # temporal variables
        (real, imag) = (0, 0)
        #we compute both temporal real and imaginary parts by formulas
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        # we return a complex instance with temporal real and imaginary parts calculated previously
        return complex(real, imag)


#class for polynomials with complex coefficients
class polynomial:
    #constructor to initialize the coefficients of the current instance
    #to a list of complex coefficients
    def __init__(self, coeffs):
        self.coeffs = coeffs

    #functiont that returns the degree/rank of the current polynomial instance
    def degree(self):
        return len(self.coeffs) - 1

    #overload for the "=" operator operator between polynomials
    def __eq__(self, other):
        #we assign the other list of coefficients to the current list
        self.coeffs = other.coeffs

    #overload for the "+" operator operator between polynomials
    def __add__(self, other):
        #temporal list of coefficients for both actual and the other polynomials
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        #we keep the list with less coefficients in the first temporal list
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)
        #we add if front of the first list NULL complex numbers to make the number of
        #coefficients equal between the two lists
        coeffs1 = [complex(0, 0)] * (len(coeffs2) - len(coeffs1)) + coeffs1
        #we add all the coefficients and store the result for every coefficient in a new list
        coeffs = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
        #return an instance of a polynomial with the coefficients computed before
        return polynomial(coeffs)

    def __sub__(self, other):
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)
        coeffs1 = [complex(0, 0)] * (len(coeffs2) - len(coeffs1)) + coeffs1
        coeffs = [coeffs1[i] - coeffs2[i] for i in range(len(coeffs1))]
        return polynomial(coeffs)

    #overload for the "*" operator between polynomials
    def __mul__(self, other):
        #temporal list of coefficients for both actual and the other polynomials
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        #creating an empty list of complex coefficients with the rank of first polynomial's rank
        #plus the second polynomial's rank
        coeffs = [complex(0, 0) for i in range(self.degree() + other.degree() + 1)]
        #multiply all coefficients of the first polynomial with every coefficient
        #of the second polynomial
        for i in range(len(coeffs1)):
            for j in range(len(coeffs2)):
                coeffs[i + j] = coeffs[i + j] + coeffs1[i] * coeffs2[j]
        #return an instance of a polynomial with the coefficients computed before
        return polynomial(coeffs)

    #fucntions that evaluates a polynomial in a given point
    def evaluate(self, x):
        #result is a NULL complex number
        result = complex(0, 0)
        #degree stores the degree/rank of the evaluated instance of a polynomial
        degree = self.degree()
        #for every coefficient of the current instance
        for i in range(degree + 1):
            #add to the result real part the product between the real part of the current coefficient
            #and the point that was given
            result.real = result.real + self.coeffs[i].real * x
            #add to the result imaginary part the product between the imaginary part of the current coefficient
            #and the point that was given
            result.imag = result.imag + self.coeffs[i].imag * x
        #return a complex number that is the result of evaluating the polynomial in the given point
        return result

    #function that prints a polynomial
    def print(self):
        #degree stores the degree/rank of the current instance of a polynomial
        degree = self.degree()
        #for every coefficient of the polynomial
        for i in range(len(self.coeffs)):
            #print "+" between each coefficient
            if i > 0:
                print(" + ", end='')
            print("(", end='', sep='')
            #if the real part exists, we print it
            if self.coeffs[i].real != 0:
                print(self.coeffs[i].real, end='', sep='')
            #if the imaginary part exists we print it with the correct sign before it
            if self.coeffs[i].imag > 0:
                print("+", end='', sep='')
            if self.coeffs[i].imag == 0:
                print(")", end='')
            else:
                print(self.coeffs[i].imag, "*i)*x^", degree - i, end='', sep='')

#class for matrices where every element is a polynomial with complex coefficients
class matrix:
    #constructor to initialize the matrix and it's rank
    def __init__(self):
        self.vec = []
        self.n = 0

    #function to initialize the matrix with a polynomial (rank becomes 1)
    def initialise(self, other):
        #delete the previous matrix
        del self.vec[:]
        #append to the vector of elements the single polynomial
        self.vec.append([other])
        #the rank of the matrix is 1
        self.n = 1

    #function that prints the
    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                self.vec[i][j].print()
                print(end="     ")
            print()
        print('\n')

    #function that adds a new line and a column to a matrix
    def increase(self, other):
        #for every line we add a new column
        for i in range(self.n):
            self.vec[i].append(other)
        #we add the new line
        self.vec.append([other for i in range(self.n+1)])
        #the rank of the matrix increases by 1
        self.n = self.n + 1

    #function that evaluates the matrix in a given point
    def evaluate(self, x):
        #by evaluating the matrix results another matrix declared below
        tmp = []
        #the result matrix is in the first place empty (only NULL complex numbers)
        tmp = [[complex(0, 0) for i in range(self.n)] for j in range(self.n)]
        #evaluate every polynomial and store it's result in the result matrix
        for i in range(self.n):
            for j in range(self.n):
                tmp[i][j] = self.vec[i][j].evaluate(x)
        #return the return matrix
        return tmp

    #overload for "=" operator between matrices
    def __eq__(self, other):
        #asign element from the other matrix to the current instance where it belongs
        for i in range(self.n):
            for j in range(self.n):
                self.vec[i][j] = other.vec[i][j]

    #overload for "+" operator between matrices
    def __add__(self, other):
        #temporal matrix where we store the result by adding the two matrices
        tmp = matrix()
        #in the first place the result matrix is empty (only NULL polynomials)
        tmp.vec = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        #add the elements on the same line and column and store it in the result matrix
        for i in range(self.n):
            for j in range(self.n):
                tmp.vec[i][j] = self.vec[i][j] + other.vec[i][j]
        #rank of the result matrix is equal with the rank of one of the matrices in the equation
        tmp.n = self.n
        #return the matrix
        return tmp

    def __sub__(self, other):
        tmp = matrix()
        tmp.vec = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                tmp.vec[i][j] = self.vec[i][j] - other.vec[i][j]
        tmp.n = self.n
        return tmp

    #overload for "*" operator between matrices
    def __mul__(self, other):
        #temporal matrix where we store the result by multiplying the two matrices
        tmp = matrix()
        #in the first place the result matrix is empty (only NULL polynomials)
        tmp.vec = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        #we multiply the two matrices and store the result in the result matrix
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    tmp.vec[i][j] = tmp.vec[i][j] + self.vec[i][k] * other.vec[k][j]
        #rank of the result matrix is equal with the rank of one of the matrices in the equation
        tmp.n = self.n
        #return the matrix
        return tmp

    def det(self):
        mat = [[polynomial([]) for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.vec[i][j]

        N = self.n - 1
        for k in range(self.n - 1):
            for i in range(N):
                for j in range(N):
                    mat[i][j] = mat[i][j] * mat[i+1][j+1] - mat[i+1][j] * mat[i][j+1]
            N = N - 1

        return mat[0][0]

#array where we store all the matrices we've created so we can make operations on them
matrices = []

#function for menu options
def menu():
    #priting all the possible operations the user can choose from
    print("\nMenu options:")
    print("Option 1: Initialize a new matrix with a single polynomial")
    print("Option 2: Print a matrix")
    print("Option 3: Increase a matrix with a line and a column")
    print("Option 4: Evaluate a matrix in a given point")
    print("Option 5: Add 2 matrices with the same rank")
    print("Option 6: Multimply 2 matrices with the same rank")
    print("Option 7: Compute the determinant of a matrix")
    print("\nOption 8: Quit.\n")
    #reading the option the user wants
    option = input("Select your option: ")

    #initialize a new matrix
    if option == '1':
        #temporal matrix
        tmp = matrix()
        #temporal array of coefficients
        coeffs = []
        #read the rank of the polynomial the new matrix will be initialized with
        rank = int(input("Read the rank of the polynomial: "))
        print("Read the complex coefficients of the polynomial")
        #read the complex coefficients of the polynomial
        for i in range(rank+1):
            print("x^", rank-i, end=': ', sep='')
            real = int(input())
            imag = int(input())
            coeffs.append(complex(real, imag))
        #initialize the matrix with the polynomial we've read
        tmp.initialise(polynomial(coeffs))
        #add the current matrix to the array of matrices
        matrices.append(tmp)

    #print a matrix
    elif option == '2':
        #read the indices of the matrix the user wants to be printed
        ind = int(input("Which matrix do you want to be printed? "))
        # check if the selected matrix exists
        if ind > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #print the matrix
            matrices[ind - 1].print()

    #increase a matrix
    elif option == '3':
        #temporal array of coefficients the matrix will be increased with
        coeffs = []
        #read the indices of the matrix that will be increased
        ind = int(input("Which matrix do you want to be increased? "))
        #check if the selected matrix exists
        if ind > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #read the rank of the polynomial used to increase the matrix
            rank = int(input("Read the rank of the polynomial: "))
            print("Read the complex coefficients of the polynomial")
            #read the coefficients of the polynomial
            for i in range(rank + 1):
                print("x^", rank - i, end=': ', sep='')
                real = int(input())
                imag = int(input())
                coeffs.append(complex(real, imag))
            #increase the selected matrix with the polynomial we've read
            matrices[ind - 1].increase(polynomial(coeffs))

    #evaluate a matrix in a given point
    elif option == '4':
        #read the indices of the matrix that will be evaluated
        ind = int(input("Which matrix do you want to be evaluated? "))
        #check if the selected matrix exists
        if ind > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #read the point in where the matrix will be evaluated
            x = int(input("In which point do you want the matrix to be evaluated? "))
            #result stores the matrix equal to the evaluation of every polynomial of the matrix
            result = matrices[ind - 1].evaluate(x)
            #N is the rank of the matrix
            N = matrices[ind - 1].n
            #print the resulted matrix of the evaluation in x
            for i in range(N):
                for j in range(N):
                    result[i][j].print()
                    print(end="     ")
                print()
            print('\n')

    #add 2 matrices. Add the 2nd matrix to the first one
    elif option == '5':
        #read the indices of the matrix that will get added
        ind1 = int(input("Which matrix do you want to be added? "))
        #check if the selected matrix exists
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #read the indices of the 2nd matrix that will be added to the first one
            ind2 = int(input("Which matrix do you want to be added to the first one? "))
            #check if the selected matrix exists
            if ind2 > len(matrices):
                print("This matrix doesn't exist. Read more matrices")
            else:
                #check if the selected matrices have the same rank
                #if they doesn't have the same rank, we can't add them
                if matrices[ind2 - 1].n != matrices[ind1 - 1].n:
                    print("The 2 matrices you selected doesn't have the same rank.")
                else:
                    #if we got to this point it means we got 2 valid matrices with the same rank
                    #so we add the 2nd matrix to the frist one
                    matrices[ind1 - 1] = matrices[ind1 - 1] + matrices[ind2 - 1]

    #multiply 2 matrices. Store the result in the first matrix
    elif option == '6':
        #read the indices of the matrix that will get multiplied
        ind1 = int(input("Which matrix do you want to be multiplied? "))
        #check if the selected matrix exists
        if ind1 > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #read the indices of the 2nd matrix
            ind2 = int(input("Which matrix do you want to be multiplied to the first one? "))
            #check if the selected matrix exists
            if ind2 > len(matrices):
                print("This matrix doesn't exist. Read more matrices")
            else:
                #check if the selected matrices have the same rank
                #if they doesn't have the same rank, we can't add them
                if matrices[ind2 - 1].n != matrices[ind1 - 1].n:
                    print("The 2 matrices you selected doesn't have the same rank.")
                else:
                    #if we got to this point it means we got 2 valid matrices with the same rank
                    #so we multiply them and store the result in the first matrix
                    matrices[ind1 - 1] = matrices[ind1 - 1] * matrices[ind2 - 1]

    #compute the determinant of a matrix
    elif option == '7':
        #read the indices of the matrix
        ind = int(input("Determinant of which matrix do you want to be computed? "))
        #check if the matrix exists
        if ind > len(matrices):
            print("This matrix doesn't exist. Read more matrices")
        else:
            #compute the determinant that is a polynomial
            poly = matrices[ind - 1].det()
            #print the determinant
            poly.print()
            print('\n')


    #terminate the program
    elif option == '8':
        return

    #print that the user selected a wrong option
    else:
        print("The option you have selected is incorrect. Try again!")

    menu()

menu()
