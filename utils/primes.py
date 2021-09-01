import math as m

def find_primes(upper):
    primes = []
    for i in range(2,upper):
        inner_upper = m.sqrt(i)
        prime = True
        for p in primes:
            if (p>inner_upper):
                break
            if (i%p==0):
                prime = False
                break
        if(prime):
            primes.append(i)
    return primes

def find_primes(num_primes):
    primes = []
    i = 2
    while(len(primes)<num_primes):
        inner_upper = m.sqrt(i)
        prime = True
        for p in primes:
            if (p>inner_upper):
                break
            if (i%p==0):
                prime = False
                break
        if(prime):
            primes.append(i)
        i+=1
    return primes
