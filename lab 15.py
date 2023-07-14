#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 3, 2022
#k-shape

phrase = input("Enter a phrase: ")
new = phrase.split()
for x in range(len(new),0,-1):
    print(" ".join(new[:x]))

for x in range(len(new)-1):
    print(" ".join(new[:x+2]))
