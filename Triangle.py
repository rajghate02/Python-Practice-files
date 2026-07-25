Side1 = float(input("Enter the Side1 of a triangle:"))
Side2= float(input("Enter the Side2 of a triangle:"))
Side3= float(input("Enter the Side3 of a triangle:"))
if(Side1==Side2 and Side1==Side3 and Side2==Side3):
    print("This traingle is an Equilateral triangle")
elif(Side1==Side2 and Side3!=Side1 and Side3!=Side2 or Side3==Side2 and Side1!=Side3 and Side1!=Side2 or Side1==Side3 and Side3!=Side2 and Side1!=Side2 ):
    print("This triangle is an Isosceles triangle")
else:
    print("This traingle is a Scalene triangle")
# This program is not Accurate as Trangle test was not done.
# Also the program is not simple and too complex and untidy.
#Given Below is the correction:-
Side1 = float(input("Enter the Side1 of a triangle:"))
Side2= float(input("Enter the Side2 of a triangle:"))
Side3= float(input("Enter the Side3 of a triangle:"))
if(Side1+Side2<= Side3 or Side2+Side3<= Side1 or Side1+Side3 <= Side2):
    print("Not a Triangle")
elif(Side1==Side2 and Side2== Side3):
    print("This is a Equilateral  Triangle")
elif(Side1==Side2 or Side2==Side3 or Side1==Side3):
    print("This is a Isoceles Triangle")
else:
    print("This is a Scalene triangle")