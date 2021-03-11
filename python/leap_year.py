def is_leap(year):
    leap = False
    if (year%4==0 and year%100 !=0) or year%400==0:
        leap=True
    return leap

year = int(input())
print(is_leap(year))




# def is_leap(year):
#     leap = False
#     leap = (year%100!=0 and year%4==0) or (year%100==0 and year%4==0 and year%400==0)
#     # Write your logic here
    
#     return leap