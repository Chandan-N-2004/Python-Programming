def findGCD(n1,n2):
    hcf=1 # bczz all the num's will have 1 as the common number
    
    lower=n1
    if n2<n1:
        lower = n2
    for i in range(2,lower+1):
        if n1% i ==0 and n2 % i ==0:
            hcf =i
    return hcf

num1=int(input("Enter teh 1st number"))
num2=int(input("Enter teh 2nd number"))

res = findGCD(num1,num2)
print(f"the gcd of {num1} and {num2} is : {res}")

# ``````````````````````````
# output
# `````````````````````````
# the gcd of 15 and 10 is : 5
