def countback(n):
    if n<=0:
        return
    print(n,end=" ")
    countback(n - 1)
    print(n,end=" ")
countback(4)

# ````````````````````````````
# output
# ``````````````````````````````
# 4 3 2 1 1 2 3 4
