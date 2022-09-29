#Nested Elif

n1=int(input("Enter Marks in 1st Subject: "))
n2=int(input("Enter marks in 2nd Subject : "))
n3=int(input("Enter Marks in 3rd Subject : "))

a=n1+n2+n3
total=a/3


if n1>=35 and n1<=100 and n2>=35 and n2<=100 and n3>=35 and n3<=100:
    print("Congratulations,You passed in all subjects")

    if total>=90 and total<=100:
        print("Your Scored Grade A")
    elif total>=80 and total<=89:
        print("You Scored Grade B")
    elif total>=60 and total<=79:
        print("You Scored Grade C")
    elif total>=50 and total<=59:
        print("You Scored Grade D")

    else:
        print("You Scored Grade E")

elif total>100:
    print("Please Enter A Valid Number")
else:
    print("Sorry to Inform You Haven't Get Enough Marks And Try Again With Your Hard Work")
