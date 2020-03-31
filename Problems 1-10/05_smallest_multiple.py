'''
    Find the smallest number that is evenyl divisible by numbers from 1-20
'''

def getlcm(start, end):
    lcm = start

    for i in range(start, end+1):
        s = lcm

        while(s % i != 0):
            s += lcm

        lcm = s

    return lcm

getlcm(1, 20)