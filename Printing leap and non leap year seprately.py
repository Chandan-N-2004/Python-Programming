def leapyearornot(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)
    

def print_leap_years(start, end):
    
    print("Leap years between", start, "and", end, "are:")
    for year in range(start, end + 1):
        if leapyearornot(year):
            print(year)
            
    print("Non-Leap years between", start, "and", end, "are:")
    for year in range(start, end + 1):
        if not leapyearornot(year):
            print(year)
                   
start = int(input("Enter the start year: "))
end = int(input("Enter the end year: "))
if start > end:
    print("Invalid range")
else:
    print_leap_years(start, end)

`````````````````````````````````````````
output
`````````````````````````````````````````
Leap years between 2000 and 2005 are:
2000
2004
Non-Leap years between 2000 and 2005 are:
2001
2002
2003
2005
