Mark = int(input("Enter Marks:"))
if(Mark >= 90):
    print("Grade:","A+")
elif(Mark>=80 and Mark<90):
    print("Grade:","A")
elif(Mark>= 70 and Mark<80):
    print("Grade","B")
elif(Mark>= 60 and Mark<70):
    print("Grade","C")
elif(Mark>= 50 and Mark<60):
    print("Grade","D")
elif(Mark>= 35 and Mark<50):
    print("Grade","E")
else:
    print("Grade","F")

