#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 17 2022
#binary to decimal values

number = input("Enter a string with 0 or 1 only: ")
num = 0
base = 2
weight = 1
length = len(number)

for x in reversed(range(length)):
    index = number[x]
    if index == '1':
        num+=weight
    elif index != '0': #!= means not equal to 
        print("Letter ", index, "is not allowed in the binary string.")

    weight*=base
print("num =", num)
