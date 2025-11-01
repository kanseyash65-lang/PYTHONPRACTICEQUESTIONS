# Check if a year is a leap year or not.

year = int(input("enter your birth year: "))

if(year % 4 == 0 & year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year.")    