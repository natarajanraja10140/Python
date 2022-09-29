#Len in string

a="----Hai-----"
print(a)
print("Type of A : ",len(a))
print("Len with strip : ",len(a.strip("-")))
print("Len Of Left After Right - Last : ",len(a.lstrip("-")))
print("Len Of Right After - First : ",len(a.rstrip("-")))
a="01-03-2005"
print("Seperating Date From DD and MM and YY : ",a.partition("-"))

