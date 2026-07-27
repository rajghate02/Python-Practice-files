
def Identifier(N):
    if(N%2==0):
        print("EVEN")
        return("EVEN")
    else:
        print("ODD")
        return("ODD")
Number = int(input("Enter the Number:"))
Identifier(Number)