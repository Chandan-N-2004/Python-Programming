def square(n,i=1):
    if i*i>n:
        return
    if n % i == 0:
        print(i, end=" ")
        if i!=(n//i):
            print((n//i), end=" ")
    return square(n,(i+1))

n=int(input())
square(n)

# output:
# n = 8
# 1 8 2 4
