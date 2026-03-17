def coprime(n1,n2):
    if n1 == 0: #### # if gcd = 1 → coprime
        return n2 == 1 # only this changd in coprime, leaving all code is exact same as gcd
    if n1<n2:
        n1, n2 = n2, n1 # by this we can swap the values of n1 and n2
    
    return coprime((n1%n2),n2) 

num1=int(input("num1 value"))
num2=int(input("num value"))

flag=coprime(num1,num2)
if flag:
    print(f" The coprime numbers of {num1} and {num2} is : {flag}")
else:
    print("Not a co prime number")

# output:
# num1 = 3
# num2 =5
#  The coprime numbers of 3 and 5 is : True
