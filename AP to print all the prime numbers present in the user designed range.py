def is_prime(n):
    count = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False


def print_primes(num):
    for i in range(1, num+1):
        if is_prime(i):
            print(i)


num = int(input("Enter the limit: "))
print_primes(num)

# ``````````````````````````
# output
# ``````````````````````````
# 2
# 3
# 5
# 7
# 11
