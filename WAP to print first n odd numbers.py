def evenodd(num):
    return num%2==0

countodd=int(input('enter the value'))
series= 1
print(f"first {countodd} odd number are: ")

while countodd > 0:
    flag = evenodd(series)
    if not flag:
        print(series, end=" ")
        countodd-=1
    series+=1

# ```````````````````````````
# output
# ```````````````````````````````
# first 5 odd number are: 
# 1 3 5 7 9 
