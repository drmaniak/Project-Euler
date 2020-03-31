
'''
    Find the sum of multiples of 3 or 5 in the range 0-1000
'''

threefive = sum([i for i in range(1000) if (i%3 == 0) or (i%5 == 0)])
print(f"Sum of all multiples of 3 or 5 under 1000 is {threefive}")