year=int(input("enter the number"))
if(year %400==0)or(year %100!=0)and(year %4==0):
    print("given year is a leap year")
else:
    print("given year is not a leap year")
