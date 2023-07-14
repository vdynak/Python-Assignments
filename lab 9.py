
#victoria.dynak61@login.cuny.edu
#victoria dynak
#september 13, 2022
#this program creates a cipher.

word = input("Enter an all-small-letter string: ")
number = int(input("Enter a non-negative int to shift: "))

newword = ""

for x in word:
    difference = ord(x) - 97 + number
    wrap = difference % 26
    new_x = chr(97+wrap)
    newword = new_x + newword
output = newword[::-1]
    

print("ciphered string: ", output)
                          
