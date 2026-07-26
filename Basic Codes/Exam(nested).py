Math=float(input("Enter Math Marks:"))
Phy=float(input("Enter Phy Marks:"))
Chem=float(input("Enter Chem Marks:"))
Total_Marks= Math + Chem + Phy
Avg_Marks=round(Total_Marks/3,2)#Used round() so that the final output will only have 2 decimal spaces.
if(Math>100 or Phy>100 or Chem>100):#added this so that no value above 100 could be added.
    print("ERROR:please insert only values between 0 and 100")
else:
    if(Total_Marks>=104):
        if(Math<35 or Phy<35 or Chem<35):
            print("The Student has FAILED")
        else:
            print("The Student has PASSED")
    else:
        print("The Student has FAILED")
        # Fix: Moved these inside the 'else' block so they stop on error.
    print("The Total marks of the Student is:",Total_Marks)
    print("The Average Marks of the Student is:",Avg_Marks)









    