def ChkPrime(lst):
    primes = []
    for p in lst:
        isPrime = True
        for num in range(2,p):
            if p % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(p)
    print("prime numbers are",primes)
    print("Sum is",sum(primes))

