def isLeapYear(year):
    if (year % 100 !=0 and year %4==0) or(year % 400 == 0):
        return True
    else:
        return False
    
year= int (input('Enter a year:'))
c = isLeapYear(year)
if c:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

````````````````````
output
````````````````````
2026 is not a leap year

========================================================
                    or
=======================================================

def leapyearornot(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)

year = int(input("enter the Year"))

flag = leapyearornot(year)

if flag:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
