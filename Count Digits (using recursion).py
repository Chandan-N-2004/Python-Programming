def countdigit(n,count):
    if n<=0:
        return count

    n=n//10
    count=count+1
    return countdigit(n,count)

num=int(input("enter a value"))
res=countdigit(num,0)
print(f'The count of digits in {num} is {res}')

# output:
# The count of digits in 3468271 is 7
