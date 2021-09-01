a = 1
b = 2
sum = 0
while(b<=4000000):
    sum+=b
    a = a+2*b
    b = 2*a-b

print(sum)
