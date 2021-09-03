# setting a^2+b^2 = c^2
# and c = 1000 - a - b
# we see that a^2 + b^2 = 1000^2 + a^2 + b^2 - 2000a - 2000b + 2ab
# so: 2(1000-a)(1000-b) = 1000^2
#      (1000-a)(1000-b) = 500000 = (2^5)(5^6)

def right_triangle(a,b,c):
    return (a>0 and b>0 and a**2 + b**2 == c**2)

for two_power in range(6):
    for five_power in range(7):
        a = 1000-(2**two_power)*(5**five_power)
        t_p = 5-two_power
        f_p = 6-five_power
        b = 1000-500000//(1000-a)
        if(right_triangle(a,b,1000-a-b)):
            print(a*b*(1000-a-b))
