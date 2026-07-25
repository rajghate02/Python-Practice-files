Choco= 25
Child=4
Per_Child_Choco= Choco//Child
print("Number of Chocolates per Children are:",Per_Child_Choco)
Divideable_Choco= Child*Per_Child_Choco
Remaining_Choco= Choco - Divideable_Choco 
# Here instead of using the subtration operator we could have used %, 25%4, which woulf have given the remainder.
print("The Remaining Chocalates are:",Remaining_Choco)
# Correction 
remaining_Choco = Choco % Child
print("The Remaining Chocolates are:",remaining_Choco)