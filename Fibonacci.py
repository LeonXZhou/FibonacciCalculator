def MaxtrixMultiplication(firstMatrix,secondMatrix):
    # A helper function that multiplies 2 2 by 2 matrixes together
    outPutMatrix11 = firstMatrix[0][0] * secondMatrix[0][0] + firstMatrix[0][1] * secondMatrix[1][0]
    outPutMatrix12 = firstMatrix[0][0] * secondMatrix[0][1] + firstMatrix[0][1] * secondMatrix[1][1]
    outPutMatrix21 = firstMatrix[1][0] * secondMatrix[0][0] + firstMatrix[1][1] * secondMatrix[1][0]
    outPutMatrix22 = firstMatrix[1][0] * secondMatrix[0][1] + firstMatrix[1][1] * secondMatrix[1][1]
    return [[outPutMatrix11,outPutMatrix12],[outPutMatrix21,outPutMatrix22 ]]

def MatrixPower(inputMatrix, n):
    # A helper function that calculates a matrix to the nth power using the MatrixMultiplication Function
    if n == 1:
        return inputMatrix
    else:
        return MaxtrixMultiplication(inputMatrix,MatrixPower(inputMatrix,n-1))

def fib(n):
    # The fibonacci function that uses the MatrixPower function to calculate the nth fibonacci number
    if n <= 0:
        print("Invalid Input n must be greater than 0")
    elif n == 1:
        print("The 1st Fibonacci number is 1")
    elif n == 2:
        print("The 2nd Fibonacci number is 1")
    else:
        Output = MatrixPower([[1,1],[1,0]],n-1)[0][0]
        print("for n = {}, the Fibonacci number is {}".format(n,Output))

userInput=input("Which Fibonacci number would you like to calculate:")
fib(int(userInput))
