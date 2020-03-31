def sieveOfEratosthenes(n):
    primes = [True for i in range(n)]
    p = 2
    while (p*p <= n):
        if primes[p]:
            for i in range(p*2, n, p):
                primes[i] = False

        p += 1

    primes[0] = False
    primes[1] = False
    sumprimes = 0
    for p in range(n):
        if primes[p]:
            sumprimes += p

    return sumprimes

sieveOfEratosthenes(2000000)