year= int (input('Enter a year:'))
if (year % 100 !=0 and year %4==0) or(year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

````````
output
```````
2002 is not a leap year
