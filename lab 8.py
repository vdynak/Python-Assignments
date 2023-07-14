#victoria.dynak61@login.cuny.edu
#victoria dynak
#September 11, 2022
#This program uses a string input to reveal the character, ASCII equivalence and the next two letters in ASCII table.
subject = input("Enter a phrase: ")
print("letter ASCII next_two_letter")
for x in subject:
    numvalue = ord(x)
    numvaluetwo = chr(numvalue + 2)
    print("%6c %5i %15c"%(x, numvalue, numvaluetwo))
    
