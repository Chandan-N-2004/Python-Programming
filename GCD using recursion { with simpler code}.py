def findgcd(n1,n2):
    if n1 == 0:
        return n2
    if n1<n2:
        n1, n2 = n2, n1 # by this we can swap the values of n1 and n2
    
    return findgcd((n1%n2),n2) 

num1=int(input("num1 value"))
num2=int(input("num value"))

result=findgcd(num1,num2)
print(f"The GCD of {num1} and {num2} is : {result}")

# output:
# The GCD of 10 and 25 is : 5
