n = int(input("enter ur desire value")) # 4315
count = 0

if n<0: # using this condition we can convert the negative number into positive number 
    n = n*-1
    
while n > 0:
    n = n // 10     
    count = count + 1
    
print("the total numbers if the given input is",count)

# `````````````````````
# output
# `````````````````````
# n = 12345

# the total numbers if the given input is 5
