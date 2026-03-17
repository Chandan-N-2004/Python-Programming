def fiboseries(pos):
    n1, n2 =0,1
    while pos>0:
        print(n1,end=" ")
        temp = n1 + n2
        n1=n2
        n2=temp
        pos-=1
        
pos=int(input("enter num"))
fiboseries(pos)

# ````````````````
# output
# ```````````````
# pos = 6 

# 0  1 1 2 3 5
