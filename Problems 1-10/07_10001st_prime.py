'''
    Find the 100001st prime number
'''

def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    i = 5
    while (i*i <= n): # Here we check only till root(n) because all larger numbers can be broken down into smaller factors <= root(n)
        if(n % i == 0 or n % (i+2) == 0):
            return False
        i += 6

    return True


def nthPrime(n):
    i = 1
    primes = []
    while True:
        if check_prime(i):
            primes.append(i)

            if len(primes) == n:
                print(primes)
                return primes[-1]

        i += 1


nthPrime(10001)
