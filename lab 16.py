#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 5 2022
#semi-colon, first name last name abbrev.

names=input("Enter a list of names, seperated by a semicolon: ")

nameslisted=names.split(";")

length=len(nameslisted)


for x in range(length):
    fullname=nameslisted[x].split(" ")
    firstname=fullname[0][0]
    lastname=str(fullname[1])
    print(firstname + ".", lastname)
