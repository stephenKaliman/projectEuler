threes = 999//3
fives = 999//5
fifteens = fives//3

def sum_up_to(n):
    return n*(n+1)//2

sum_threes = 3*sum_up_to(threes)
sum_fives = 5*sum_up_to(fives)
sum_fifteens = 15*sum_up_to(fifteens)

ans = sum_threes+sum_fives-sum_fifteens

print(ans)
