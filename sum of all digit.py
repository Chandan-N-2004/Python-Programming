def sumdigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumdigits(n // 10)


num = int(input("Enter number: "))

res = sumdigits(num)

print("Sum of digits:", res)

# output:
# Sum of digits: 6
