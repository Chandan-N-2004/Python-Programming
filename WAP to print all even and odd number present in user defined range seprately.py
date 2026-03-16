def evenodd(num):
    return num % 2 ==0

sr = int(input("enter the sr value"))
er= int(input('enter the er value'))

if sr > er:
    print('Invalid I/P')

print("even number are")
for i in range(sr,er+1):
    flag = evenodd(i)
    if flag:
        print(i,end=" , ")
        
print("\n")
        
print("odd number are")
for i in range(sr,er+1):
    flag = evenodd(i)
    if not flag:
        print(i,end=" , ")

# ````````````````````````````````
# output
# ``````````````````````````````

# even number are
# 2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 20 , 22 , 24 , 26 , 28 , 30 , 

# odd number are
# 1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17 , 19 , 21 , 23 , 25 , 27 , 29 , 
