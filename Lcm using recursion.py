def findlcm(n1,n2,lcm):
    if lcm==(n1*n2):
        return lcm
    if lcm%n1==0 and lcm%n2==0:
        return lcm
    return findlcm(n1, n2, (lcm+1))
    
data1 = int(input())
data2= int(input())
lcm=max(data1, data2)
res=findlcm(data1,data2,lcm)
print(f"The lcm of {data1} and {data2} is : ",res)

# output:
# The lcm of 5 and 25 is :  25
