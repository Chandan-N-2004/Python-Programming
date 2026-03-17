def countfront(n):
    if n>4:
        return
    print(n,end=" ")
    count(n+1)
    print(n,end=" ")
count(1)

# `````````````````````
# output
# ````````````````````
# 1 2 3 4 4 3 2 1
