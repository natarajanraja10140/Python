#For Loop

for i in range(0,5):
    print(i)

#Execute Many Times By Range
for i in range(2):
    a=int(input("Number1 :"))
    b=int(input("Number2 : "))
    c=a+b
    print(c)

#a-z=65-90
#A-Z=97-122



for i in range(65,70):
    print(chr(i))


for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")



