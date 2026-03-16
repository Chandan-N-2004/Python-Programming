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

```````````````````````````````````````
output
```````````````````````````````````````
year = 2026 
2026 is not  a leap year
