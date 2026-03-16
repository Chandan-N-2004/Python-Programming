WAL to check whether the given number id prime or not using customise function

def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return f"{n} is a prime number"
    else:
        return f"{n} is a not prime number"

num = int(input('enter the prime number'))
print(prime(num))

``````````````````````````
ouput
```````````````````````````
1 is a not prime number
