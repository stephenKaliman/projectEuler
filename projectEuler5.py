import math as m

def find_primes(upper):
    primes = []
    for i in range(2,upper+1):
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

p_to_twenty = find_primes(20)
product = 1
# print(p_to_twenty)
for p in p_to_twenty:
    factor = 1
    while(factor*p<20):
        factor*=p
    product*=factor

print(product)
