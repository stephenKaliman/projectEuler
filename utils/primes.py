import math as m

def find_primes(upper):
    if(upper<2):
        return []
    elif(upper==2):
        return [2]
    primes = [2]
    for i in range(2,upper):
        inner_upper = m.sqrt(i)
        prime = True
        for p in primes:
            if (p>=inner_upper):
                break
            if (i%p==0):
                prime = False
                break
        if(prime):
            primes.append(i)
    return primes
