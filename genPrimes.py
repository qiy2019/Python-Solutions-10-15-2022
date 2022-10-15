def genPrimes():
    primes = []
    x = 1
    while True:
        x += 1
        for n in primes:
            if x % n == 0: break
        else:
            primes.append(x)
            yield x