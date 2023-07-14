#victoria dynak
#victoria.dynak61@login.cuny.edu
#september 18, 2022
#reverse, capitalize, abbreviation.

phrase = input("input: ")
reversephrase = phrase[::-1]
print("user reverse: " + reversephrase)

revcap = reversephrase.upper()
print("user reverse upper: " + revcap)

abb = revcap.split()
abbreviation = ""
for x in abb:
    abbreviation += x[-1]
    abbr = abbreviation[::-1]
print("user abbreviation: ", abbr)
