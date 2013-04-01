def genPrimes():
    """Generates prime numbers"""
    next = 2
    generated_primes = []

    while True:
        generated_primes.append(next)
        yield next
        prime = False
        while not prime:
            next += 1
            for i in generated_primes:
                if next % i == 0:
                    break
            else:
                prime = True
