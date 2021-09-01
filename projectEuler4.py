# possibilities:
# 1: go through pairs of 3 digit numbers starting at (999,999) and check for palindrome
#       issue: hard to determine proper order to check if we have max palindrome
# 2: go through palindromes starting at 999999 and check if it factors into 2 3-digit numbers
#       issue: factoring lol

# 3: do both? simultaneously-ish
#       issue: nope lol

# decision: do (1)
# use am-gm to check if we can do better than our last palindrome 

import math as m

def check_sixdigit_palindrome(num):
    # print(num)
    return(num[0]==num[5] and num[1]==num[4] and num[2]==num[3])

max_palindrome = 0

for AM_doubled in reversed(range(999*2+1)):
    if((AM_doubled**2)//4 < max_palindrome):
        break
    a = (AM_doubled+1)//2
    b = (AM_doubled)//2
    current_palindrome = 0
    while(a<1000):
        to_check = list(str(a*b))
        if(check_sixdigit_palindrome(to_check)):
            current_palindrome = a*b
            break
        a+=1
        b-=1
    max_palindrome = max(max_palindrome, current_palindrome)
    # print(max_palindrome)

print(max_palindrome)
    


