def evenodd(num):
    return num%2 ==0

counteven = int(input('enter the number'))
series = 1

print(f"first {counteven} Even number's are :")
while counteven > 0:
    flag = evenodd(series)
    if flag:
        print(series, end=" ")
        counteven -=1
    series +=1

# ```````````````````````````````````````
# output
# ``````````````````````````````````````````
# first 6 Even number's are :
# 2 4 6 8 10 12 
