def countdigit(n, count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdigit(n,count)

def armstrong(n, pow, asn, temp):
    if n<=0:
        return asn==temp
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return armstrong(n, pow, asn, temp)

num=int(input('Enter the value')) #153
pow=countdigit(num,0)
flag=armstrong(num, pow, 0, num)

if flag:
    print('ASN')
else:
    print('Not an ASN')

output:
num = 153
ASN
