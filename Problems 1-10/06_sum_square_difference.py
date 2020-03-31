'''
    Find the difference between the sum of the squares and the square of the sum for the first 100 natural numbers
'''
def sumSquareDifference(s, e):
    sumsquare = sum([x**2 for x in range(s, e+1)])
    squaresum = sum([x for x in range(s, e+1)])**2
    print(sumsquare)
    print(squaresum)
    return squaresum - sumsquare

sumSquareDifference(1,100)
