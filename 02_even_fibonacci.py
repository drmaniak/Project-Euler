'''
    Sum of even Fibonacci terms in the range 0 to <= 4000000
'''

fibo = [0, 1]

while True:
    n = fibo[-1] + fibo[-2]
    if n <= 4000000:
        fibo.append(n)
    else:
        break

evenfibo = sum([i for i in fibo if (i%2 == 0)])

print("Sum of all even fibonacci terms under 4 million is: {evenfibo}")
    