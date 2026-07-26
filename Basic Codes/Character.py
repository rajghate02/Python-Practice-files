Chac=input("Enter a Character:")
if(len(Chac)!=1):
    print("Please Enter a Single Character")
elif Chac in "AEOUIaeoui":
    print("This Character is a Vowel")
elif Chac.isalpha():
    print("This Character is a Consonant")
elif Chac.isdigit():
    print("This Character is a Digit")
else:
    print("This Is a Special Character")
