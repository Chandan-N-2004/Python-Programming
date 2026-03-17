def palindrome(n,rev,temp):
    if n<=0:
        return rev==temp
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return palindrome(n, rev, temp)  # for repeating a logic

num=int(input())
print("Input:", num)
flag=palindrome(num, 0, num)

if flag:
    print(f"yes {flag}")
else:
    print(f"not {flag}")

# output:
# num = 25213
# not False
