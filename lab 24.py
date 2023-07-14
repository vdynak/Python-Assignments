#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 17 2022
#number of words ending with a or b, fraction of words srarting with a or b

words = input("Enter a list of words, separated by a space: ")
amount = len(words.split(" "))
word = (words.split())
count = 0
trash = 0
for x in range(amount):
    currentword = word[x]
    if currentword[-1] == "a":
        count += 1
    elif currentword[-1] == "b":
        count += 1
    else:
        trash += 1
print("number of words: " +str(amount))
print("number of words ending with a or b: " + str(count))
fraction = (count/amount)
fractionfinal = round(fraction, 2)
print("fraction of words ending with a or b: " + str(fractionfinal))
        
