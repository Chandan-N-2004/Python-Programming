def prime(n,i=1, countfactor=0):
    if i*i>n:
        return countfactor == 2
    if n % i == 0:
        countfactor += 1
        if i!=(n//i):
            countfactor += 1
    return prime(n,(i+1), countfactor)

n=int(input())
prime(n)
result = prime(n)

if result:
    print(f"input = {n}: It's a Prime Number")
else:
    print("Output: Not a Prime Number")

# output:
# n = 19
# input = 19: It's a Prime Number
