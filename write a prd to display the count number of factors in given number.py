def factor(n):
    print(f"The factor of {n} is:")
    for i in range(1,(n+1)):
        if n % i ==0:
            print(i,end=" ")

def countfactors(n):
    countfact, countcycles = 0,0
    for i in range (1,(n+1)):
        countcycles+=1
        if n % i ==0:
            countfact+=1
    return countfact, countcycles

n = int(input('enter the value'))
factor(n)
print('\n====')
resfact, rescycle = countfactors(n)
print(f'The sum of factors of {n} is: {resfact}')

# ````````````````````
# output
# ```````````````````
# The factor of 6 is:
# 1 2 3 6 
# ====
# The sum of factors of 6 is: 4
