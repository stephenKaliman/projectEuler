import math as m

num = 600851475143
upper = int(m.sqrt(num))

primes = [2,3,5,7]

for i in range(11,upper):
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

for p in reversed(primes):
    if(num%p==0):
        print(p)
        break
