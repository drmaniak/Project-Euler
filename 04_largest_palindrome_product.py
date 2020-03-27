'''
    Print the largest palindrome product of two 3 digit numbers
'''
pals = sorted([x * y for x in range(100,1000) for y in range(x,1000) if str(x*y) == str(x*y)[::-1]])
print(pals[-1])