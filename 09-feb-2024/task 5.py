year=int(input("enter year: "))
if year% 400==0 and year% 100 ==0:
    print( year, "is a leap year")
elif year%4 ==0 and year% 100 !=0:
    print(year, "is a leap year")
else:
    print( year, "is not a leap year")


side1 = int(input("Enter side1"))
side2 = int(input("Enter side2"))
side3 = int(input("Enter side3"))
if side1==side2==side3:
    print("it is equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("it is isoscalea triangle")
else:
    print("it is scalea triangle")




