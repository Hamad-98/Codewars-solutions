def square_digits(num):
    squaredOutput = ''
    for num in str(num):
        squaredOutput += str(int(num)**2)
    return int(squaredOutput)
