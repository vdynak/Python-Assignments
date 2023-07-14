#victoria.dynak61@login.cuny.edu
#victoria dynak
#9/6/22
#This program tests the upper and lower case commands.

myString = input ("Enter name in format firstName lastName: ")
myNew = myString.split(" ")
lastname=myNew[1].upper()
firstname=myNew[0]
print("name in LASTNAME, firstName format:" , lastname+"," , firstname)
mySecond = input ("Enter user name of email: ")
loweremail = mySecond.lower()
print("email:"+" "+loweremail + "@hunter.cuny.edu")
