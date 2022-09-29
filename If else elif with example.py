#If Else Elif Statement
a=int(input("Enter Your Age = "))
if a>=18:
 print("You Are Eligible To Vote")
else:
    print("You are Not Eligible to vote Please wait for ",18-a,"Years")

#elif Example

a=int(input("Enter Number Of Days: "))
if a==0:
    print("Good you donot have any interest")
elif a>=1 and a<=5:
    print("Fine Amount: ",a*0.5)
elif a>5 and a<=10:
    print("Fine amount: ",a*1)
elif a>10 and a<=30:
    print("Fine amount : ",a*5)
elif a>30:
    print("Your MemberShip Was Cancelled")
else:
    print("Enter A Valid Days")


