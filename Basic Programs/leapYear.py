# A leap year is:

# Divisible by 400, or
# Divisible by 4 but not divisible by 100.

year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")