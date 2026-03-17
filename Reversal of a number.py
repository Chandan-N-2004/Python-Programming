def res_rev(n,rev):
    if n<=0:
        return rev
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return res_rev(n,rev)

num=int(input("Enter the value:"))
res=res_rev(num, 0)
print(f"the reversed num of {num} is {res}")

# output:
# the reversed num of 25 is 52
